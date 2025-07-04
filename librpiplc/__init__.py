"""
Copyright (c) 2025 Industrial Shields. All rights reserved.

This file is part of python3-librpiplc.

python3-librpiplc is free software: you can redistribute
it and/or modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation, either version
3 of the License, or (at your option) any later version.

python3-librpiplc is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import annotations

import ctypes
import os
import sys
import warnings
from contextlib import contextmanager
from ctypes.util import find_library
from typing import TYPE_CHECKING, Any, ClassVar

from .__about__ import __major__, __minor__, __patch__, __version__
from .exceptions import UnknownPLCConfError
from .lib_types import DigitalLevel, PinType
from .mapping import PLCMappingDict

if TYPE_CHECKING:
    from collections.abc import Generator


C_ABI_VERSION_4 = 4


class CPeripherals(ctypes.Structure):
    """
    C structure to hold peripheral information for the RPIPLC library.

    Attributes:
        arrayMCP23008 (ctypes.POINTER(ctypes.c_uint8)): Pointer to an array of MCP23008 addresses.
        numArrayMCP23008 (ctypes.c_size_t): Number of MCP23008 addresses.
        arrayADS1015 (ctypes.POINTER(ctypes.c_uint8)): Pointer to an array of ADS1015 addresses.
        numArrayADS1015 (ctypes.c_size_t): Number of ADS1015 addresses.
        arrayPCA9685 (ctypes.POINTER(ctypes.c_uint8)): Pointer to an array of PCA9685 addresses.
        numArrayPCA9685 (ctypes.c_size_t): Number of PCA9685 addresses.
        arrayLTC2309 (ctypes.POINTER(ctypes.c_uint8)): Pointer to an array of LTC2309 addresses.
        numArrayLTC2309 (ctypes.c_size_t): Number of LTC2309 addresses.
        arrayMCP23017 (ctypes.POINTER(ctypes.c_uint8)): Pointer to an array of MCP23017 addresses.
        numArrayMCP23017 (ctypes.c_size_t): Number of MCP23017 addresses.

    """

    _fields_: ClassVar[list[tuple[str, Any]]] = [
        ("arrayMCP23008", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayMCP23008", ctypes.c_size_t),
        ("arrayADS1015", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayADS1015", ctypes.c_size_t),
        ("arrayPCA9685", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayPCA9685", ctypes.c_size_t),
        ("arrayLTC2309", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayLTC2309", ctypes.c_size_t),
        ("arrayMCP23017", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayMCP23017", ctypes.c_size_t),
    ]


class RPIPLCClass:
    """
    Class to manage Raspberry Pi PLC operations.

    This class provides methods to directly interface with the C library.

    Attributes:
        INPUT (PinType): Constant for input pin mode.
        OUTPUT (PinType): Constant for output pin mode.
        LOW (DigitalLevel): Constant for low digital level.
        HIGH (DigitalLevel): Constant for high digital level.

    """

    INPUT = PinType.INPUT
    OUTPUT = PinType.OUTPUT
    LOW = DigitalLevel.LOW
    HIGH = DigitalLevel.HIGH

    def __init__(self) -> None:
        """
        Initialize the RPIPLCClass instance and loads the C library into memory.

        If some symbol is undefined, it will raise UnknownPLCConfError.

        Raises:
            UnknownPLCConfError: If the C library version is incompatible.

        """
        self._mapping = PLCMappingDict({})
        self._is_initialized = False
        libname = find_library("rpiplc")
        if not libname:
            msg = "librpiplc is not installed in this system"
            raise OSError(msg)
        self._dyn_lib: ctypes.CDLL = ctypes.cdll.LoadLibrary(libname)

        incompatible_msg = "The librpiplc C library is not compatible with this Python library"

        try:
            c_version_major = ctypes.c_int.in_dll(
                self._dyn_lib, "LIB_RPIPLC_VERSION_MAJOR_NUM"
            ).value
            c_version_minor = ctypes.c_int.in_dll(
                self._dyn_lib, "LIB_RPIPLC_VERSION_MINOR_NUM"
            ).value
            c_version_patch = ctypes.c_int.in_dll(
                self._dyn_lib, "LIB_RPIPLC_VERSION_PATCH_NUM"
            ).value
            c_version = ctypes.c_char_p.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION").value
            if (
                c_version is None
                or c_version_patch is None
                or c_version_minor is None
                or c_version_major is None
            ):
                raise UnknownPLCConfError(incompatible_msg)

            self.c_version_major = c_version_major
            self.c_version_minor = c_version_minor
            self.c_version_patch = c_version_patch
            self.c_version = c_version.decode("utf-8")
        except ValueError as exc:
            raise UnknownPLCConfError(incompatible_msg) from exc

        self.python_version_major = __major__
        self.python_version_minor = __minor__
        self.python_version_patch = __patch__
        self.python_version = __version__

        self._is_library_old = self.c_version_major < C_ABI_VERSION_4

        self._c_prepare_arg_and_return_types()

        self._c_struct: CPeripherals | None = None

    def __new__(cls) -> RPIPLCClass:  # noqa: PYI034
        """Override method to make the class a singleton."""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def _c_prepare_arg_and_return_types(self) -> None:
        """Set the function argument and return types of the C library."""
        # int initExpandedGPIO(bool restart);
        self._dyn_lib.initExpandedGPIO.argtypes = [ctypes.c_bool]
        self._dyn_lib.initExpandedGPIO.restype = ctypes.c_int

        # int deinitExpandedGPIO(void);
        self._dyn_lib.deinitExpandedGPIO.argtypes = []
        self._dyn_lib.deinitExpandedGPIO.restype = ctypes.c_int

        if not self._is_library_old:
            # int deinitExpandedGPIONoReset(void);
            self._dyn_lib.deinitExpandedGPIONoReset.argtypes = []
            self._dyn_lib.deinitExpandedGPIONoReset.restype = ctypes.c_int

        # int pinMode(uint32_t pin, uint8_t mode);
        self._dyn_lib.pinMode.argtypes = [ctypes.c_uint32, ctypes.c_uint8]
        self._dyn_lib.pinMode.restype = ctypes.c_int

        # int digitalWrite(uint32_t pin, uint8_t value);
        self._dyn_lib.digitalWrite.argtypes = [ctypes.c_uint32, ctypes.c_uint8]
        self._dyn_lib.digitalWrite.restype = ctypes.c_int

        # int digitalRead(uint32_t pin);
        self._dyn_lib.digitalRead.argtypes = [ctypes.c_uint32]
        self._dyn_lib.digitalRead.restype = ctypes.c_int

        # int analogWrite(uint32_t pin, uint16_t value);
        self._dyn_lib.analogWrite.argtypes = [ctypes.c_uint32, ctypes.c_uint16]
        self._dyn_lib.analogWrite.restype = ctypes.c_int

        # int analogWriteSetFrequency(uint32_t pin, uint32_t desired_freq);
        self._dyn_lib.analogWriteSetFrequency.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
        self._dyn_lib.analogWriteSetFrequency.restype = ctypes.c_int

        # uint16_t analogRead(uint32_t pin);
        self._dyn_lib.analogRead.argtypes = [ctypes.c_uint32]
        self._dyn_lib.analogRead.restype = ctypes.c_uint16

        # int digitalWriteAll(uint8_t addr, uint32_t values);
        self._dyn_lib.digitalWriteAll.argtypes = [ctypes.c_uint8, ctypes.c_uint32]
        self._dyn_lib.digitalWriteAll.restype = ctypes.c_int

        # int digitalReadAll(uint8_t addr, void* values);
        self._dyn_lib.digitalReadAll.argtypes = [ctypes.c_uint8, ctypes.POINTER(ctypes.c_void_p)]
        self._dyn_lib.digitalReadAll.restype = ctypes.c_int

        # int analogWriteAll(uint8_t addr, const void* values);
        self._dyn_lib.analogWriteAll.argtypes = [ctypes.c_uint8, ctypes.POINTER(ctypes.c_void_p)]
        self._dyn_lib.analogWriteAll.restype = ctypes.c_int

    def _c_populate_arrays(self, version_name: str, model_name: str) -> None:
        """
        Populate the library's peripheral arrays based on the version and model.

        Args:
            version_name (str): The version name of the PLC.
            model_name (str): The model name of the PLC.

        """
        self._c_struct = CPeripherals.in_dll(self._dyn_lib, "_peripherals_struct")

        if version_name in ["RPIPLC_V3", "RPIPLC_V4", "RPIPLC_V6"]:
            mcp23008_array = (ctypes.c_uint8 * 2)(0x20, 0x21)
        else:
            mcp23008_array = (ctypes.c_uint8 * 0)()
        self._c_struct.arrayMCP23008 = mcp23008_array
        self._c_struct.numArrayMCP23008 = len(mcp23008_array)

        # Populate arrayADS1015
        if version_name == "RPIPLC_V3":
            ads1015_array = (ctypes.c_uint8 * 4)(0x48, 0x49, 0x4A, 0x4B)
        elif version_name == "TOUCHBERRY_PI_V1":
            ads1015_array = (ctypes.c_uint8 * 1)(0x49)
        else:
            ads1015_array = (ctypes.c_uint8 * 0)()
        self._c_struct.arrayADS1015 = ads1015_array
        self._c_struct.numArrayADS1015 = len(ads1015_array)

        # Populate arrayPCA9685
        if version_name in ["RPIPLC_V3", "RPIPLC_V4", "RPIPLC_V6"]:
            pca9685_array = (ctypes.c_uint8 * 2)(0x40, 0x41)
        else:
            pca9685_array = (ctypes.c_uint8 * 0)()
        self._c_struct.arrayPCA9685 = pca9685_array
        self._c_struct.numArrayPCA9685 = len(pca9685_array)

        # Populate arrayLTC2309
        if version_name in ["RPIPLC_V4", "RPIPLC_V6"]:
            if model_name in ["RPIPLC_21", "RPIPLC_19R", "RPIPLC_CPU"]:
                ltc2309_array = (ctypes.c_uint8 * 2)(0x08, 0x0A)
            else:
                ltc2309_array = (ctypes.c_uint8 * 3)(0x08, 0x0A, 0x28)
        else:
            ltc2309_array = (ctypes.c_uint8 * 0)()
        self._c_struct.arrayLTC2309 = ltc2309_array
        self._c_struct.numArrayLTC2309 = len(ltc2309_array)

        mcp23017_array = (ctypes.c_uint8 * 0)()
        self._c_struct.arrayMCP23017 = mcp23017_array
        self._c_struct.numArrayMCP23017 = len(mcp23017_array)

    def init(self, version_name: str, model_name: str, *, restart: bool = False) -> int:
        """
        Initialize the RPIPLC library with the specified version and model.

        Args:
            version_name (str): The version name of the PLC.
            model_name (str): The model name of the PLC.
            restart (bool): Whether to restart the peripherals or not (default is False).

        Returns:
            int: Return code from the initialization function (0 for success, 1 if it was
                 already initialized, others for failure).

        Raises:
            UnknownPLCConfError: If the version or model is unknown.

        """
        if model_name == "RPIPLC":
            model_name = "RPIPLC_CPU"
            warnings.warn(
                "RPIPLC model is deprecated, please use RPIPLC_CPU instead.",
                category=DeprecationWarning,
                stacklevel=2,
            )

        available_versions = {
            "RPIPLC_V6": "rpiplc_mapping_v6",
            "RPIPLC_V4": "rpiplc_mapping_v4",
            "RPIPLC_V3": "rpiplc_mapping_v3",
            "UPSAFEPI_V6": "upsafepi_mapping_v6",
            "GATEBERRY_V9": "gateberry_mapping_v9",
            "TOUCHBERRY_PI_V1": "touchberry_pi_mapping_v1",
        }

        hw = {}
        try:
            module_name = available_versions[version_name]
            if self._is_library_old:
                module_name = f"old_{module_name}"
            hw = __import__(f"librpiplc.{module_name}", fromlist=["hw"]).hw
        except KeyError as exc:
            pretty_versions = "\n" + "\n".join(available_versions.keys())
            error_str = (
                f"Unknown version {version_name}, the only available versions "
                f"for {version_name} are:{pretty_versions}"
            )
            raise UnknownPLCConfError(error_str) from exc

        try:
            self._mapping = hw[model_name]
        except KeyError as exc:
            pretty_models = "\n" + "\n".join(hw.keys())
            error_str = (
                f"Unknown model {model_name}, the only available models "
                f"for {version_name} are:{pretty_models}"
            )
            raise UnknownPLCConfError(error_str) from exc

        if not self._is_library_old:
            self._c_populate_arrays(version_name, model_name)
        rc = int(self._dyn_lib.initExpandedGPIO(restart))
        self._is_initialized = rc in (0, 1)
        return rc

    @contextmanager
    def with_init(
        self,
        version_name: str,
        model_name: str,
        *,
        restart: bool = False,
        restart_when_closing: bool = True,
    ) -> Generator[int, None, None]:
        """
        Context manager to initialize the rpiplc singleton with "with" statements.

        Args:
            version_name (str): The version name of the PLC.
            model_name (str): The model name of the PLC.
            restart (bool): Whether to restart the peripherals or not (default is False).
            restart_when_closing (bool): Whether to restart the peripherals when exiting the with
                                         block.

        Raises:
            UnknownPLCConfError: If the version or model is unknown.

        """
        rc = self.init(version_name, model_name, restart=restart)
        yield rc
        self.deinit(restart=restart_when_closing)

    def deinit(self, *, restart: bool = True) -> int:
        """
        Deinitialize the RPIPLC library.

        This method cleans up the library and resets the internal state.

        Returns:
            int: Return code from the deinitialization function (0 for success, 1 if it was already
                 deinitialized, others for failure).

        Raises:
            UnknownPLCConfError: If the library version doesn't support not restarting when calling
                            deinit.

        """
        if not self._is_library_old:
            if restart:
                rc = int(self._dyn_lib.deinitExpandedGPIO())
            else:
                rc = int(self._dyn_lib.deinitExpandedGPIONoReset())
        else:
            if not restart:
                msg = "This library version doesn't support de-initializing without restarting"
                raise UnknownPLCConfError(msg)
            rc = int(self._dyn_lib.deinitExpandedGPIO())

        if rc in (0, 2):
            self._mapping = PLCMappingDict({})
            self._is_initialized = False
            self._c_struct = None

        return rc

    def pin_mode(self, pin_name: str, mode: PinType) -> int:
        """
        Set the mode of a specified pin.

        Args:
            pin_name (str): The name of the pin to set.
            mode (PinType): The mode to set for the pin (rpiplc.INPUT or rpiplc.OUTPUT).

        Returns:
            int: Return code from the pinMode function (0 for success, non-zero for failure).

        """
        return int(self._dyn_lib.pinMode(self._mapping[pin_name], mode.value))

    def digital_write(self, pin_name: str, level: DigitalLevel | int | bool) -> int:  # noqa: FBT001
        """
        Write a digital value to a specified pin.

        Args:
            pin_name (str): The name of the pin to write to.
            level (DigitalLevel): The digital level to write (LOW or HIGH).

        Returns:
            int: Return code from the digitalWrite function (0 for success, non-zero for failure).

        """
        if isinstance(level, bool):
            level = self.HIGH if level else self.LOW
        elif isinstance(level, int):
            warnings.warn(
                "Passing an int to digital_write is not recommended, use HIGH, LOW, booleans, or "
                "the DigitalLevel enum. The usage of integers will be removed in future versions.",
                category=DeprecationWarning,
                stacklevel=2,
            )
            level = self.HIGH if level > 0 else self.LOW
        return int(self._dyn_lib.digitalWrite(self._mapping[pin_name], level.value))

    def digital_read(self, pin_name: str) -> int:
        """
        Read a digital value from a specified pin.

        Args:
            pin_name (str): The name of the pin to read from.

        Returns:
            int: The digital value read from the pin (0 or 1).

        """
        return int(self._dyn_lib.digitalRead(self._mapping[pin_name]))

    def analog_write_set_frequency(self, pin_name: str, freq: int) -> int:
        """
        Set the frequency for PWM on a specified pin.

        Args:
            pin_name (str): The name of the pin to set the frequency for.
            freq (int): The desired frequency in Hz.

        Returns:
            int: Return code from the analogWriteSetFrequency function (0 for success, non-zero for
                 failure).

        """
        return int(self._dyn_lib.analogWriteSetFrequency(self._mapping[pin_name], freq))

    def analog_write(self, pin_name: str, value: int) -> int:
        """
        Write an analog value to a specified pin.

        Args:
            pin_name (str): The name of the pin to write to.
            value (int): The analog value to write (it's normally a number between 0 and 4095).

        Returns:
            int: Return code from the analogWrite function (0 for success, non-zero for failure).

        """
        return int(self._dyn_lib.analogWrite(self._mapping[pin_name], value))

    def analog_read(self, pin_name: str) -> int:
        """
        Read an analog value from a specified pin.

        Args:
            pin_name (str): The name of the pin to read from.

        Returns:
            int: The analog value read from the pin (it's normally a number between 0 and 4095).

        """
        return int(self._dyn_lib.analogRead(self._mapping[pin_name]))

    def delay(self, value: int) -> None:
        """
        Pause execution for a specified number of milliseconds.

        Args:
            value (int): The number of milliseconds to delay.

        """
        self._dyn_lib.delay(value)

    def delay_microseconds(self, value: int) -> None:
        """
        Pause execution for a specified number of microseconds.

        Args:
            value (int): The number of microseconds to delay.

        """
        self._dyn_lib.delayMicroseconds(value)


def is_installing() -> bool:
    """Return true if we are using pip to install the package."""
    return "pip" in sys.modules or "pip" in os.environ.get("PYTHONPATH", "")


if not is_installing():
    rpiplc = RPIPLCClass()

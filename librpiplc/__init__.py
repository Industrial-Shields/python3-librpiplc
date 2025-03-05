"""
Copyright (c) 2025 Industrial Shields. All rights reserved

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
import ctypes
from enum import Enum
from typing import Optional
from .types import DigitalLevel, PeripheralType, PinType
from .exceptions import UnknownPLCConf



class C_Peripherals(ctypes.Structure):
    _fields_ = [
        ("arrayMCP23008", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayMCP23008", ctypes.c_size_t),
        ("arrayADS1015", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayADS1015", ctypes.c_size_t),
        ("arrayPCA9685", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayPCA9685", ctypes.c_size_t),
        ("arrayLTC2309", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayLTC2309", ctypes.c_size_t),
        ("arrayMCP23017", ctypes.POINTER(ctypes.c_uint8)),
        ("numArrayMCP23017", ctypes.c_size_t)
    ]


class RPIPLCClass:
    INPUT = PinType.INPUT
    OUTPUT = PinType.OUTPUT
    LOW = DigitalLevel.LOW
    HIGH = DigitalLevel.HIGH

    def __init__(self) -> None:
        self._mapping = {}
        self._is_initialized = False
        self._dyn_lib = ctypes.cdll.LoadLibrary("librpiplc.so")

        incompatible_msg = "The librpiplc C library is not compatible with this Python library"

        try:
            c_version_major = ctypes.c_int.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION_MAJOR_NUM") \
                                          .value
            c_version_minor = ctypes.c_int.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION_MINOR_NUM") \
                                          .value
            c_version_patch = ctypes.c_int.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION_PATCH_NUM") \
                                          .value
            c_version = ctypes.c_char_p.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION").value
            if c_version is None \
               or c_version_patch is None \
               or c_version_minor is None \
               or c_version_major is None:
                raise UnknownPLCConf(incompatible_msg)

            self.c_version_major = c_version_major
            self.c_version_minor = c_version_minor
            self.c_version_patch = c_version_patch
            self.c_version = c_version.decode("utf-8")
        except ValueError as exc:
            raise UnknownPLCConf(incompatible_msg) from exc

        self.python_version_major = self.c_version_major
        self.python_version_minor = self.c_version_minor
        self.python_version_patch = 0
        self.python_version = f"{self.python_version_major}" \
            f".{self.python_version_minor}.{self.python_version_patch}"

        self._c_prepare_arg_and_return_types()


    # Make it a singleton
    def __new__(cls) -> "RPIPLCClass":
        if not hasattr(cls, 'instance'):
            cls.instance = super(RPIPLCClass, cls).__new__(cls)
        return cls.instance

    def _c_prepare_arg_and_return_types(self) -> None:
        # int initExpandedGPIOV2(bool restart);
        self._dyn_lib.initExpandedGPIOV2.argtypes = [ctypes.c_bool]
        self._dyn_lib.initExpandedGPIOV2.restype = ctypes.c_int

        # int deinitExpandedGPIO(void);
        self._dyn_lib.deinitExpandedGPIO.argtypes = []
        self._dyn_lib.deinitExpandedGPIO.restype = ctypes.c_int

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
        _c_struct = C_Peripherals.in_dll(self._dyn_lib, "_peripherals_struct")

        if version_name in ["RPIPLC_V3", "RPIPLC_V4", "RPIPLC_V6"]:
            mcp23008_array = (ctypes.c_uint8 * 2)(0x20, 0x21)
        else:
            mcp23008_array = (ctypes.c_uint8 * 0)()
        _c_struct.arrayMCP23008 = mcp23008_array
        _c_struct.numArrayMCP23008 = len(mcp23008_array)

        # Populate arrayADS1015
        if version_name == "RPIPLC_V3":
            ads1015_array = (ctypes.c_uint8 * 4)(0x48, 0x49, 0x4A, 0x4B)
        else:
            ads1015_array = (ctypes.c_uint8 * 0)()
        _c_struct.arrayADS1015 = ads1015_array
        _c_struct.numArrayADS1015 = len(ads1015_array)

        # Populate arrayPCA9685
        if version_name in ["RPIPLC_V3", "RPIPLC_V4", "RPIPLC_V6"]:
            pca9685_array = (ctypes.c_uint8 * 2)(0x40, 0x41)
        else:
            pca9685_array = (ctypes.c_uint8 * 0)()
        _c_struct.arrayPCA9685 = pca9685_array
        _c_struct.numArrayPCA9685 = len(pca9685_array)

        # Populate arrayLTC2309
        if version_name in ["RPIPLC_V4", "RPIPLC_V6"]:
            if model_name in ["RPIPLC_21", "RPIPLC_19R"]:
                ltc2309_array = (ctypes.c_uint8 * 2)(0x08, 0x0A)
            else:
                ltc2309_array = (ctypes.c_uint8 * 3)(0x08, 0x0A, 0x28)
        else:
            ltc2309_array = (ctypes.c_uint8 * 0)()
        _c_struct.arrayLTC2309 = ltc2309_array
        _c_struct.numArrayLTC2309 = len(ltc2309_array)

        mcp23017_array = (ctypes.c_uint8 * 0)()
        _c_struct.arrayMCP23017 = mcp23017_array
        _c_struct.numArrayMCP23017 = len(mcp23017_array)


    def init(self, version_name: str, model_name: str, restart: bool = False) -> int:
        available_versions = {
            "RPIPLC_V6": "rpiplc_mapping_v6",
            "RPIPLC_V4": "rpiplc_mapping_v4",
            "RPIPLC_V3": "rpiplc_mapping_v3",
            "UPSAFEPI_V6": "upsafepi_mapping_v6"
        }

        hw = {}
        try:
            module_name = available_versions[version_name]
            hw = __import__(f"librpiplc.{module_name}", fromlist=["hw"]).hw
        except KeyError as exc:
            pretty_versions = "\n" + '\n'.join(hw.keys())
            error_str = f"Unknown version {version_name}, the only available versions" \
                f"for {version_name} are:{pretty_versions}"
            raise UnknownPLCConf(error_str) from exc

        try:
            self._mapping = hw[model_name]
        except KeyError as exc:
            pretty_models = "\n" + '\n'.join(hw.keys())
            error_str = f"Unknown model {model_name}, the only available models" \
                f"for {version_name} are:{pretty_models}"
            raise UnknownPLCConf(error_str) from exc

        self._c_populate_arrays(version_name, model_name)
        rc = int(self._dyn_lib.initExpandedGPIOV2(restart))
        self._is_initialized = rc in (0, 1)
        return rc

    def deinit(self) -> int:
        rc = int(self._dyn_lib.deinitExpandedGPIO())
        if rc < 0:
            return rc

        self._mapping = {}
        self._is_initialized = False

        return rc


    def pin_mode(self, pin_name: str, mode: PinType) -> int: #type no-any-return
        return int(self._dyn_lib.pinMode(self._mapping[pin_name], mode.value))

    def digital_write(self, pin_name: str, level: DigitalLevel) -> int:
        return int(self._dyn_lib.digitalWrite(self._mapping[pin_name], level.value))

    def digital_read(self, pin_name: str) -> int:
        return int(self._dyn_lib.digitalRead(self._mapping[pin_name]))

    def analog_write_set_frequency(self, pin_name: str, freq: int) -> int:
        return int(self._dyn_lib.analogWriteSetFrequency(self._mapping[pin_name], freq))

    def analog_write(self, pin_name: str, value: int) -> int:
        return int(self._dyn_lib.analogWrite(self._mapping[pin_name], value))

    def analog_read(self, pin_name: str) -> int:
        return int(self._dyn_lib.analogRead(self._mapping[pin_name]))

    def delay(self, value: int) -> None:
        self._dyn_lib.delay(value)

    def delay_microseconds(self, value: int) -> None:
        self._dyn_lib.delayMicroseconds(value)



rpiplc = RPIPLCClass()

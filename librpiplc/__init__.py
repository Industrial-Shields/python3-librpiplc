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
from ctypes import cdll, c_uint8, c_int, c_size_t, c_char_p, POINTER, Structure
from enum import Enum
from .mapping import PeripheralType
from .exceptions import UnknownPLCConf



class PinType(Enum):
    INPUT = 0
    OUTPUT = 1

class DigitalLevel(Enum):
    LOW = 0
    HIGH = 1


class Peripherals(Structure):
    _fields_ = [
        ("arrayMCP23008", POINTER(c_uint8)),
        ("numArrayMCP23008", c_size_t),
        ("arrayADS1015", POINTER(c_uint8)),
        ("numArrayADS1015", c_size_t),
        ("arrayPCA9685", POINTER(c_uint8)),
        ("numArrayPCA9685", c_size_t),
        ("arrayLTC2309", POINTER(c_uint8)),
        ("numArrayLTC2309", c_size_t),
        ("arrayMCP23017", POINTER(c_uint8)),
        ("numArrayMCP23017", c_size_t)
    ]




class RPIPLCClass:
    INPUT = PinType.INPUT
    OUTPUT = PinType.OUTPUT
    LOW = DigitalLevel.LOW
    HIGH = DigitalLevel.HIGH

    def __init__(self):
        self._mapping = None
        self._dyn_lib = cdll.LoadLibrary("librpiplc.so")

        self.c_version_major = c_int.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION_MAJOR_NUM").value
        self.c_version_minor = c_int.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION_MINOR_NUM").value
        self.c_version_patch = c_int.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION_PATCH_NUM").value
        self.c_version = c_char_p.in_dll(self._dyn_lib, "LIB_RPIPLC_VERSION").value.decode("utf-8")
        self.python_version_major = self.c_version_major
        self.python_version_minor = self.c_version_minor
        self.python_version_patch = 0
        self.python_version = f"{self.python_version_major}.{self.python_version_minor}.{self.python_version_patch}"

    # Make it a singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RPIPLCClass, cls).__new__(cls)
        return cls.instance

    def _populateArrays(self, version_name: str, model_name: str) -> int:
        _c_struct = Peripherals.in_dll(self._dyn_lib, "_peripherals_struct")

        if version_name in ["RPIPLC_V3", "RPIPLC_V4", "RPIPLC_V6"]:
            mcp23008_array = (c_uint8 * 2)(0x20, 0x21)
        else:
            mcp23008_array = (c_uint8 * 0)()
        _c_struct.arrayMCP23008 = mcp23008_array
        _c_struct.numArrayMCP23008 = len(mcp23008_array)

        # Populate arrayADS1015
        if version_name == "RPIPLC_V3":
            ads1015_array = (c_uint8 * 4)(0x48, 0x49, 0x4A, 0x4B)
        else:
            ads1015_array = (c_uint8 * 0)()
        _c_struct.arrayADS1015 = ads1015_array
        _c_struct.numArrayADS1015 = len(ads1015_array)

        # Populate arrayPCA9685
        if version_name in ["RPIPLC_V3", "RPIPLC_V4", "RPIPLC_V6"]:
            pca9685_array = (c_uint8 * 2)(0x40, 0x41)
        else:
            pca9685_array = (c_uint8 * 0)()
        _c_struct.arrayPCA9685 = pca9685_array
        _c_struct.numArrayPCA9685 = len(pca9685_array)

        # Populate arrayLTC2309
        if version_name in ["RPIPLC_V4", "RPIPLC_V6"]:
            if model_name in ["RPIPLC_21", "RPIPLC_19R"]:
                ltc2309_array = (c_uint8 * 2)(0x08, 0x0A)
            else:
                ltc2309_array = (c_uint8 * 3)(0x08, 0x0A, 0x28)
        else:
            ltc2309_array = (c_uint8 * 0)()
        _c_struct.arrayLTC2309 = ltc2309_array
        _c_struct.numArrayLTC2309 = len(ltc2309_array)

        mcp23017_array = (c_uint8 * 0)()
        _c_struct.arrayMCP23017 = mcp23017_array
        _c_struct.numArrayMCP23017 = len(mcp23017_array)


    def init(self, version_name: str, model_name: str, restart: bool = False) -> int:
        available_versions = {
            "RPIPLC_V6": "rpiplc_mapping_v6",
            "RPIPLC_V4": "rpiplc_mapping_v4",
            "RPIPLC_V3": "rpiplc_mapping_v3",
            "UPSAFEPI_V6": "upsafepi_mapping_v6"
        }

        hw = None
        try:
            module_name = available_versions[version_name]
            hw = __import__(f"librpiplc.{module_name}", fromlist=["hw"]).hw
        except KeyError as exc:
            pretty_available_versions = "\n" + '\n'.join(hw.keys())
            raise UnknownPLCConf(f"Unknown version {version_name}, the only available versions for {version_name} are:{pretty_available_versions}") from exc

        try:
            self._mapping = hw[model_name]
        except KeyError as exc:
            pretty_available_models = "\n" + '\n'.join(hw.keys())
            raise UnknownPLCConf(f"Unknown model {model_name}, the only available models for {version_name} are:{pretty_available_models}") from exc

        self._populateArrays(version_name, model_name)

        return self._dyn_lib.initExpandedGPIOV2(restart)

    def deinit(self) -> int:
        rc = self._dyn_lib.deinitExpandedGPIO()
        if rc < 0:
            return rc

        self._mapping = None

        return rc


    def pin_mode(self, pin_name: str, mode: PinType) -> int:
        self._dyn_lib.pinMode(self._mapping[pin_name], mode.value)

    def digital_write(self, pin_name: str, level: DigitalLevel) -> int:
        return self._dyn_lib.digitalWrite(self._mapping[pin_name], level.value)

    def digital_read(self, pin_name: str) -> int:
        return self._dyn_lib.digitalRead(self._mapping[pin_name])

    def analog_write_set_frequency(self, pin_name: str, freq: int) -> int:
        return self._dyn_lib.analogWriteSetFrequency(self._mapping[pin_name], freq)

    def analog_write(self, pin_name: str, value: int) -> int:
        return self._dyn_lib.analogWrite(self._mapping[pin_name], value)

    def analog_read(self, pin_name: str) -> int:
        return self._dyn_lib.analogRead(self._mapping[pin_name])

    def delay(self, value: int) -> int:
        self._dyn_lib.delay(value)

    def delay_microseconds(self, value: int) -> int:
        self._dyn_lib.delayMicroseconds(value)



rpiplc = RPIPLCClass()

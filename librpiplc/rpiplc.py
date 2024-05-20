"""
Copyright (c) 2024 Industrial Shields. All rights reserved

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

from ctypes import cdll, c_int, c_char_p

_rpiplc = cdll.LoadLibrary("librpiplc.so")
c_version_major = c_int.in_dll(_rpiplc, "LIB_RPIPLC_VERSION_MAJOR_NUM").value
c_version_minor = c_int.in_dll(_rpiplc, "LIB_RPIPLC_VERSION_MINOR_NUM").value
c_version_patch = c_int.in_dll(_rpiplc, "LIB_RPIPLC_VERSION_PATCH_NUM").value
c_version = c_char_p.in_dll(_rpiplc, "LIB_RPIPLC_VERSION").value.decode("utf-8")
python_version_major = c_version_major
python_version_minor = c_version_minor
python_version_patch = 1
python_version = f"{python_version_major}.{python_version_minor}.{python_version_patch}"

INPUT = 0
OUTPUT = 1

LOW = 0
HIGH = 1

class UnknownPLCConf(Exception):
     def __init__(self, message):
        super().__init__(message)

# This function loads into memory the correct mapping of the version and model you choose
def init(version_name, model_name, restart=False):
    global _hw

    rc = _rpiplc.initExpandedGPIO(restart)
    if rc < 0:
        return rc

    if version_name == "RPIPLC_V6":
        from .folder_rpiplc.models_v6 import hw
    elif version_name == "RPIPLC_V4":
        from .folder_rpiplc.models_v4 import hw
    elif version_name == "RPIPLC_V3":
        from .folder_rpiplc.models_v3 import hw
    elif version_name == "UPSAFEPI_V6":
        from .upsafepi.models_v6 import hw
    else:
        raise UnknownPLCConf(f"Unknown version {version_name}, the only available versions are RPIPLC_V6, RPIPLC_V4 and RPIPLC_V3")

    available_models = hw.keys()
    if model_name not in available_models:
        pretty_available_models = "\n" + '\n'.join(available_models)
        raise UnknownPLCConf(f"Unknown model {model_name}, the only available models for {version_name} are:{pretty_available_models}")

    _hw = hw[model_name]

    return rc

def deinit():
     global _hw

     rc = _rpiplc.deinitExpandedGPIO()
     if rc < 0:
         return rc

     _hw = None

     return rc

def pin_mode(pin_name, mode):
    return _rpiplc.pinMode(_hw[pin_name], mode)

def digital_write(pin_name, value):
    return _rpiplc.digitalWrite(_hw[pin_name], value)

def digital_read(pin_name):
    return _rpiplc.digitalRead(_hw[pin_name])

def analog_write_set_frequency(pin_name, freq):
     return _rpiplc.analogWriteSetFrequency(_hw[pin_name], freq)

def analog_write(pin_name, value):
    return _rpiplc.analogWrite(_hw[pin_name], value)

def analog_read(pin_name):
    return _rpiplc.analogRead(_hw[pin_name])

def delay(value):
    _rpiplc.delay(value)

def delay_microseconds(value):
    _rpiplc.delayMicroseconds(value)

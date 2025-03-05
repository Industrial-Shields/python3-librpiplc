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
from enum import Enum
from typing import Any, Dict
from .exceptions import UnknownPin
from .types import PeripheralType



class MappingDict(dict): # type: ignore
    def __getitem__(self, key: Any) -> Any:
        try:
            return super().__getitem__(key)
        except KeyError as exc:
            raise UnknownPin(key) from exc


def _make_pin_plc(peripheral_type: PeripheralType, byte2: int, byte3: int, byte4: int) -> int:
    return ((peripheral_type.value & 0xFF) << 24) | \
        ((byte2 & 0xFF) << 16) | \
        ((byte3 & 0xFF) << 8) | \
        (byte4 & 0xFF)

def make_pin_direct(index: int) -> int:
    return _make_pin_plc(PeripheralType.PLC_DIRECT, (index & 0xFF0000) >> 16, (index & 0xFF00) >> 8, index)

def make_pin_pca9685(addr: int, index: int) -> int:
    return _make_pin_plc(PeripheralType.PLC_PCA9685, addr, 0x00, index)

def make_pin_mcp23008(addr: int, index: int) -> int:
    return _make_pin_plc(PeripheralType.PLC_MCP23008, addr, 0x00, index)

def make_pin_mcp23017(addr: int, index: int) -> int:
    return _make_pin_plc(PeripheralType.PLC_MCP23017, addr, 0x00, index)

def make_pin_ltc2309(addr: int, index: int) -> int:
    return _make_pin_plc(PeripheralType.PLC_LTC2309, addr, 0x00, index)

def make_pin_ads1015(addr: int, index: int) -> int:
    return _make_pin_plc(PeripheralType.PLC_ADS1015, addr, 0x00, index)

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

from enum import Enum


class PeripheralType(Enum):
    """Enum representing different types of peripherals that can be connected."""

    PLC_DIRECT = 0
    PLC_PCA9685 = 1
    PLC_MCP23008 = 2
    PLC_MCP23017 = 3
    PLC_LTC2309 = 4
    PLC_ADS1015 = 5


class PinType(Enum):
    """Enum representing the type of pin configuration."""

    INPUT = 0
    OUTPUT = 1


class DigitalLevel(Enum):
    """Enum representing the digital levels for pins."""

    LOW = 0
    HIGH = 1

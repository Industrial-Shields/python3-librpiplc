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

from .mapping import PLCMappingDict, make_pin_ads1015, make_pin_direct

extras = {
    "RE": make_pin_direct(17),
    "DE": make_pin_direct(27),
    "CS0": make_pin_direct(8),
    "CS1": make_pin_direct(7),
    "EXP1_AN": 0xFFFFFFFF,
    "EXP1_PWM": 0xFFFFFFFF,
    "EXP1_INT": 0xFFFFFFFF,
    "EXP1_RST": 0xFFFFFFFF,
    "I0_4_20": make_pin_ads1015(0x49, 0x01),
    "I1_4_20": make_pin_ads1015(0x49, 0x00),
    "I0": make_pin_ads1015(0x49, 0x02),
    "I1": make_pin_ads1015(0x49, 0x03),
    "I2": make_pin_direct(20),
    "I3": make_pin_direct(21),
    "I4": make_pin_direct(26),
    "O0": make_pin_direct(19),
    "O1": make_pin_direct(6),
    "O2": make_pin_direct(5),
    "O3": make_pin_direct(22),
    "O4": make_pin_direct(4),
    "Q0": make_pin_direct(19),
    "Q1": make_pin_direct(6),
    "Q2": make_pin_direct(5),
    "Q3": make_pin_direct(22),
    "Q4": make_pin_direct(4),
}

hw = {
    "TOUCHBERRY_PI": PLCMappingDict({**extras}),
}

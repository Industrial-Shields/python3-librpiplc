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

from .mapping import PLCMappingDict, make_pin_direct

extras = {
    "DE_RE": make_pin_direct(27),
    "EXP_RST": make_pin_direct(26),
    "EXP_CS": make_pin_direct(11),
    "EXP_AN": make_pin_direct(16),
    "EXP_PWM": make_pin_direct(20),
    "EXP_INT": make_pin_direct(21),
}

hw = {
    "GATEBERRY": PLCMappingDict({**extras}),
}

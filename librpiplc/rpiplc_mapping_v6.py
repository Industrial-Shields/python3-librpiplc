"""
Copyright (c) 2024 Industrial Shields. All rights reserved.

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

from .mapping import (
    PLCMappingDict,
    make_pin_direct,
    make_pin_ltc2309,
    make_pin_mcp23008,
    make_pin_pca9685,
)

analog0 = {
    "I0.0": make_pin_mcp23008(0x20, 0x04),
    "I0.1": make_pin_mcp23008(0x20, 0x02),
    "I0.2": make_pin_mcp23008(0x20, 0x03),
    "I0.3": make_pin_mcp23008(0x20, 0x00),
    "I0.4": make_pin_mcp23008(0x20, 0x01),
    "I0.5": make_pin_direct(13),
    "I0.6": make_pin_direct(12),
    "I0.7": make_pin_ltc2309(0x08, 0x06),
    "I0.8": make_pin_ltc2309(0x08, 0x00),
    "I0.9": make_pin_ltc2309(0x0A, 0x06),
    "I0.10": make_pin_ltc2309(0x08, 0x04),
    "I0.11": make_pin_ltc2309(0x0A, 0x04),
    "I0.12": make_pin_ltc2309(0x08, 0x02),
    "Q0.0": make_pin_pca9685(0x40, 0x0C),
    "Q0.1": make_pin_pca9685(0x40, 0x0B),
    "Q0.2": make_pin_pca9685(0x40, 0x0F),
    "Q0.3": make_pin_pca9685(0x40, 0x0E),
    "Q0.4": make_pin_pca9685(0x40, 0x06),
    "Q0.5": make_pin_pca9685(0x40, 0x07),
    "Q0.6": make_pin_pca9685(0x40, 0x02),
    "Q0.7": make_pin_pca9685(0x40, 0x00),
    "A0.5": make_pin_pca9685(0x40, 0x07),
    "A0.6": make_pin_pca9685(0x40, 0x02),
    "A0.7": make_pin_pca9685(0x40, 0x00),
}
analog1 = {
    "I1.0": make_pin_mcp23008(0x21, 0x00),
    "I1.1": make_pin_mcp23008(0x20, 0x06),
    "I1.2": make_pin_mcp23008(0x21, 0x01),
    "I1.3": make_pin_mcp23008(0x20, 0x05),
    "I1.4": make_pin_mcp23008(0x21, 0x02),
    "I1.5": make_pin_direct(27),
    "I1.6": make_pin_direct(5),
    "I1.7": make_pin_ltc2309(0x08, 0x07),
    "I1.8": make_pin_ltc2309(0x08, 0x05),
    "I1.9": make_pin_ltc2309(0x0A, 0x07),
    "I1.10": make_pin_ltc2309(0x0A, 0x01),
    "I1.11": make_pin_ltc2309(0x08, 0x03),
    "I1.12": make_pin_ltc2309(0x0A, 0x00),
    "Q1.0": make_pin_pca9685(0x40, 0x0A),
    "Q1.1": make_pin_pca9685(0x41, 0x01),
    "Q1.2": make_pin_pca9685(0x40, 0x09),
    "Q1.3": make_pin_pca9685(0x41, 0x00),
    "Q1.4": make_pin_pca9685(0x40, 0x0D),
    "Q1.5": make_pin_pca9685(0x40, 0x08),
    "Q1.6": make_pin_pca9685(0x40, 0x05),
    "Q1.7": make_pin_pca9685(0x40, 0x01),
    "A1.5": make_pin_pca9685(0x40, 0x08),
    "A1.6": make_pin_pca9685(0x40, 0x05),
    "A1.7": make_pin_pca9685(0x40, 0x01),
}
analog2 = {
    "I2.0": make_pin_mcp23008(0x21, 0x07),
    "I2.1": make_pin_mcp23008(0x21, 0x04),
    "I2.2": make_pin_mcp23008(0x21, 0x06),
    "I2.3": make_pin_mcp23008(0x21, 0x03),
    "I2.4": make_pin_mcp23008(0x21, 0x05),
    "I2.5": make_pin_direct(26),
    "I2.6": make_pin_direct(4),
    "I2.7": make_pin_ltc2309(0x08, 0x01),
    "I2.8": make_pin_ltc2309(0x0A, 0x03),
    "I2.9": make_pin_ltc2309(0x0A, 0x02),
    "I2.10": make_pin_ltc2309(0x28, 0x06),
    "I2.11": make_pin_ltc2309(0x0A, 0x05),
    "I2.12": make_pin_ltc2309(0x28, 0x07),
    "Q2.0": make_pin_pca9685(0x41, 0x07),
    "Q2.1": make_pin_pca9685(0x41, 0x06),
    "Q2.2": make_pin_pca9685(0x41, 0x03),
    "Q2.3": make_pin_pca9685(0x41, 0x05),
    "Q2.4": make_pin_pca9685(0x41, 0x02),
    "Q2.5": make_pin_pca9685(0x41, 0x04),
    "Q2.6": make_pin_pca9685(0x40, 0x04),
    "Q2.7": make_pin_pca9685(0x40, 0x03),
    "A2.5": make_pin_pca9685(0x41, 0x04),
    "A2.6": make_pin_pca9685(0x40, 0x04),
    "A2.7": make_pin_pca9685(0x40, 0x03),
}
relay0 = {
    "I0.0": make_pin_direct(13),
    "I0.1": make_pin_direct(12),
    "I0.2": make_pin_ltc2309(0x08, 0x06),
    "I0.3": make_pin_ltc2309(0x08, 0x00),
    "I0.4": make_pin_ltc2309(0x0A, 0x06),
    "I0.5": make_pin_ltc2309(0x08, 0x04),
    "Q0.0": make_pin_pca9685(0x40, 0x07),
    "Q0.1": make_pin_pca9685(0x40, 0x02),
    "Q0.2": make_pin_pca9685(0x40, 0x00),
    "A0.0": make_pin_pca9685(0x40, 0x07),
    "A0.1": make_pin_pca9685(0x40, 0x02),
    "A0.2": make_pin_pca9685(0x40, 0x00),
    "R0.1": make_pin_mcp23008(0x20, 0x02),
    "R0.2": make_pin_mcp23008(0x20, 0x04),
    "R0.3": make_pin_mcp23008(0x20, 0x00),
    "R0.4": make_pin_mcp23008(0x20, 0x03),
    "R0.5": make_pin_pca9685(0x40, 0x06),
    "R0.6": make_pin_pca9685(0x40, 0x0E),
    "R0.7": make_pin_pca9685(0x40, 0x0F),
    "R0.8": make_pin_pca9685(0x40, 0x0B),
}
relay1 = {
    "I1.0": make_pin_direct(27),
    "I1.1": make_pin_direct(5),
    "I1.2": make_pin_ltc2309(0x08, 0x07),
    "I1.3": make_pin_ltc2309(0x08, 0x05),
    "I1.4": make_pin_ltc2309(0x0A, 0x07),
    "I1.5": make_pin_ltc2309(0x0A, 0x01),
    "Q1.0": make_pin_pca9685(0x40, 0x08),
    "Q1.1": make_pin_pca9685(0x40, 0x05),
    "Q1.2": make_pin_pca9685(0x40, 0x01),
    "A1.0": make_pin_pca9685(0x40, 0x08),
    "A1.1": make_pin_pca9685(0x40, 0x05),
    "A1.2": make_pin_pca9685(0x40, 0x01),
    "R1.1": make_pin_mcp23008(0x20, 0x06),
    "R1.2": make_pin_mcp23008(0x21, 0x00),
    "R1.3": make_pin_mcp23008(0x20, 0x05),
    "R1.4": make_pin_mcp23008(0x21, 0x01),
    "R1.5": make_pin_pca9685(0x40, 0x0D),
    "R1.6": make_pin_pca9685(0x41, 0x00),
    "R1.7": make_pin_pca9685(0x40, 0x09),
    "R1.8": make_pin_pca9685(0x41, 0x01),
}
relay2 = {
    "I2.0": make_pin_direct(26),
    "I2.1": make_pin_direct(4),
    "I2.2": make_pin_ltc2309(0x08, 0x01),
    "I2.3": make_pin_ltc2309(0x0A, 0x03),
    "I2.4": make_pin_ltc2309(0x0A, 0x02),
    "I2.5": make_pin_ltc2309(0x28, 0x06),
    "Q2.0": make_pin_pca9685(0x41, 0x04),
    "Q2.1": make_pin_pca9685(0x40, 0x04),
    "Q2.2": make_pin_pca9685(0x40, 0x03),
    "A2.0": make_pin_pca9685(0x41, 0x04),
    "A2.1": make_pin_pca9685(0x40, 0x04),
    "A2.2": make_pin_pca9685(0x40, 0x03),
    "R2.1": make_pin_mcp23008(0x21, 0x04),
    "R2.2": make_pin_mcp23008(0x21, 0x07),
    "R2.3": make_pin_mcp23008(0x21, 0x03),
    "R2.4": make_pin_mcp23008(0x21, 0x06),
    "R2.5": make_pin_pca9685(0x41, 0x02),
    "R2.6": make_pin_pca9685(0x41, 0x05),
    "R2.7": make_pin_pca9685(0x41, 0x03),
    "R2.8": make_pin_pca9685(0x41, 0x06),
}

extras = {
    "EXP1_RST": make_pin_pca9685(0x41, 0x0C),
    "EXP2_RST": make_pin_pca9685(0x41, 0x0D),
    "PIN8": make_pin_direct(8),
    "P_RELAY": make_pin_direct(26),
    "OPTO_OUT_2": make_pin_direct(27),
    "OPTO_OUT_1": make_pin_direct(13),
    "OPTO_IN_2": make_pin_direct(5),
    "OPTO_IN_1": make_pin_direct(12),
    "INT31": make_pin_direct(4),
}

hw = {
    "RPIPLC_CPU": PLCMappingDict({**extras}),
    "RPIPLC_19R": PLCMappingDict({**relay0, **extras}),
    "RPIPLC_21": PLCMappingDict({**analog0, **extras}),
    "RPIPLC_38AR": PLCMappingDict({**analog0, **relay1, **extras}),
    "RPIPLC_38R": PLCMappingDict({**relay0, **relay1, **extras}),
    "RPIPLC_42": PLCMappingDict({**analog0, **analog1, **extras}),
    "RPIPLC_50RRA": PLCMappingDict({**relay0, **relay1, **analog2, **extras}),
    "RPIPLC_53ARR": PLCMappingDict({**analog0, **relay1, **relay2, **extras}),
    "RPIPLC_54ARA": PLCMappingDict({**analog0, **relay1, **analog2, **extras}),
    "RPIPLC_57AAR": PLCMappingDict({**analog0, **analog1, **relay2, **extras}),
    "RPIPLC_57R": PLCMappingDict({**relay0, **relay1, **relay2, **extras}),
    "RPIPLC_58": PLCMappingDict({**analog0, **analog1, **analog2, **extras}),
}

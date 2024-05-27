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

analog0 = {
	"I0.0": 0x00002105,
	"I0.1": 0x00002102,
	"I0.2": 0x00002104,
	"I0.3": 0x00002101,
	"I0.4": 0x00002103,
	"I0.5": 13,
	"I0.6": 12,
	"I0.7": 0x00000806,
	"I0.8": 0x00000805,
	"I0.9": 0x00000807,
	"I0.10": 0x00000A00,
	"I0.11": 0x00000A06,
	"I0.12": 0x00000A03,

	"Q0.0": 0x0000410C,
	"Q0.1": 0x00004000,
	"Q0.2": 0x0000410F,
	"Q0.3": 0x0000410E,
	"Q0.4": 0x00004105,
	"Q0.5": 0x00004104,
	"Q0.6": 0x00004102,
	"Q0.7": 0x00004100,

	"A0.5": 0x00004104,
	"A0.6": 0x00004102,
	"A0.7": 0x00004100,
}
analog1 = {
	"I1.0": 0x00002004,
	"I1.1": 0x00002000,
	"I1.2": 0x00002001,
	"I1.3": 0x00002106,
	"I1.4": 0x00002107,
	"I1.5": 27,
	"I1.6": 5,
	"I1.7": 0x00002807,
	"I1.8": 0x00000800,
	"I1.9": 0x00002800,
	"I1.10": 0x00000A02,
	"I1.11": 0x00000804,
	"I1.12": 0x00000A04,

	"Q1.0": 0x00004003,
	"Q1.1": 0x00004006,
	"Q1.2": 0x00004002,
	"Q1.3": 0x00004005,
	"Q1.4": 0x0000410D,
	"Q1.5": 0x00004001,
	"Q1.6": 0x00004103,
	"Q1.7": 0x00004101,

	"A1.5": 0x00004001,
	"A1.6": 0x00004103,
	"A1.7": 0x00004101,
}
analog2 = {
	"I2.0": 0x00002007,
	"I2.1": 0x00002003,
	"I2.2": 0x00002006,
	"I2.3": 0x00002002,
	"I2.4": 0x00002005,
	"I2.5": 26,
	"I2.6": 4,
	"I2.7": 0x00000803,
	"I2.8": 0x00002803,
	"I2.9": 0x00000802,
	"I2.10": 0x00000801,
	"I2.11": 0x00002806,
	"I2.12": 0x00000A01,

	"Q2.0": 0x0000400E,
	"Q2.1": 0x0000400C,
	"Q2.2": 0x0000400F,
	"Q2.3": 0x0000400D,
	"Q2.4": 0x00004007,
	"Q2.5": 0x00004004,
	"Q2.6": 0x00004107,
	"Q2.7": 0x00004106,

	"A2.5": 0x00004004,
	"A2.6": 0x00004107,
	"A2.7": 0x00004106,
}
relay0 = {
	"I0.0": 13,
	"I0.1": 12,
	"I0.2": 0x00000806,
	"I0.3": 0x00000805,
	"I0.4": 0x00000807,
	"I0.5": 0x00000A00,

	"Q0.0": 0x00004104,
	"Q0.1": 0x00004102,
	"Q0.2": 0x00004100,

	"A0.0": 0x00004104,
	"A0.1": 0x00004102,
	"A0.2": 0x00004100,

	"R0.1": 0x00002102,
	"R0.2": 0x00002105,
	"R0.3": 0x00002101,
	"R0.4": 0x00002104,
	"R0.5": 0x00004105,
	"R0.6": 0x0000410E,
	"R0.7": 0x0000410F,
	"R0.8": 0x00004000,
}
relay1 = {
	"I1.0": 27,
	"I1.1": 5,
	"I1.2": 0x00002807,
	"I1.3": 0x00000800,
	"I1.4": 0x00002800,
	"I1.5": 0x00000A02,

	"Q1.0": 0x00004001,
	"Q1.1": 0x00004103,
	"Q1.2": 0x00004101,

	"A1.0": 0x00004001,
	"A1.1": 0x00004103,
	"A1.2": 0x00004101,

	"R1.1": 0x00002000,
	"R1.2": 0x00002004,
	"R1.3": 0x00002106,
	"R1.4": 0x00002001,
	"R1.5": 0x0000410D,
	"R1.6": 0x00004005,
	"R1.7": 0x00004002,
	"R1.8": 0x00004006,
}
relay2 = {
	"I2.0": 26,
	"I2.1": 4,
	"I2.2": 0x00000803,
	"I2.3": 0x00002803,
	"I2.4": 0x00000802,
	"I2.5": 0x00000801,

	"Q2.0": 0x00004004,
	"Q2.1": 0x00004107,
	"Q2.2": 0x00004106,

	"A2.0": 0x00004004,
	"A2.1": 0x00004107,
	"A2.2": 0x00004106,

	"R2.1": 0x00002003,
	"R2.2": 0x00002007,
	"R2.3": 0x00002002,
	"R2.4": 0x00002006,
	"R2.5": 0x00004007,
	"R2.6": 0x0000400D,
	"R2.7": 0x0000400F,
	"R2.8": 0x0000400C,
}

extras = {
	"PIN8": 8,
	"PWM3": 0x00004109,
	"PWM2": 0x0000410A,
	"PWM1": 0x0000410B,
	"EXP1_RST": 0x00004008,
	"EXP2_RST": 0x0000400A,
}

hw = {
	"RPIPLC": {**extras},
	"RPIPLC_19R": {**relay0, **extras},
        "RPIPLC_21": {**analog0, **extras},
        "RPIPLC_38AR": {**analog0, **relay1, **extras},
        "RPIPLC_38R": {**relay0, **relay1, **extras},
        "RPIPLC_42": {**analog0, **analog1, **extras},
        "RPIPLC_50RRA": {**relay0, **relay1, **analog2, **extras},
        "RPIPLC_53ARR": {**analog0, **relay1, **relay2, **extras},
        "RPIPLC_54ARA": {**analog0, **relay1, **analog2, **extras},
        "RPIPLC_57AAR": {**analog0, **analog1, **relay2, **extras},
        "RPIPLC_57R": {**relay0, **relay1, **relay2, **extras},
        "RPIPLC_58": {**analog0, **analog1, **analog2, **extras},
}

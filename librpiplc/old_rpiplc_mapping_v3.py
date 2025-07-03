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

from .mapping import PLCMappingDict

analog0 = {
    "I0.0": 0x00002105,
    "I0.1": 0x00002103,
    "I0.2": 0x00002102,
    "I0.3": 0x00002101,
    "I0.4": 0x00002100,
    "I0.5": 13,
    "I0.6": 12,
    "I0.7": 0x00004A00,
    "I0.8": 0x00004A01,
    "I0.9": 0x00004B00,
    "I0.10": 0x00004802,
    "I0.11": 0x00004800,
    "I0.12": 0x00004801,
    "Q0.0": 0x0000400F,
    "Q0.1": 0x0000400E,
    "Q0.2": 0x0000400D,
    "Q0.3": 0x0000400C,
    "Q0.4": 0x0000400B,
    "Q0.5": 0x0000400A,
    "Q0.6": 0x00004001,
    "Q0.7": 0x00004000,
    "A0.5": 0x0000400A,
    "A0.6": 0x00004001,
    "A0.7": 0x00004000,
}
analog1 = {
    "I1.0": 0x00002002,
    "I1.1": 0x00002001,
    "I1.2": 0x00002000,
    "I1.3": 0x00002107,
    "I1.4": 0x00002106,
    "I1.5": 27,
    "I1.6": 4,
    "I1.7": 0x00004900,
    "I1.8": 0x00004A03,
    "I1.9": 0x00004B02,
    "I1.10": 0x00004B03,
    "I1.11": 0x00004A02,
    "I1.12": 0x00004901,
    "Q1.0": 0x00004002,
    "Q1.1": 0x00004009,
    "Q1.2": 0x00004006,
    "Q1.3": 0x00004004,
    "Q1.4": 0x00004007,
    "Q1.5": 0x00004003,
    "Q1.6": 0x00004005,
    "Q1.7": 0x00004008,
    "A1.5": 0x00004003,
    "A1.6": 0x00004005,
    "A1.7": 0x00004008,
}
analog2 = {
    "I2.0": 0x00002006,
    "I2.1": 0x00002005,
    "I2.2": 0x00002007,
    "I2.3": 0x00002004,
    "I2.4": 0x00002003,
    "I2.5": 17,
    "I2.6": 16,
    "I2.7": 0x00004903,
    "I2.8": 0x00004902,
    "I2.9": 0x00004803,
    "I2.10": 0x00004B01,
    "Q2.0": 0x00004106,
    "Q2.1": 0x00004107,
    "Q2.2": 0x00004105,
    "Q2.3": 0x00004104,
    "Q2.4": 0x00004103,
    "Q2.5": 0x00004102,
    "Q2.6": 0x00004101,
    "Q2.7": 0x00004100,
    "A2.5": 0x00004102,
    "A2.6": 0x00004101,
    "A2.7": 0x00004100,
}
relay0 = {
    "I0.0": 13,
    "I0.1": 12,
    "I0.2": 0x00004A00,
    "I0.3": 0x00004A01,
    "I0.4": 0x00004B00,
    "I0.5": 0x00004802,
    "Q0.0": 0x0000400A,
    "Q0.1": 0x00004001,
    "Q0.2": 0x00004000,
    "A0.0": 0x0000400A,
    "A0.1": 0x00004001,
    "A0.2": 0x00004000,
    "R0.1": 0x00002103,
    "R0.2": 0x00002105,
    "R0.3": 0x00002101,
    "R0.4": 0x00002102,
    "R0.5": 0x0000400B,
    "R0.6": 0x0000400C,
    "R0.7": 0x0000400D,
    "R0.8": 0x0000400E,
}
relay1 = {
    "I1.0": 27,
    "I1.1": 4,
    "I1.2": 0x00004900,
    "I1.3": 0x00004A03,
    "I1.4": 0x00004B02,
    "I1.5": 0x00004B03,
    "Q1.0": 0x00004003,
    "Q1.1": 0x00004005,
    "Q1.2": 0x00004008,
    "A1.0": 0x00004003,
    "A1.1": 0x00004005,
    "A1.2": 0x00004008,
    "R1.1": 0x00002001,
    "R1.2": 0x00002002,
    "R1.3": 0x00002107,
    "R1.4": 0x00002000,
    "R1.5": 0x00004007,
    "R1.6": 0x00004004,
    "R1.7": 0x00004006,
    "R1.8": 0x00004009,
}
relay2 = {
    "I2.0": 17,
    "I2.1": 16,
    "I2.2": 0x00004903,
    "I2.3": 0x00004902,
    "I2.4": 0x00004803,
    "I2.5": 0x00004B01,
    "Q2.0": 0x00004102,
    "Q2.1": 0x00004101,
    "Q2.2": 0x00004100,
    "A2.0": 0x00004102,
    "A2.1": 0x00004101,
    "A2.2": 0x00004100,
    "R2.1": 0x00002005,
    "R2.2": 0x00002006,
    "R2.3": 0x00002004,
    "R2.4": 0x00002007,
    "R2.5": 0x00004103,
    "R2.6": 0x00004104,
    "R2.7": 0x00004105,
    "R2.8": 0x00004107,
}

hw = {
    "RPIPLC_CPU": PLCMappingDict({}),
    "RPIPLC_19R": PLCMappingDict({**relay0}),
    "RPIPLC_21": PLCMappingDict({**analog0}),
    "RPIPLC_38AR": PLCMappingDict({**analog0, **relay1}),
    "RPIPLC_38R": PLCMappingDict({**relay0, **relay1}),
    "RPIPLC_42": PLCMappingDict({**analog0, **analog1}),
    "RPIPLC_50RRA": PLCMappingDict({**relay0, **relay1, **analog2}),
    "RPIPLC_53ARR": PLCMappingDict({**analog0, **relay1, **relay2}),
    "RPIPLC_54ARA": PLCMappingDict({**analog0, **relay1, **analog2}),
    "RPIPLC_57AAR": PLCMappingDict({**analog0, **analog1, **relay2}),
    "RPIPLC_57R": PLCMappingDict({**relay0, **relay1, **relay2}),
    "RPIPLC_58": PLCMappingDict({**analog0, **analog1, **analog2}),
}

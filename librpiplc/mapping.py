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

from .exceptions import UnknownPinError
from .lib_types import PeripheralType


class PLCMappingDict(dict[str, int]):
    """
    A dictionary that maps pin names to their corresponding integer values.

    This class extends the built-in dictionary to provide custom behavior
    for retrieving pin values.
    """

    def __getitem__(self, key: str) -> int:
        """
        Retrieve the integer value associated with the given pin name.

        Args:
            key (str): The name of the pin to retrieve.

        Returns:
            int: The integer value associated with the pin name.

        Raises:
            UnknownPin: If the pin name does not exist in the dictionary.

        """
        try:
            return int(super().__getitem__(key))
        except KeyError:
            pass
        raise UnknownPinError(key)


def _make_pin_plc(peripheral_type: PeripheralType, byte2: int, byte3: int, byte4: int) -> int:
    """
    Construct a pin identifier for a peripheral according to the librpiplc specifications.

    Args:
        peripheral_type (PeripheralType): The type of peripheral (e.g., PLC_DIRECT, PLC_PCA9685).
        byte2 (int): The second byte of the pin identifier.
        byte3 (int): The third byte of the pin identifier.
        byte4 (int): The fourth byte of the pin identifier.

    Returns:
        int: The constructed pin identifier.

    """
    return (
        ((peripheral_type.value & 0xFF) << 24)
        | ((byte2 & 0xFF) << 16)
        | ((byte3 & 0xFF) << 8)
        | (byte4 & 0xFF)
    )


def make_pin_direct(index: int) -> int:
    """
    Create a pin identifier for a direct GPIO (also known as normal GPIO).

    Args:
        index (int): The index of the pin.

    Returns:
        int: The constructed pin identifier for the direct PLC GPIO.

    """
    return _make_pin_plc(
        PeripheralType.PLC_DIRECT, (index & 0xFF0000) >> 16, (index & 0xFF00) >> 8, index
    )


def make_pin_pca9685(addr: int, index: int) -> int:
    """
    Create a pin identifier for a PCA9685.

    Args:
        addr (int): The address of the PCA9685.
        index (int): The index of the pin.

    Returns:
        int: The constructed pin identifier for the PCA9685.

    """
    return _make_pin_plc(PeripheralType.PLC_PCA9685, addr, 0x00, index)


def make_pin_mcp23008(addr: int, index: int) -> int:
    """
    Create a pin identifier for an MCP23008.

    Args:
        addr (int): The address of the MCP23008.
        index (int): The index of the pin.

    Returns:
        int: The constructed pin identifier for the MCP23008.

    """
    return _make_pin_plc(PeripheralType.PLC_MCP23008, addr, 0x00, index)


def make_pin_mcp23017(addr: int, index: int) -> int:
    """
    Create a pin identifier for an MCP23017.

    Args:
        addr (int): The address of the MCP23017.
        index (int): The index of the pin.

    Returns:
        int: The constructed pin identifier for the MCP23017.

    """
    return _make_pin_plc(PeripheralType.PLC_MCP23017, addr, 0x00, index)


def make_pin_ltc2309(addr: int, index: int) -> int:
    """
    Create a pin identifier for an LTC2309.

    Args:
        addr (int): The address of the LTC2309.
        index (int): The index of the pin.

    Returns:
        int: The constructed pin identifier for the LTC2309.

    """
    return _make_pin_plc(PeripheralType.PLC_LTC2309, addr, 0x00, index)


def make_pin_ads1015(addr: int, index: int) -> int:
    """
    Create a pin identifier for an ADS1015.

    Args:
        addr (int): The address of the ADS1015.
        index (int): The index of the pin.

    Returns:
        int: The constructed pin identifier for the ADS1015.

    """
    return _make_pin_plc(PeripheralType.PLC_ADS1015, addr, 0x00, index)

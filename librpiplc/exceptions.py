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


class UnknownPLCConfError(Exception):
    """Exception raised for invalid PLC configuration parameters."""

    def __init__(self, message: str) -> None:
        """Init method."""
        super().__init__(message)


UnknownPLCConf = UnknownPLCConfError  # Alias for backwards compatibility


class UnknownPinError(KeyError):
    """Exception raised for unknown pins in a dictionary."""

    def __init__(self, key: str) -> None:
        """Init method."""
        super().__init__(f"Unknown pin: '{key}'")

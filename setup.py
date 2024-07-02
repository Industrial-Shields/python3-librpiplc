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

from setuptools import find_packages, setup

# Helper symlink to make sure not to import the library installed in the system
from _setup_librpiplc import rpiplc



setup(
        name = "python3-librpiplc",
        version = rpiplc.python_version,
        packages = find_packages(include = ["librpiplc", "librpiplc.folder_rpiplc", "librpiplc.upsafepi"]),
        description = "Industrial Shields librpiplc bindings for Python 3",
        author = "Industrial Shields",
        license = "LGPL-3.0-or-later",
        classifier = ["License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)"]
        )

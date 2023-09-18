from setuptools import find_packages, setup

setup(
        name = "rpiplc_lib",
        version = '2.0.0',
        packages = find_packages(include = ["rpiplc_lib"]),
        description = "Industrial Shields RPIPLC library for python3",
        author = "Industrial Shields",
        license = "LGPL-v3"
        )

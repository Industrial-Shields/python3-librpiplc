from setuptools import find_packages, setup

setup(
        name = "librpiplc",
        version = '2.0.0',
        packages = find_packages(include = ["src"]),
        description = "Industrial Shields librpiplc bindings for Python 3",
        author = "Industrial Shields",
        license = "LGPL-v3"
        )

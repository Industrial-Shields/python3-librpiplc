# python3-librpiplc
### by Industrial Shields

**python3-librpiplc** provides a Python wrapper for the librpiplc C library, enabling Python applications to interface with the GPIOs of Raspberry Pi based Industrial Shields PLCs:
* Analog reads and write
* Digital reads and writes
* Relay controlling


## Licensing
This library is licensed under the LGPL-3.0-or-later. The test programs are licensed under the GPL-3.0-or-later.


## Prerequisites

### One of our PLCs: https://www.industrialshields.com/


### Installing librpiplc

You must first install the [librpiplc](https://github.com/Industrial-Shields/librpiplc), as this library depends on it.


### Installing git and pip

1. Start by updating the package manager:
```
sudo apt update
```

2. Run the following command to install pip:
```
sudo apt install git python3-pip
```

3. Verify the installation by typing the following commands, which will print the versions of each package:
```
pip --version
```



## Installing

1. Go to the directory where you want the library repository to be. For example, in your *home*:
```
cd
```

2. Run the following command to clone the repository:
```
git clone -b <tagname> https://github.com/Industrial-Shields/python3-librpiplc
```
Where `<tagname>` is the version you wish to download. Before this unification, you had to choose between versions 1.X.X (for V3 PLCs) or 2.X.X (for V4 PLCs). As of 3.X.X this library is compatible with our PLCs regardless of it's version.
You can check the available versions in here: https://github.com/Industrial-Shields/python3-librpiplc/tags

3. Go to the library directory and install the library with the following command:
```
cd python3-librpiplc/
# If you have Raspberry Bookwoorm or superior:
sudo python -m pip install . --break-system-packages --root-user-action=ignore
# Else
sudo python -m pip install .
```


## API
To start using the library, you need to import it with the following statement:
``` python
from librpiplc import rpiplc
```

And to set it up, you must call `rpiplc.init("VERSION_NAME", "MODEL_NAME")`, where VERSION_NAME and MODEL_NAME are the [available PLC versions](#available-versions) and [available PLC models](#available-models) respectively. This function must be called once every time you start your program.

Finally, it is a good practice to initialize the pins you want to use as INPUTS or OUTPUTS. You can do so with the `rpiplc.pin_mode(pin_name, mode)` function. For example, if you want to read from the **I0.2** input:
``` python
rpiplc.pin_mode("I0.2", rpiplc.INPUT)
```

The functions to read and write are the following:
``` python
digital_read(): rpiplc.digital_read(PIN_NAME) # It returns either rpiplc.HIGH (enabled) or rpiplc.LOW (disabled)

digital_write(): rpiplc.digital_write(PIN_NAME, VALUE) # Where value is either rpiplc.HIGH (enabled) or rpiplc.LOW (disabled)
# It can be used to control both digital outputs and relays.

analog_read(): rpiplc.analog_read(PIN_NAME) # It returns a 12-bit number that goes from 0 to 4095 (0 to 10V)

analog_write(): rpiplc.analog_write(PIN_NAME, VALUE) # Where value is a 12-bit number that goes from 0 to 4095 (0 to 10V)

delay(): rpiplc.delay(MS) # Where MS is the number of milliseconds to block the execution before continuing

delay_microseconds(): rpiplc.delay_microseconds(US) # Where US is the number of microseconds to block the execution before continuing
```



## Examples
``` python
"""
Copyright (c) 2024 Industrial Shields. All rights reserved

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from librpiplc import rpiplc

def digital_read_write():
	rpiplc.pin_mode("Q0.0", rpiplc.OUTPUT)
	rpiplc.digital_write("Q0.0", rpiplc.HIGH)
	rpiplc.delay(1000)

	rpiplc.pin_mode("I0.0", rpiplc.INPUT)
	read_value=rpiplc.digital_read("I0.0")
	print("The I0.0 is reading: {}".format(read_value))

	rpiplc.digital_write("Q0.0", rpiplc.LOW)
	rpiplc.delay(1000)

def analog_read_write():
	rpiplc.pin_mode("A0.0", rpiplc.OUTPUT)

	rpiplc.analog_write("A0.0", 1024) # 2.5v Output
	rpiplc.delay(2000)
	rpiplc.pin_mode("I0.2", rpiplc.INPUT)
	read_value=rpiplc.analog_read("I0.2") # 0 - 2047
	print("The I0.2 is reading: {}".format(read_value))

	rpiplc.analog_write("A0.0", 4095) # 10v Output
	rpiplc.delay(2000)
	rpiplc.pin_mode("I0.2", rpiplc.INPUT)
	read_value=rpiplc.analog_read("I0.2") # 0 - 2047
	print("The I0.2 is reading: {}".format(read_value))

	rpiplc.analog_write("A0.0", 0)

def analog_write_pwm():
	rpiplc.pin_mode("Q0.1", rpiplc.OUTPUT)
	rpiplc.analog_write_set_frequency("Q0.1", 24)
	rpiplc.analog_write("Q0.1", 2000)

def relay_test():
	rpiplc.pin_mode("R0.1",rpiplc.OUTPUT)
	rpiplc.digital_write("R0.1",rpiplc.HIGH)
	rpiplc.delay(1000)
	rpiplc.digital_write("R0.1",rpiplc.LOW)
        rpiplc.delay_microseconds(1000000)


def main():
	print(f"librpiplc version: {rpiplc.c_version}, python3-librpiplc version: {rpiplc.python_version}")

	rpiplc.init("RPIPLC_V4", "RPIPLC_57R")

	analog_write_pwm()

	try:
		while True:
			digital_read_write()
			analog_read_write()
			relay_test()
	except KeyboardInterrupt:
                return 0;


if __name__ == "__main__":
    main()
```



## References

1. [Available PLC versions](#available-versions)
1. [Available PLC models](#available-models)



### <a name="available-versions"></a>Available PLC versions
```
RPIPLC_V3 (deprecated)
RPIPLC_V4
RPIPLC_V6
```


### <a name="available-models"></a>Available PLC models
```
RPIPLC_19R
RPIPLC_21
RPIPLC_38AR
RPIPLC_38R
RPIPLC_42
RPIPLC_50RRA
RPIPLC_53ARR
RPIPLC_54ARA
RPIPLC_57AAR
RPIPLC_57R
RPIPLC_58
```

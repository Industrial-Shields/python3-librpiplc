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


## Installing

**WARNING: Installing this library from APT will remove the older library files, and all compiled
programs that depend on the library must be recompiled, including the ones that come with our image
(like `hw-config`). All of our programs can be installed later as an APT package (`sudo apt install
hw-config`).**

1. Check that you have configured the Industrial Shields Debian repository:
``` bash
apt-cache policy | grep industrialshields
```
* If no URL appears, install the repository with the following commands:
``` bash
# Set the debian repository URL as apt source
printf "\n\ndeb https://apps.industrialshields.com/main/DebRepo/ ./" | sudo tee -a /etc/apt/sources.list > /dev/null
# Download and install the GPG key
wget -O - https://apps.industrialshields.com/main/DebRepo/PublicKey.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/IndustrialShieldsDebian.gpg > /dev/null
# Update repositories
sudo apt update
```
After running the `sudo apt update` command, the repository should appear in the output.

2. Install the C and Python libraries through APT:
``` bash
sudo apt install librpiplc python3-librpiplc
```


## Building the library from source

### Extra pre-requisites: Installing Git and pip

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

### Build steps

1. Go to the directory where you want the library repository to be. For example, in your *home*:
```
cd
```

2. Run the following command to clone the repository:
```
git clone -b v<tag-version> https://github.com/Industrial-Shields/python3-librpiplc
```
Where `<tag-version>` is the version number you wish to download. Before this unification, you had
to choose between versions 1.X.X (for V3 PLCs) or 2.X.X (for V4 PLCs). As of 3.X.X, this library is
compatible with all our Raspberry PLCs regardless of it's version. At the moment of writing, this
library is available to Raspberry PLCs V6, V4 and V3. You can check the available versions in here:
https://github.com/Industrial-Shields/python3-librpiplc/tags

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

And to set it up, you must call `rpiplc.init("VERSION_NAME", "MODEL_NAME", restart=)`, where VERSION_NAME and
MODEL_NAME are the [available PLC versions](#available-versions) and
[available PLC models](#available-models) respectively. This function must be called once every time
you start your program.

Finally, it is a good practice to initialize the pins you want to use as INPUTS or OUTPUTS. You can
do so with the `rpiplc.pin_mode(pin_name, mode)` function. For example, if you want to read from the
**I0.2** input:
``` python
rpiplc.pin_mode("I0.2", rpiplc.INPUT)
```

The functions to read and write are the following:
``` python
init(): rpiplc.init(VERSION_NAME, MODEL_NAME, restart=False)
# Returns 0 if the library was initialized successfully, or 1 if it was already initialized; otherwise, an error occurred.

with_init(): rpiplc.with_init(VERSION_NAME, MODEL_NAME, restart=False, restart_when_closing=True)
# It's the same as init(), but it can be used in the "with" statement.

deinit(): rpiplc.deinit(restart=True)
# Returns 0 if the library deinitialized successfully, or 2 if it was already deinitialized; otherwise, an error ocurred.
# If restart is True, all the PLC peripherals will be restarted to it's original state.
# Note: restart = False is not supported with older versions of librpiplc (<4.X.X). If you try to call it with an incompatible version,
# an exception will be raised.

digital_read(): rpiplc.digital_read(PIN_NAME)
# It returns either rpiplc.HIGH (enabled) or rpiplc.LOW (disabled)

digital_write(): rpiplc.digital_write(PIN_NAME, VALUE)
# Where value is either rpiplc.HIGH (enabled) or rpiplc.LOW (disabled)
# It can be used to control both digital outputs and relays.

analog_read(): rpiplc.analog_read(PIN_NAME)
# Returns the analog value read from PIN_NAME. However, the maximum reading value will depend on
# the PLC being used. For instance, the analog inputs of all Raspberry PLCs, from V3 to V6, operate
# up to 12 bits (i.e., 0 to 4095), and TouchBerry Pi analog inputs up to 11 bits (i.e., 0 to 2047).

analog_write(): rpiplc.analog_write(PIN_NAME, VALUE)
# Writes an analog value to PIN_NAME. However, the maximum value must be adjusted depending on the
# PLC being used. For instance, the analog outputs of all Raspberry PLCs, from V3 to V6, operate up
# to 12 bits (i.e., 0 to 4095).

delay(): rpiplc.delay(MS)
# Where MS is the number of milliseconds to block the execution before continuing

delay_microseconds(): rpiplc.delay_microseconds(US)
# Where US is the number of microseconds to block the execution before continuing
```



## Examples
``` python
import sys
from librpiplc import rpiplc

def main() -> int:
    print(f"librpiplc version: {rpiplc.c_version}, python3-librpiplc version: {rpiplc.python_version}")

    rc = rpiplc.init("RPIPLC_V6", "RPIPLC_21", restart=True)
    print(f"librpiplc init code: {rc}")
    if rc not in (0, 1):
        print("librpiplc could not be initialized")
        return -1

    try:
        while True:
            rpiplc.digital_write("Q0.0", rpiplc.HIGH);
            rpiplc.delay(500)
            rpiplc.digital_write("Q0.0", rpiplc.LOW);
            rpiplc.delay(500)
    except KeyboardInterrupt:
        pass

    print(f"librpiplc deinit code: {rpiplc.deinit(restart=True)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

```



## References

1. [Available PLC versions](#available-versions)
1. [Available PLC models](#available-models)



### <a name="available-versions"></a>Available PLC versions
```
RPIPLC_V3 (deprecated)
RPIPLC_V4
RPIPLC_V6

UPSAFEPI_V6

GATEBERRY_V9

TOUCHBERRY_PI_V1
```


### <a name="available-models"></a>Available PLC models
```
RPIPLC_CPU
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

UPSAFEPI (for UPSafePis)

GATEBERRY (for GateBerries)

TOUCHBERRY_PI (for TouchBerry Pis)
```

# Python Library for Industrial Shields Raspberry PLCs

## Summary
This library is developed for Industrial shields Raspberry PLCs and is only supported by Python3.
It performs the following functions:
* Analog Read
* Analog write
* Digital Read
* Digital write
* Relay 

## Installation
To install this library, You need to first clone this repository to your PLC using the following command:

$`git clone -b <tagname> https://github.com/Industrial-Shields/rpiplc-python3-lib` 
```
tagname = v1.X.X = RPI PLC Version 3

tagname = v2.X.X = RPI PLC Version 4

You can find the available tags here: https://github.com/Industrial-Shields/rpiplc-python3-lib/tags
```
After which, run the following command to install the library:

$`python3 setup.py install`

### Once installed, make sure to comment the following lines from config.txt file:

You can find the file here:

 _/boot/config.txt_
 
> Reboot the PLC once done.

```
#dtoverlay=mcp23017,noints,mcp23008,addr=0x20
#dtoverlay=mcp23017,noints,mcp23008,addr=0x21
#dtoverlay=i2c-pwm-pca9685a,addr=0x40
#dtoverlay=i2c-pwm-pca9685a,addr=0x41
#dtoverlay=ads1015,addr=0x48
#dtparam=cha_enable=true,cha_gain=1
#dtparam=chb_enable=true,chb_gain=1
#dtparam=chc_enable=true,chc_gain=1
#dtparam=chd_enable=true,chd_gain=
#dtoverlay=ads1015,addr=0x49
#dtparam=cha_enable=true,cha_gain=1
#dtparam=chb_enable=true,chb_gain=1
#dtparam=chc_enable=true,chc_gain=1
#dtparam=chd_enable=true,chd_gain=1
#dtoverlay=ads1015,addr=0x4a
#dtparam=cha_enable=true,cha_gain=1
#dtparam=chb_enable=true,chb_gain=1
#dtparam=chc_enable=true,chc_gain=1
#dtparam=chd_enable=true,chd_gain=1
#dtoverlay=ads1015,addr=0x4b
#dtparam=cha_enable=true,cha_gain=1
#dtparam=chb_enable=true,chb_gain=1
#dtparam=chc_enable=true,chc_gain=1
#dtparam=chd_enable=true,chd_gain=1
```

## API
PLC initialization

`rpiplc.init("RPIPLC_57R")`

You can choose from the below model list to fill the parameter.
PLC Model list:
- RPIPLC_19R 
- RPIPLC_21
- RPIPLC_38AR 
- RPIPLC_38R
- RPIPLC_42
- RPIPLC_50RRA
- RPIPLC_53ARR
- RPIPLC_54ARA
- RPIPLC_57AAR 
- RPIPLC_57R 
- RPIPLC_58 

Pin initialization:
It is a good practice to initialize the pins as inputs or outpust, for this use the following code:

`pin_mode(pin_name, mode)`  _# mode can be rpiplc.OUTPUT ;rpiplc.INPUT or 1 ; 0_

Pin Functions:
_analog_read()_

`rpiplc.analog_read("I0.2")`

_analog_write()_

`rpiplc.analog_write("A0.0",value)` _# Here the value is in the range of 0 to 4095. 0 being 0V and 4095 is 10v_

_digital_read()_

`rpiplc.digital_read("I0.0")`

_digital_write()_

`rpiplc.digital_write("Q0.0",rpiplc.HIGH)`

_relay()_

`rpiplc.digital_write("R0.1",rpiplc.HIGH)`


## Examples

```
from rpiplc_lib import rpiplc

def digital_read_write():
    rpiplc.pin_mode("I0.0",rpiplc.INPUT)
    read_value=rpiplc.digital_read("I0.0")
    print("The I0.0 is reading: {}".format(read_value))
 
    rpiplc.pin_mode("Q0.0",rpiplc.OUTPUT)
    rpiplc.digital_write("Q0.0",rpiplc.HIGH)
    rpiplc.delay(1000)
    rpiplc.digital_write("Q0.0",rpiplc.LOW)
    rpiplc.delay(1000)
    
    
def analog_read_write():
    rpiplc.pin_mode("I0.2",rpiplc.INPUT)
    read_value=rpiplc.analog_read("I0.2") # 0 - 2047
    print("The I0.2 is reading: {}".format(read_value))

    rpiplc.pin_mode("A0.0",rpiplc.OUTPUT)  	
    rpiplc.analog_write("A0.0",1024) # 2.5v Output
    rpiplc.delay(2000)
    rpiplc.analog_write("A0.0",4095) # 10v Output
    rpiplc.delay(2000)
    rpiplc.analog_write("A0.0",0)


def relay_test():
    rpiplc.pin_mode("R0.1",rpiplc.OUTPUT)
    rpiplc.digital_write("R0.1",rpiplc.HIGH)
    rpiplc.delay(1000)
    rpiplc.digital_write("R0.1",rpiplc.LOW)
    rpiplc.delay(1000)
    
    
def main():
    rpiplc.init("RPIPLC_57R")

    while True:
        digital_read_write()
        analog_read_write()
        relay_test()


if __name__ == "__main__":
    main()
```

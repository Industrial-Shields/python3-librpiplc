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

    rpiplc.init("RPIPLC_V6", "RPIPLC_57R")

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

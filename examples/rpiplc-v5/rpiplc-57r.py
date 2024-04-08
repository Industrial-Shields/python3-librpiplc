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
	rpiplc.init("RPIPLC_V5", "RPIPLC_57R")

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

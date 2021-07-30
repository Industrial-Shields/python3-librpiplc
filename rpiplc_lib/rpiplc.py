from ctypes import cdll
from . models import hw

_rpiplc = cdll.LoadLibrary("librpiplc.so")
_hw = None

INPUT = 0
OUTPUT = 1

LOW = 0
HIGH = 1

def init(model_name):
    global _hw

    _rpiplc.initPins()
    _hw = hw[model_name]

def analog_read(pin_name):
    return _rpiplc.analogRead(_hw[pin_name])

def analog_write(pin_name, value):
    _rpiplc.analogWrite(_hw[pin_name], value)

def delay(value):
    _rpiplc.delay(value)

def digital_read(pin_name):
    return _rpiplc.digitalRead(_hw[pin_name])

def digital_write(pin_name, value):
    _rpiplc.digitalWrite(_hw[pin_name], value)

def pin_mode(pin_name, mode):
    _rpiplc.pinMode(_hw[pin_name], mode)

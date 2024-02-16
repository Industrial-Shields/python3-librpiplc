from ctypes import cdll

_rpiplc = cdll.LoadLibrary("librpiplc.so")
_hw = None

INPUT = 0
OUTPUT = 1

LOW = 0
HIGH = 1

class UnknownPLCConf(Exception):
     def __init__(self, message):
        super().__init__(message)

def init(version_name, model_name):
    global _hw

    _rpiplc.initPins()

    if version_name == "RPIPLC_V4":
        from . models_v4 import hw
    elif version_name == "RPIPLC_V3":
        from . models_v3 import hw
    else:
        raise UnknownPLCConf(f"Unknown version {version_name}, the only available versions are RPIPLC_V4 and RPIPLC_V3")

    available_models = hw.keys()
    if model_name not in available_models:
        pretty_available_models = "\n" + '\n'.join(available_models)
        raise UnknownPLCConf(f"Unknown model {model_name}, the only available models for {version_name} are:{pretty_available_models}")

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

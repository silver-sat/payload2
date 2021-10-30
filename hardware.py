
class RPIHardware:
    
    def __init__(self):
        pass
        
    def setup_gpio_pins(self):
        pass
    
    def gpio_pin_is_high(self,pin_number):
        pass
    
    def gpio_pin_is_low(self,pin_number):
        pass
    
    # gpio_pins_are_low(PIN1,PIN2,PIN3)
    def gpio_pins_are_low(self,*pins):
        pass
    
    def gpio_pins_are_high(self,*pins):
        pass
    
    def setup_camera(self):
        pass
    
    def take_photo(self,filename):
        pass
    
class SimulatedRPIHardware(RPIHardware):
    _filename = "~/.rpihardware.ini"
    def __init__(self):
        # look for the config file
        _poweron = time.time()
        _config = ...
        
    def gpio_pin_is_high(self,pin_number):
        

try:
    import GPIO
except ImportError:
    pass

class ActualRPIHardware(RPIHardware):
    
    def gpio_pin_is_high(self,pin_number)
        return GPIO.input(pin_number) == GPIO.HIGH
    
    def gpio_pin_is_low(self,pin_number)
        return GPIO.input(pin_number) == GPIO.LOW

_rpihardware = None

def get_hardware():
    if not _rpihardware:
        if os.path.exists(SimulatedRPIHardware._filename):
            _rpihardware = SimulatedRPIHardware()
        else:
            _rpihardware = ActualRPIHardware()
    return _rpihardware    

        
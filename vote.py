import RPi.GPIO as GPIO

IPIN1 = 16
IPIN2 = 20
IPIN3 = 21
OPIN1 = 17
OPIN2 = 27
OPIN3 = 22
PINS = [PIN1, PIN2, PIN3]
OPINS = [OPIN1, OPIN2, OPIN3]


def pinsetup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    for pin in PINS:
        GPIO.setup(pin, GPIO.IN)

    for pin in OPINS:
        GPIO.setup(pin, GPIO.OUT)
        
        

def opins(*PINS):
    for pin in PINS:
        GPIO.output(pin, GPIO.HIGH)

        
        
def triplevoting(*PINS):
    count = 0
    for pin in PINS:
        if GPIO.input(pin) == GPIO.HIGH:
            count += 1

    if count >= 2:
        return GPIO.HIGH

    return GPIO.LOW

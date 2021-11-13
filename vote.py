import RPi.GPIO as GPIO

IPIN1 = 16
IPIN2 = 20
IPIN3 = 21
OPIN1 = 17
OPIN2 = 27
OPIN3 = 22
IPINS = [IPIN1, IPIN2, IPIN3]
OPINS = [OPIN1, OPIN2, OPIN3]


def pinsetup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    for pin in IPINS:
        GPIO.setup(pin, GPIO.IN)

    for pin in OPINS:
        GPIO.setup(pin, GPIO.OUT)
        
        

def opins(*OPINS):
    for pin in OPINS:
        GPIO.output(pin, GPIO.HIGH)

        
        
def triplevoting(*IPINS):
    count = 0
    for pin in IPINS:
        if GPIO.input(pin) == GPIO.HIGH:
            count += 1

    if count >= 2:
        return GPIO.HIGH

    return GPIO.LOW

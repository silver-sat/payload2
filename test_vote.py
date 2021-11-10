import RPi.GPIO as GPIO

from vote import pinsetup, opins, triplevoting

from vote import OPIN1, OPIN2, OPIN3, IPIN1, IPIN2, IPIN3

pinsetup()

#setting output pins to high
opins(OPIN1, OPIN2, OPIN3)


print(triplevoting(IPIN1, IPIN2, IPIN3))


if triplevoting(IPIN1, IPIN2, IPIN3) == GPIO.HIGH:
    print("take photo")

else:
    print("tweet")

import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def decToBin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    period = float(input("ВВедите значение: "))

    while True:
        value = 0

        while(value < 255):
            GPIO.output(dac, decToBin(value))
            time.sleep(period/512)
            value += 1
        while(value > 0):
            GPIO.output(dac, decToBin(value))
            time.sleep(period/512)
            value -= 1
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
import RPi.GPIO as GPIO
import time


leds = [21, 20, 16, 12, 7, 8, 25, 24]

ed = [1,1,1,1,1,1,1,1]

aux = [22, 23, 27, 18, 15,14,3,2]

GPIO.setmode(GPIO.BCM)


GPIO.cleanup()

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

GPIO.output(leds, ed)



while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))
    time.sleep(0.1)
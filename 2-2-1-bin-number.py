import RPi.GPIO as GPIO
import time

array = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)


GPIO.setup(array, GPIO.OUT)

GPIO.output(array, 0)

GPIO.cleanup()
# while True:
#     for i in array:
#         GPIO.output(i, 1)
#         time.sleep(1)
#         GPIO.output(i, 0)





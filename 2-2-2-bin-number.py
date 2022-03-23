import RPi.GPIO as GPIO
import time
import random

dac = [26, 19, 13, 6, 5, 11, 9, 10]
num = [0 ,  0,  0, 0, 0 , 0, 0, 0]

GPIO.setmode(GPIO.BCM)

# for i in num:
#     i = random.randint(0, 1)

inNum = 2
i = 7
while inNum != 0:
    num[7 - i] = inNum // 2**i

    inNum %= 2**i
    i -= 1
print(num)

    

# print(bin(inNum))
    

GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, num)

time.sleep(20)
GPIO.output(dac, 0)
GPIO.cleanup()
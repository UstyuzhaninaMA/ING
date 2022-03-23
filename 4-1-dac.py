import RPi.GPIO as GPIO

def demicalToBinary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def expectedValue(number):
    return 3.3 * number / 256 



dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)



try:
    while True:
        inpStr = input("Введите число от 0 до 255:")


        if(inpStr == 'q'):
           break
        if(inpStr.isdigit() == 0):
            print("Неверный ввод(отрицательное число или не число)")
            continue
        try:
            int(inpStr)
        except ValueError:
            print("Введено не целое число")
            continue
        number = int(inpStr)
        # if(number < 0): 
        #     print("Введено отрицательное число")
        #     continue
        if(number > 255): 
            print("Введено неверное число")
            continue


        GPIO.output(dac, demicalToBinary(number))

        print("Предполагаемое значение напряжения: ", expectedValue(number)) 

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
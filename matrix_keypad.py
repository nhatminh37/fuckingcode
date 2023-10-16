import RPi.GPIO as GPIO
import time
L1= 5
L2= 6
L3= 13
L4= 19

C1= 12
C2= 16
C3= 20
C4= 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) ==1):
        GPIO.output(3, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(3, GPIO.LOW)
    if(GPIO.input(C2) ==1):
        GPIO.output(2,GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(2,GPIO.HIGH)
    GPIO.output(line, GPIO.LOW)
try:
    while True:
        readLine(L1)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")





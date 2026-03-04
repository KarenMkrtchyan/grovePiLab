import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 1
grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    dis = grovepi.ultrasonicRead(ultrasonic_ranger) # orignial ragne: 0 - 500
    # TODO: read threshold from potentiometer
    pot = grovepi.analogRead(potentiometer)/2 # orignial range 0 - 1023, divide by 2 to map 
    # TODO: format LCD text according to threshhold
    if pot < dis:
      setText(str(pot) + "cm\n" + str(dis))
      setRGB(0,255,0)
    else:
      setText(str(pot) + "cm OBJ PRES\n" + str(dis))
      setRGB(255,0,0)

    time.sleep(0.2)


  
  except IOError:
    print("Error")
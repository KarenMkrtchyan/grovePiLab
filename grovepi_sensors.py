import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 1
led = 4
ledS = 0
need_ref = 1
grovepi.pinMode(led, "OUTPUT")
grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

# clear lcd screen  before starting main loop
setText("")
top_line = ""

while True:
  try:
    dis = grovepi.ultrasonicRead(ultrasonic_ranger) # orignial ragne: 0 - 500
    pot = grovepi.analogRead(potentiometer) # orignial range 0 - 1023, divide by 2 to map 
    if pot < dis:
      top_line = (str(pot) + "cm").ljust(16)
      setRGB(0,255,0)
    else:
      top_line = (str(pot) + "cm OBJ PRES").ljust(16)
      setRGB(255,0,0)

    bottom_line = (str(dis) + "cm").ljust(16)
    setText_norefresh(top_line + "\n" + bottom_line)
    # grovepi.digitalWrite(led, ledS)
    # time.sleep(0.5)

  except IOError:
    print("Error")
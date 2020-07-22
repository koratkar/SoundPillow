
import time
import os
import board
import digitalio 
import busio
import adafruit_lis3dh




hurtSound = ["hurt1.mp3", "hurt2.mp3", "hurt3.mp3"]


def checkAceleration():
    x = "x"
    y = "y"
    z = "z"
    xyz = [x, y, z]
    print('acceleration: (%s)' % xyz)
    os.system('omxplayer hurt1.mp3')


while True:
    time.sleep(0.2)
    checkAceleration()
import time
import board
import digitalio 
import busio
import adafruit_lis3dh
# Hardware I2C setup. Use the CircuitPlayground built-in accelerometer if available; # otherwise check I2C pins.
if hasattr(board, "ACCELEROMETER_SCL"):
    i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA) 
    int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT) 
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
else:
    i2c = busio.I2C(board.SCL, board.SDA)
    int1 = digitalio.DigitalInOut(board.D6) 
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

x, y, z = [
value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration ]
print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
# Small delay to keep things responsive but give time for interrupt processing. time.sleep(0.1)
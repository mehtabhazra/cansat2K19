import board
import digitalio
import busio
import time
import adafruit_bmp280 

import Adafruit_ADXL345


# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()

i2c=busio.I2C(board.SCL,board.SDA)
bmp280=adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

bmp280.seaLevelhPa=1013.25
while True:
    print("\nTemperature:%0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude =%0.f meters" % bmp280.altitude)
                    #print('Printing X, Y, Z axis values')
                        
                            #time.sleep(1)
                                # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()
    print("\n printing adxl345 values of X,Y,Z")
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
                                                                    # Wait half a second and repeat.
                                                                                            
    time.sleep(1)

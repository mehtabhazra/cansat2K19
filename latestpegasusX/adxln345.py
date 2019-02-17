import time
import Adafruit_ADXL345
import board
import digitalio
import busio
import time
import adafruit_bmp280

accel = Adafruit_ADXL345.ADXL345()
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.seaLevelhPa = 1013.25


print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
while True:
        # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()
    print('\n X={0}, Y={1}, Z={2}'.format(x, y, z))
                    # Wait half a second and repeat.
    
    time.sleep(0.2)
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(0.2)


    #time.sleep(0.5)

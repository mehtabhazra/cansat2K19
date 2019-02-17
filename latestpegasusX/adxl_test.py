import time
import board
import busio
import adxl345
import adxl345


i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

accel = adafruit_adxl345.ADXL345()

#axes=adxl345.getAxes(True)



while True:
    print("%f %f %f"%accelerometer.acceleration)
    x, y, z = accel.read()
    #print(axes['x'])
    
    time.sleep(1)

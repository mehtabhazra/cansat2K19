import serial
#For Serial Communication
import time
#For Delay Function
ser = serial.Serial('/dev/ttyAMA0')
#Set ser as Object
ser.baudrate = 9600

#Set Baud Rate to 9600
ser.write("A")
#Send Character A
time.sleep(1)
#Give 1 Second Delay
ser.close()
#Close Communication


import time
import serial
import string
import pynmea2
import smtplib
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText

#setting up mail information
fromaddr = ""
pword = ""
toaddr = ""
#msg = MIMEMultipart()
#msg['From'] = fromaddr
#msg['To'] = toaddr
#msg['Subject'] = " Location change alert"


#setup the serial port to which gps is connected 
port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
dataout  = pynmea2.NMEAStreamReader()


    
while True:
    newdata = ser.readline()
    print ("getting new lat")
#    if newdata[0:6] == '$GPGGA':
    newmsg = pynmea2.parse(newdata)
    newlat = newmsg.latitude
    print(newlat)
    newlong = newmsg.longitude
    print(newlong)
    lat  = str(newlat)
    lon = str(newlong)

    print(lat,lon)
        
    time.sleep(3)
        
        

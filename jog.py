'''
JogWear for the OpenEyeTap
Created by Cayden Pierce, Feb. 2018.
'''


from time import sleep
import datetime as dt
from blue import GPSbluetooth #my Bluetooth GPS NMEA client, RFCOMM

def CurrentTime():
    return('%s')%(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def createLog(): #adds log of seeing person. Contains context such as who, what, where, when
        with open(os.path.join(os.path.dirname(__file__), "memory/joglog.csv"), "a", newline="") as log_csv: #open in append and read mode
            time = CurrentTime()
            coordinates = GPSbluetooth.getLocation(sock)
            if coordinates:
            	lat, long = coordinates
            else:
            	location = ("{}, {}".format(lat, long)
            
            speed = GPSbluetooth.getSpeed(sock)
            if !sock:
                speed = "NA"
            memory = [time, speed, location]

            wr = csv.writer(log_csv, delimiter = ',')
            wr.writerow(memory)

#start the bluetooth server for GPS
sock = GPSbluetooth.startBluetoothServer()
 
while True: #main 
	createLog() #create a new log with time, speed, and location data
	sleep(1)

#clean up when complete
sock.close()      



'''
Speedometer for the OpenEyeTap
Created by Cayden Pierce, Feb. 2018.
Humanistic Intelligence is the future we are all creating together.
'''


from time import sleep
import datetime as dt
from blue import GPSbluetooth #my Bluetooth GPS NMEA client, RFCOMM

def CurrentTime():
    return('%s')%(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def createLog(): #adds log of seeing person. Contains context such as who, what, where, when
        with open(os.path.join(os.path.dirname(__file__), "memory/locationlog.csv"), "a", newline="") as log_csv: #open in append and read mode
            time = CurrentTime()
            coordinates = GPSbluetooth.getLocation(sock)
            if coordinates:
            	lat, long = coordinates
            	location = getAddress(lat, long)
            else:
            	location = ("Latitude: {}, Longitude: {}".format(lat, long))
            memory = [time, location, "Null"]

            wr = csv.writer(log_csv, delimiter = ',')
            wr.writerow(memory)
            
while True: #main 
	#get current speed
	location = GPSbluetooth.getLocation(sock)
	createLog(location)
        
sock.close()      
camera.stop_preview()

'''
JogWear for the OpenEyeTap
Created by Cayden Pierce, Feb. 2018.
'''

import os
import sys
import csv
from time import sleep
import datetime as dt
from math import sin, cos, sqrt, atan2, radians
from blue import GPSbluetooth #my Bluetooth GPS NMEA client, RFCOMM

def CurrentTime():
    return('%s')%(dt.datetime.now().strftime('%m/%d/%Y_%H:%M:%S'))

def createJogFile(name):
        with open(os.path.join(os.path.dirname(__file__), "memory/{}.csv".format(name)), "a", newline="") as log_csv: #open in append and read mode
            initLine = ["time", "speed", "latitude", "longitude"]
            wr = csv.writer(log_csv, delimiter = ',')
            wr.writerow(initLine)

def createLog(name): #adds log of seeing person. Contains context such as who, what, where, when
        with open(os.path.join(os.path.dirname(__file__), "memory/{}.csv".format(name)), "a", newline="") as log_csv: #open in append and read mode
            time = CurrentTime()
            coordinates = GPSbluetooth.getLocation(sock)
            if coordinates:
            	latitude, longitude = coordinates
            else:
                latitude = "NA"
                longitude = "NA"

            #location = ("{}, {}".format(lat, long))

            speed = GPSbluetooth.getSpeed(sock)
            if speed is None:
                speed = "NA"
            memory = [time, speed, latitude, longitude]

            wr = csv.writer(log_csv, delimiter = ',')
            wr.writerow(memory)
'''
def distanceTwoPoints(point1, point2): #returns distance between two points, in meters
	# approximate radius of earth in km
	R = 6373.0

	lat1 = radians(point1[0])
	lon1 = radians(point1[1])
	lat2 = radians(point2[0])
	lon2 = radians(point2[1])

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c * 1000
	return distance

def totalDistance(name):
    with open(os.path.join(os.path.dirname(__file__), "memory/{}.csv".format(name)), "a", newline="") as joglog: #open in append and read mode
        reader = csv.reader(joglog, delimiter = ',')
	for row in reader[0:]:
		print(row)

'''

#start the bluetooth server for GPS
sock = GPSbluetooth.startBluetoothServer()

#get name of jog that was passed as an arg
name = sys.argv[1]

#create file to save coordinates
#createJogFile(name)

while True: #main 
	createLog(name) #create a new log with time, speed, and location data
	sleep(1)

#find total distance of jog, append it to end of log
#distance = jogReader(name)

#clean up when complete
sock.close()      



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

def distanceTwoPoints(point1, point2): #returns distance between two points, in kilometers
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

	distance = R * c
	return distance

def totalDistance(name):
	points = [] #list of points to find distances between
	totalDistance = 0 #totalDistance travelled

	with open(os.path.join(os.path.dirname(__file__), "memory/{}.csv".format(name)), "r") as joglog: #open in append and read mode
		reader = csv.reader(joglog, delimiter = ',')
		for i, row in enumerate(reader):
			if ((i % 30) - 1 == 0): #only check every thirty coordinates
				points.append([float(row[2]), float(row[3])]) #append coordinate point to points list
	for i, point in enumerate(points[:-1]):
		totalDistance += distanceTwoPoints(points[i], points[i+1])
	return totalDistance


#start the bluetooth server for GPS
sock = GPSbluetooth.startBluetoothServer()

#get name of jog that was passed as an arg
name = sys.argv[1]

#create file to save coordinates
createJogFile(name)

try:
	while True: #main 
		createLog(name) #create a new log with time, speed, and location data
		sleep(1)
		'''with open(os.path.join(os.path.dirname(__file__), "memory/{}.csv".format(name)), "a", newline="") as log_csv: #open in append and read mode
			wr = csv.writer(log_csv, delimiter = ',')
			wr.writerow(["hello", "NA", "NA", "NA"])'''

finally:
	#find total distance of jog, append it to end of log
	distance = totalDistance(name)
	with open(os.path.join(os.path.dirname(__file__), "memory/{}.csv".format(name)), "a", newline="") as joglog: #open in append and read mode
		joglog.write('\n')
		joglog.write("Total distance was: {} km \n".format(distance))

	#clean up when complete
	sock.close()   



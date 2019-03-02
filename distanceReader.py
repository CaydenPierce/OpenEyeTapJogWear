import csv
import sys
import os

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
	points = [] #list of points to find distances between
	with open(os.path.join(os.path.dirname(__file__), "memory/{}.csv".format(name)), "r") as joglog: #open in append and read mode
		reader = csv.reader(joglog, delimiter = ',')
		for i, row in enumerate(reader):
			if ((i % 30) - 1 == 0): #only check every thirty coordinates
				points.append(row[2]) #append coordinate point to points list
	print(points)
				

name = sys.argv[1]
totalDistance(name)

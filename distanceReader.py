import csv
import sys
import os
from math import sin, cos, sqrt, atan2, radians

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
				if (row[2] != "NA"):
					points.append([float(row[2]), float(row[3])]) #append coordinate point to points list
	for i, point in enumerate(points[:-1]):
		totalDistance += distanceTwoPoints(points[i], points[i+1])
	return totalDistance

name = sys.argv[1]
print(totalDistance(name))

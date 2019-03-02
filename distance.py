from math import sin, cos, sqrt, atan2, radians
import csv


def distance(point1, point2): #returns distance between two points, in meters
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

def jogReader(jog):
    with open(jog, 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        encoding = list(reader)
        encoding = np.array(encoding[0])
    encoding = encoding.astype(np.float)
    return encoding
	
point1 = [42.99485495, -81.26335386666666]
point2 = [42.99486845, -81.26338]

print(distance(point1, point2))

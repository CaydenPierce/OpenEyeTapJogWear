'''
Speedometer for the OpenEyeTap
Created by Cayden Pierce, Feb. 2018.
Humanistic Intelligence is the future we are all creating together.
'''


import picamera
from time import sleep
import datetime as dt
from blue import GPSbluetooth
        
#start the bluetooth server for GPS, save socket
sock = GPSbluetooth.startBluetoothServer()

#create the camera, set to low resolution for faster processing
camera = picamera.PiCamera()
camera.resolution = (320, 240)

#start camera view
camera.start_preview()

#counter for testing
counter = 0

while counter < 15:
#main program loop
	counter += 1
	print("loop {}".format(counter))
 
	#get current speed
	speed = GPSbluetooth.getSpeed(sock)
	camera.annotate_text = speed
        
sock.close()      
camera.stop_preview()

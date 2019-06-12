###################################################################################################################
# File: serialwriter.py
# Course: 17640
# Project: IoT Order Fulfillment Center
# Copyright: Copyright (c) 2018 Carnegie Mellon University (ajl)
# Versions:
#	1.0 April 2018 - Initial write (ajl).
#
# Description: This class serves as an example for how to write an application that can write serial data to
# an external device. The intent is for this to illustrate how to write data to an Arduino software serial
# port. This example could be used as a basis for writing an application to send command to fulfillment
# center robots.
#
# Parameters: Port or device file
#
# Internal Methods:
#  None
#
# External Dependencies:
#   - python 2.7
#	- time
#	- serial ## pyserial-3.2.1 library
###################################################################################################################

import sys
import time
import serial 
from flask import Flask, render_template, request


# Make sure the device/comm port was supplied on the command line. To get a list of valie devices please see
# serialports.py (lists the available ports).

if len(sys.argv) < 2:
    print('You need to supply the comm port/device on the command line.')
    print('python serialwriter <comm port or device path>')
    exit()
else:
	print('____________________________________________________________')		
	print('Writing to port ' + sys.argv[1])
	print('To stop, press control-C')
	print('____________________________________________________________')

# Here we define the serial port. This reflects the settings for the software serial port on the arduino.
# Please refer to the companion arduino code: SoftSerialRead.ino. Note that no errors are trapped here in the 
# name of brevity. If the comm port/device doesn't exist, it will crash here. For your production code you should
# probably add error handling here (try-catches).

ser = serial.Serial(
    port=sys.argv[1],
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

# Wait a couple of seconds for things to settle (typical in the embedded world ;-)

time.sleep(1)

# This is a pretty simple do-forever loop. We ask the user for some input and we write it out the specified
# port.

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/your_flask_funtion1')
def get_ses1():
	message='q+'
	b = str.encode(message)						# Puts the message into bytes
	ser.write(b)								# Writes the bytes to the specified port 
	ser.flush()									# We clear the port
	return render_template('index.html')
@app.route('/your_flask_funtion2')
def get_ses2():
	message='p+'
	b = str.encode(message)						# Puts the message into bytes
	ser.write(b)								# Writes the bytes to the specified port 
	ser.flush()									# We clear the port
	return render_template('index.html')
@app.route('/your_flask_funtion3')
def get_ses3():
	message='m+'
	b = str.encode(message)						# Puts the message into bytes
	ser.write(b)								# Writes the bytes to the specified port 
	ser.flush()									# We clear the port
	return render_template('index.html')
	


if __name__ == '__main__':
	app.run(debug=False)



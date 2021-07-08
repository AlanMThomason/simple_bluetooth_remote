"""
Robot controller over Bluetooth
"""

import time
import msvcrt
import serial #Note that if you don't have this, you must pip install PySerial, not serial
import sys


# This is intended to communicate via serial protocol over BlueTooth using an
#  HC-05.
#  Like this
#   https://www.amazon.com/dp/B01MQKX7VP?psc=1&ref=ppx_yo2_dt_b_product_details
#
# I was trying to control an Arduino equpped robot.
#
# To set this up, you must first power up the HC-05
# Pair your computer with this Bluetooth device.  The code for the one above was '1234'
#
# Mine showed ups as COM14.
#
# To find this port number must go to Device Manager / Ports
# There will be one or two ports named something similar to 
#  "Standard Serial over Bluetooth link (COMXX)"
#
# If you cannot open Device Manager by entering DeviceManager in the start bar, 
#  enter run in the windows start bar at the bottom left of the screen.
#  and enter
#   devmgmt.msc
#
# For different COM ports than the deafult just start this program with the
#  port as the argument.  For instance, 
#    python robot_comms.py 37
#  One frustrating note is that my windows application opens two ports for bluetooth
#    The first one causes the program to hang, not sure why.  So I have to set the
#     second one.
#
#
#  There is almost nothing here, but it will feel so cool to control your robot
#   with the keyboard.  The C program that I have in the Arduino listens for the 
#    up (forward)
#    dn (backward)
#    left 
#    right
#    space (stop)
#
#  The most likely challenge is that in the C program you need to calibrate what 'stopped' 
#  is.
#

import sys
try:
    comms_port = "COM" + sys.argv[1]
    print("Will use comms_port", comms_port)
except:
    comms_port = "COM14"
    print("Will use default comms_port", comms_port)


ser = serial.Serial(comms_port, 9600)  # open serial port


ser.timeout = 3 #set timeout for serial communications


#Now set up a loop which reads teh keyboard and sends each key 
# code (ASCII) to the serial comms
finished = False

while not finished:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()

        if key_stroke == b'Q' or key_stroke == b'q' :
            print("User requested break to sequence")
            key_stroke = b' '
            finished = True
            
        #Every time the keyboard is pressed, b'\xe0' is reported
        # with every key press.  Sending this over the serial stream
        #  causes a hesitation in control, probably since there is no 
        #  associated action but it is received by the arduino
        #  and the ardunio program could then miss the desired action
      
        if key_stroke != b'\xe0' :
            print("key pressed = ", key_stroke)
            ser.write(key_stroke)


    
    time.sleep(0.01)


ser.close()

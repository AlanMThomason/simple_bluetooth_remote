"""
Robot controller over Bluetooth
"""

import time
import msvcrt
import serial #Note that if you don't have this, you must pip install PySerial, not serial


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
# Mine showed ups as COM31.
#
#  Don't laugh!  There is almost nothing here, but it will feel so cool to control your robot
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

ser = serial.Serial('COM31', 9600)  # open serial port


ser.timeout = 3 #set timeout for serial communications



while True:

    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        ser.write(key_stroke)


    time.sleep(0.01)


ser.close()

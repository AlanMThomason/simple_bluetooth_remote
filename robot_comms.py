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

# To find this you must go to Device Manager / Ports
# There will be one or two ports named something similar to 
#  "Standard Serial over Bluetooth link (COMXX)"
# If you cannot open Device Manager by entering DeviceManager in the start bar, 
#  enter run in the windows start bar at the bottom left of the screen.
#  and enter
#   devmgmt.msc

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


print("Stepping Stone remote robot control.")
print("Before running this progThe light on the HC-05 bluetooth receiver on the robot should be blinking at ~4Hz")
print("  or 4 times per second")
print("Next step is to attempt to connect through internal bluetooth device")
print("If that is successful, the light sequence will change to 2fast flashes followed by ")
print("  a pause for a periodic frequency of about 0.5Hz, or 2 fast flashes every 2seconds")
print("")
print("If the robot is moving when turned on, you will need to adjust the neutral settins in ")
print(" the Arduino program")
print("Otherwise, hopefully the light is blinking twice fast then pausing every 2sec")


#Sets up the serial communications channel at 9600baud
ser = serial.Serial('COM14', 9600)  # open serial port
ser.timeout = 3 #set timeout for serial communications


#Now set up a loop which reads teh keyboard and sends each key 
# code (ASCII) to the serial comms
while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()

        if key_stroke == b'Q' or key_stroke == b'q' :
            print("User requested break to sequence")
            break
            
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

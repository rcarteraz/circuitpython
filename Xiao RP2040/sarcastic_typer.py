# This is a simple script for writing sarcastically. It will display a message stating "Normal Typing Mode Engaged" while a switch is in the off position. When the switch is flipped to on, it will change that message to "sArCaStIc TyPiNg MoDe EnGaGeD!" and then send the keycode for CAPS_Lock to the connected computer at an interval of .1 seconds. 

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
import board

# Initialize Keyboard
kbd = Keyboard(usb_hid.devices)

# Define Switch
switch = DigitalInOut(board.D10)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# When Switch Activated Press and Release CAPS_LOCK
while True:
    if switch.value:
        print('Normal Typing Mode Engaged')
       
    else:
        print("sArCaStIc TyPiNg MoDe EnGaGeD!")
        kbd.send(Keycode.CAPS_LOCK)
        time.sleep(0.1)
    time.sleep(0.1)

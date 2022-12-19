# This is a simple script for writing sarcastically. It will display a message stating "Normal Mode." while a switch is in the off position. When the switch is flipped to on position, it will change that message to "sArCaStIc MoDe!" and then send the keycode for CAPS_Lock to the connected computer at an interval of .1 seconds. 

import board
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
import displayio
import adafruit_displayio_ssd1306
import adafruit_display_text.label
import terminalio

displayio.release_displays()

# Initialize the display
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Create a text box
text_area = adafruit_display_text.label.Label(terminalio.FONT, text="Normal Mode.")
text_area2 = adafruit_display_text.label.Label(terminalio.FONT, text="sArCaStIc MoDe!")
# Set the x and y position of the text box
text_area.anchor_point = (0.5, 0.5)
text_area.anchored_position = (128 / 2, 32 / 2)
text_area2.anchor_point = (0.5, 0.5)
text_area2.anchored_position = (128 / 2, 32 / 2)
# Add the text box to the display
display.show(text_area)

# Initialize Keyboard
kbd = Keyboard(usb_hid.devices)

# Define Switch
switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if switch.value:
        display.show(text_area)
    else:
        display.show(text_area2)
        kbd.send(Keycode.CAPS_LOCK)
        time.sleep(0.1)
    time.sleep(0.1)

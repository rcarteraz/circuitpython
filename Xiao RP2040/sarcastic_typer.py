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
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Create a text box
text_area = adafruit_display_text.label.Label(terminalio.FONT, scale=2, text="Normal\n Mode.")
text_area2 = adafruit_display_text.label.Label(terminalio.FONT, scale=2, text="sArCaStIc\n  MoDe!")
# Set the x and y position of the text box
text_area.anchor_point = (0.5, 0.5)
text_area.anchored_position = (128 / 2, 64 / 2)
text_area2.anchor_point = (0.5, 0.5)
text_area2.anchored_position = (128 / 2, 64 / 2)

# Initialize Keyboard
kbd = Keyboard(usb_hid.devices)

# Define Switch
switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if switch.value:
        # Add the text box to the display
        display.show(text_area)
    else:
        # Add the text box to the display
        display.show(text_area2)
        kbd.send(Keycode.CAPS_LOCK)
        time.sleep(0.1)
    time.sleep(0.1)
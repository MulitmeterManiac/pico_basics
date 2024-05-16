import time, usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_de import KeyboardLayout
from time import sleep


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)


def end():
    keyboard.send(Keycode.WINDOWS, Keycode.R)
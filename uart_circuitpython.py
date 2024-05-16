import board
import digitalio
from time import sleep
import busio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_de import KeyboardLayout

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

while True:
    data = uart.read(32)  # read up to 32 bytes
    # print(data)  # this is a bytearray type

    if data is not None:
        # convert bytearray to string
        data_string = ''.join([chr(b) for b in data])
        print(data_string, end="")

        
        if "LED1" in data_string:
            keyboard.send(Keycode.WINDOWS, Keycode.R)
            sleep(2)
            layout.write("cmd")
            keyboard.send(Keycode.ENTER)
            sleep(2)
            layout.write("shutdown -s -t 0 ")
            keyboard.send(Keycode.ENTER)

        
        

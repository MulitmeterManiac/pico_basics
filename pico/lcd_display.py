# Bibliotheken laden
from time import sleep_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
# Bibliothek laden
import machine

# RTC initialisieren


# Initialisierung I2C
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)

# Initialisierung LCD über I2C
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Text in Zeilen
zeile_oben = 'Hello World';
zeile_unten = 'Hurra ich lebe'

lcd.clear()

while True:
    rtc = machine.RTC()
    t = rtc.datetime()
    lcd.move_to(2, 0)
    lcd.putstr(":")
    h = t[4]
    h = str(h)

    m = t[5]
    m = str(m)

    if len(m) == 1:
        m = "0" + m
    if len(h) == 1:
        h = "0" + h
    lcd.move_to(0, 0)
    lcd.putstr(h)

    lcd.move_to(3, 0)
    lcd.putstr(m)
    sleep_ms(1000)








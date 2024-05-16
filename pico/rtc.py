# Bibliothek laden
import machine

# RTC initialisieren
rtc = machine.RTC()

# Datum/Uhrzeit lesen und ausgeben
t = rtc.datetime()
print(t[4])
print(t[5])
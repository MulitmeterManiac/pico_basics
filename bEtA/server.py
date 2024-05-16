# Bibliotheken laden
import network
import machine
import socket
import rp2
import time
from time import sleep_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
import _thread

led = machine.Pin('LED', machine.Pin.OUT)

i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

wlanSSID = 'o2-WLAN89'
wlanPW = 'TZU7LZHK74Q4NAXR'
network.country('DE')

# HTML-Datei
html = """<!doctype html><html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="shortcut icon" href="data:">
<title>server_ctrl</title>
</head>
<body>
    <h1 align="center">webserver_test</h1>
    <form>
        <div>          
            <input id="example" type="text" name="text" size="1" maxlength="2"/>
            
            <input id="example2" type="text" name="text" size="1" maxlength="2" />
            
        </div>
        <div>
            <input type="submit" value="Send" />
        </div>    
    </form>
    </a>
        
        
    </body>
    </html>"""
wlan = network.WLAN(network.STA_IF)
# Funktion: WLAN-Verbindung
def wlanConnect():
    
    if not wlan.isconnected():
        print('WLAN-Verbindung herstellen')
        wlan.config(pm = 0xa11140)
        wlan.active(True)
        wlan.connect(wlanSSID, wlanPW)
        for i in range(10):
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            print('.')
            time.sleep(1)
    if wlan.isconnected():
        print('WLAN-Verbindung hergestellt')
        netConfig = wlan.ifconfig()
        print('IPv4-Adresse:', netConfig[0])
        print()
        return netConfig[0]
    else:
        print('Keine WLAN-Verbindung')
        print('WLAN-Status:', wlan.status())
        print()
        return ''
    
#thread2


# WLAN-Verbindung herstellen
ipv4 = wlanConnect()

clock = bytearray([0x00,0x0E,0x15,0x17,0x11,0x0E,0x00,0x00])
lcd.custom_char(1, clock)
lcd.move_to(0, 0)
lcd.putstr(chr(1))

clock2 = bytearray([0x00,0x0E,0x1F,0x11,0x1F,0x0E,0x00,0x00])
lcd.custom_char(2, clock2)
lcd.move_to(0, 1)
lcd.putstr(chr(2))

conn_yn = bytearray([ 0x00,0x00,0x07,0x08,0x13,0x14,0x15,0x00])
lcd.custom_char(0, conn_yn)
lcd.move_to(14, 0)
lcd.putstr(chr(0))


# HTTP-Server starten
if ipv4 != '':
    addr = socket.getaddrinfo(ipv4, 80)[0][-1]
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    server.listen(1)
    print (addr)
    print()

# mainloop
lcd.move_to(3, 0)
lcd.putstr(":")
lcd.move_to(3, 1)
lcd.putstr(":")

def time_update():
    rtc = machine.RTC()
    t = rtc.datetime()
    sleep_ms(500)
    
    h = t[4]
    h = str(h)
    
    m = t[5]
    m = str(m)
    
    lcd.move_to(1, 1)
    lcd.putstr(ch)
    
    lcd.move_to(4, 1)
    lcd.putstr(cm)
    
    if len(m) == 1:
        m = "0"+m
    if len(h) == 1:
        h = "0"+h
    lcd.move_to(1, 0)
    lcd.putstr(h)
    
    lcd.move_to(4, 0)
    lcd.putstr(m)
ch = "--"
cm = "--"

while True:
    if wlan.isconnected() == True:
        lcd.move_to(15, 0)
        lcd.putstr("y")
    else:
        lcd.move_to(15, 0)
        lcd.putstr("n")
    time_update()
    
    try:
        time_update()
        conn, addr = server.accept()
        request = conn.recv(1024)
        request = str(request)
        request = request.split()
        
        print(request[1])
        if len(request[1]) == 17:
            re1 = request[1][7:9]
            re2 = request[1][15:17]
            print(re1)
            print(re2)
            ch = re1
            cm = re2
        if request[1] == '/light/on':
            peint("on")
        elif request[1] == "/light/t":
            print("t")
        #response
        #//
        state_is = ''
        response = html.replace('TEXT', state_is)
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
        rtc = machine.RTC()
        t = rtc.datetime()
        print("3")
        
    except OSError as e:
        break
    except (KeyboardInterrupt):
        break
    except:
        pass
    

try: conn.close()
except NameError: pass
try: server.close()
except NameError: pass
print('Server beendet')


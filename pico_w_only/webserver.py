# Bibliotheken laden
import network
import machine
import socket
import rp2
import time

# Onboard-LED initialisieren
led = machine.Pin('LED', machine.Pin.OUT)

# WLAN-Konfiguration
wlanSSID = 'ssid'
wlanPW = 'password'
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


# Funktion: WLAN-Verbindung
def wlanConnect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('WLAN-Verbindung herstellen')
        wlan.config(pm=0xa11140)
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


# WLAN-Verbindung herstellen
ipv4 = wlanConnect()

# HTTP-Server starten
if ipv4 != '':
    addr = socket.getaddrinfo(ipv4, 80)[0][-1]
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    server.listen(1)
    print(addr)
    print()

# Auf eingehende Verbindungen hören
while True:
    try:
        conn, addr = server.accept()
        # print('HTTP-Request von Client', addr)
        request = conn.recv(1024)
        # print('Request:', request)
        request = str(request)
        request = request.split()
        # print('URL:', request[1])
        # URL auswerten
        print(request[1])
        # if request[1].len() == 26:
        re1 = request[1][15:17]
        re2 = request[1][23:25]
        print(re1)
        print(re2)
        if request[1] == '/light/on':
            print('LED einschalten')
            led.value(1)
        elif request[1] == '/light/off':
            print('LED ausschalten')
            led.value(0)
        elif request[1] == '/light/toggle':
            print('LED umschalten')
            led.toggle()
        elif request[1] == "/light/t":
            print("t")
        # LED-Status auswerten
        # print('LED-Status:', led.value())
        state_is = ''
        if led.value() == 1:
            state_is += '<p align="center"><b>LED ist AN</b> <a href="off"><button>AUS</button></a></p>'
        if led.value() == 0:
            state_is += '<p align="center"><b>LED ist AUS</b> <a href="on"><button>ANagsdf</button></a></p>'

        # HTTP-Response erzeugen und senden
        response = html.replace('TEXT', state_is)

        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
        # print('HTTP-Response gesendet')
        print()
    except OSError as e:
        break
    except (KeyboardInterrupt):
        break
    except:
        pass

try:
    conn.close()
except NameError:
    pass
try:
    server.close()
except NameError:
    pass
print('Server beendet')

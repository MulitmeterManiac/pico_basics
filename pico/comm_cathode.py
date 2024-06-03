import machine
from time import sleep
machine.Pin("LED", machine.Pin.OUT).off()

A = machine.Pin(15, machine.Pin.OUT)
B = machine.Pin(15, machine.Pin.OUT)
C = machine.Pin(15, machine.Pin.OUT)
D = machine.Pin(15, machine.Pin.OUT)
E = machine.Pin(15, machine.Pin.OUT)
F = machine.Pin(15, machine.Pin.OUT)
G = machine.Pin(15, machine.Pin.OUT)
DP = machine.Pin(15, machine.Pin.OUT)

class digits():
    
    #set Pins of the seven-digit-display
    def __init__(self, a, b, c, d, e, f, g, dp):
        global A, B, C, D, E, F, G, DP
        
        self.A = machine.Pin(a, machine.Pin.OUT)
        self.B = machine.Pin(b, machine.Pin.OUT)
        self.C = machine.Pin(c, machine.Pin.OUT)
        self.D = machine.Pin(d, machine.Pin.OUT)
        self.E = machine.Pin(e, machine.Pin.OUT)
        self.F = machine.Pin(f, machine.Pin.OUT)
        self.G = machine.Pin(g, machine.Pin.OUT)
        self.DP = machine.Pin(dp, machine.Pin.OUT)

        
    def reset(self):
        self.A.on()
        self.B.on()
        self.C.on()
        self.D.on()
        self.E.on()
        self.F.on()
        self.G.on()
        self.DP.on()
        
    def one(self):
        self.A.on()
        self.B.off()
        self.C.off()
        self.D.on()
        self.E.on()
        self.F.on()
        self.G.on()
        self.DP.on()
        
    def two(self):
        self.A.off()
        self.B.off()
        self.C.on()
        self.D.off()
        self.E.off()
        self.F.on()
        self.G.off()
        self.DP.on()
        
    def three(self):
        self.A.off()
        self.B.off()
        self.C.off()
        self.D.off()
        self.E.on()
        self.F.on()
        self.G.off()
        self.DP.on()
        
    def four(self):
        self.A.on()
        self.B.off()
        self.C.off()
        self.D.on()
        self.E.on()
        self.F.off()
        self.G.off()
        self.DP.on()
        
    def five(self):
        self.A.off()
        self.B.on()
        self.C.off()
        self.D.off()
        self.E.on()
        self.F.off()
        self.G.off()
        self.DP.on()
    def six(self):
        self.A.off()
        self.B.on()
        self.C.off()
        self.D.off()
        self.E.off()
        self.F.off()
        self.G.off()
        self.DP.on()
        
    def seven(self):
        self.A.off()
        self.B.off()
        self.C.off()
        self.D.on()
        self.E.on()
        self.F.on()
        self.G.on()
        self.DP.on()
        
    def eight(self):
        self.A.off()
        self.B.off()
        self.C.off()
        self.D.off()
        self.E.off()
        self.F.off()
        self.G.off()
        self.DP.on()
        
    def nine(self):
        self.A.off()
        self.B.off()
        self.C.off()
        self.D.off()
        self.E.on()
        self.F.off()
        self.G.off()
        self.DP.on()
        
    def dot(self):
        self.A.on()
        self.B.on()
        self.C.on()
        self.D.on()
        self.E.on()
        self.F.on()
        self.G.on()
        self.DP.off()
        
    def trigger_dot(self):
        self.DP.toggle()
        
    def demo(self):
        
        
        self.one()
        sleep(1)
        self.two()
        sleep(1)
        self.three()
        sleep(1)
        self.four()
        sleep(1)
        self.five()
        sleep(1)
        self.six()
        sleep(1)
        self.seven()
        sleep(1)
        self.eight()
        sleep(1)
        self.nine()
        sleep(1)
        self.dot()
        sleep(2)
        self.reset()
        
    def demo2(self):
        
        
        self.one()
        sleep(0.05)
        self.two()
        sleep(0.05)
        self.three()
        sleep(0.05)
        self.four()
        sleep(0.05)
        self.five()
        sleep(0.05)
        self.six()
        sleep(0.05)
        self.seven()
        sleep(0.05)
        self.eight()
        sleep(0.05)
        self.nine()
        sleep(0.05)
        
        self.reset()
        


        

    







    


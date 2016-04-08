# parent class
class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label
    
    # performGateLogic() will be implemented later for specific gate
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

# LogicGate : BinaryGate   
# Gate with 2 inputs
class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None
        
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A for gate " + self.getLabel() + "--->" ))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B for gate "+ self.getLabel() + "--->" ))
        else:
            return self.pinB.getFrom().getOutput()
    
    # source is connector object
    def setNextPin(self, source):
        if self.pinA==None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: No Empty Pins!")
            

# LogicGate : UnaryGate   
# Gate with 1 input
class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None
        
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin for gate " + self.getLabel() + "--->"))
        else:
            return self.pin.getFrom().getOutput()
    
    # source is a connector object
    def setNextPin(self, source):
        if self.pin==None:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty Pins!")
            

# LogicGate: BinaryGate: AndGate
class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

# LogicGate: BinaryGate: OrGate
class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1
        

# LogicGate: UnaryGate: NotGate
class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)
    
    def performGateLogic(self):
        a = self.getPin()
        if a==0:
            return 1
        else:
            return 0
        
        
# Connector: connect output to input
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate
    

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g2)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

circuitOutput = g4.getOutput()
print "Output of circuit --->", circuitOutput




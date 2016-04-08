# greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# sign
def sign(a):
    return ( (a>0) - (a<0) )

class Fraction:
    def __init__(self, top, bottom):
        if type(top) != int or type(bottom) != int:
            raise ValueError("Both numerator and denominator should be integer!")
        commonDiv = gcd(top, bottom)
        self.num = top//commonDiv
        self.den = bottom//commonDiv
        
        
    def __str__(self):
        return ("%d/%d" % (self.num, self.den))
    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
        
    def __add__(self, other):
        newNum = self.num*other.den + self.den*other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)
    
    def __sub__(self, other):
        newNum = self.num*other.den - self.den*other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)
    
    def __eq__(self, other):
        e1 = self.num * other.den
        e2 = self.den * other.num
        return e1==e2
    
    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.den * other.den
        return Fraction(top,bottom)
    
    def __div__(self, other):
        top = self.num * other.den
        bottom = self.den * other.num
        return Fraction(top,bottom)
    
    def __gt__(self, other):
        temp = self - other
        return sign(temp.den)==sign(temp.num)
    
    def __ge__(self, other):
        temp = self - other
        return(sign(temp.num)==0 or sign(temp.den)==sign(temp.num))
    
    def __lt__(self, other):
        temp = other - self
        return sign(temp.num)==sign(temp.den)

    
    def __le__(self, other):
        temp = other - self
        return( sign(temp.num)==0 or sign(temp.den)==sign(temp.num) )
    
    def __ne__(self, other):
        a = self.num*other.den
        b = self.den*other.num
        return a!=b
        
    def show(self):
        print self.__str__()
        


    
test = Fraction(3, -5)
print "test = Fraction(3, -5)"
print "type(test): ", type(test)
print "Print test: ", test
print "test.show(): ",
test.show()
print "type(test).__str__(test):", type(test).__str__(test)
print "Greatest common divisor gcd(36, 16):", gcd(36, 16)
print "Fraction(6, 10) + Fraction(1/3): ", Fraction(6, 10)+Fraction(1, 3)
print "Fraction(6, 10) == Fraction(3, 5): ", Fraction(6, 10)==Fraction(3, 5)
print "Fraction(1, 2) == Fraction(3, 5): ", Fraction(1, 2)==Fraction(3, 5)
print "Fraction(2, 4) * Fraction(3, 5): ", Fraction(2, 4)*Fraction(3, 5)
print "Fraction(2, 4) / Fraction(3, 5): ", Fraction(2, 4)/Fraction(3, 5)
x = Fraction(123, -321)
print "\nx = Fraction(123, -321) \nx.getNum():%d \ny.getDen():%d" % (x.getNum(), x.getDen())
x = Fraction(1, 2)
y = Fraction(1, 3)
print "x = Fraction(1, 2) \ny = Fraction(1, 3)"
print "x > y --->", x>y
print "x >= y --->", x>=y
print "x < y --->", x<y
print "x <= y --->", x<=y
print "x != y --->", x!=y

print "sign(2): %d \nsign(-10):%d" % (sign(2), sign(-10))

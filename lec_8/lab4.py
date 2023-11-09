from math import pi
from math import sqrt
class Shape:
    def __init_(self):
        pass
    def whoam(self):
        print("I am a shape")

class twoD(Shape):
    def __init__(self):
        pass
    def area(self):
        print(" I am a 2 D object")
class trheeD(Shape):
    def __init__(self):
        pass
    def area(self):
        print(" I am  a 3 D object")

class Square(twoD):
    def __init__(self,a):
        self.a = a
    def area(self):
        return self.a * self.a
class Trinagle(twoD):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a+self.b+self.c)/2
        return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
class Cube(trheeD):
    def __init__(self,a):
        self.a =a
    def volume(self):
        return self.a * self.a * self.a 
class Cone(trheeD):
    def __init__(self,r,h):
        self.r =r
        self.h = h
    def volume(self):
        result = (pi * self.r * self.r * self.h)/3                 
        return result

sp = Square(12)
sp.area()
print(twoD.area(sp))

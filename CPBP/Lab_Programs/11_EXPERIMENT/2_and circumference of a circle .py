# WAP that has a class Circle. Use a class variable to define the value of constant pi. Use this class variable to calculate area and circumference of a circle with specified radius.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.circum = 0
        self.pi = 3.14
    def calcArea(self):
        self.area = self.pi * self.radius * self.radius
    def calcCircum(self):
        self.circum = 2 * self.pi * self.radius
    def printDetails(self):
        print()
        print("Given radius: ", self.radius)
        print("Area of circle: ", self.area)
        print("Circumference of circle: ", self.circum)

c1 = Circle(7)
c1.calcArea()
c1.calcCircum()

c2 = Circle(10)
c2.calcArea()
c2.calcCircum()

c1.printDetails()
c2.printDetails()

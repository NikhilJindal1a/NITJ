# WAP that has a class Point. Define another class Location which has 2 objects - location and destination. 
# Also define a function in location that prints the reflection of destination on the x-axis.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_new = 0
        self.y_new = 0
    def display_point(self):
        print(f'X = {self.x}, Y = {self.y}')

class Location(Point):
    def reflection(self):
        self.y_new = self.y * -1
        self.x_new = self.x
        print(f'X_relected = {self.x_new}, Y_reflected = {self.y_new}')

location = Location(1, 2)
destination = Location(10, 20)

location.display_point()
destination.display_point()
destination.reflection()

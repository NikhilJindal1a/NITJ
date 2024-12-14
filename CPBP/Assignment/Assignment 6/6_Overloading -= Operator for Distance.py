# 6. Write a program to overload -= operator to subtract two Distance objects
class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __isub__(self, other):
        self.meters -= other.meters
        return self

    def display(self):
        print(f"Distance: {self.meters} meters")

# Example usage
d1 = Distance(100)
d2 = Distance(40)
d1 -= d2
d1.display()

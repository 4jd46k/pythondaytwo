class Rectangle:
    def __init__(self):
        self.width = float(input("Enter the width of the rectangle: "))
        self.height = float(input("Enter the height of the rectangle: "))

    def area(self):
        return self.width * self.height
rect = Rectangle()
print(rect.area())

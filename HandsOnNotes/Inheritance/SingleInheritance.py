# class Shape:
#     def __init__(self):
#         print("This is the class Shape")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print("Area of the circle is: ", 3.14 * self.radius**2)
#     def peri(self):
#         print("Perimeter of the circle is: ", 2*3.14*self.radius)
# p = Circle(5)
# p.area()
# p.peri()

class Shape:
    def __init__(self,num_sides):
        self.num_sides = num_sides
        self.side = 0
    def ask_input(self):
        self.side = int(input("Enter the side of the square: "))
    def display(self):
        print("The side of the square is ",self.side)

class Square(Shape):
    def __init__(self, num_sides):
        Shape.__init__(self,N)
    def area(self):
        print("Area of the square is: ", self.side**2)
    def peri(self):
        print("Perimeter of the circle is: ", 4*self.side)
n = int(input("Enter the number of sides of the shape(Square)"))
p = Square(n)
p.ask_input()
p.display()
p.area()
p.peri()
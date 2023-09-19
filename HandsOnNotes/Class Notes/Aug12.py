### Inheritance
class polygon: ###base/parent class
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        if self.n ==4:
            pass
        else:
            self.sides = [0 for i in range(no_of_sides)] ###list comprehension
        #list comprehension where all the list elements are initialised to
    def inputsides(self):
        if self.n ==4:
            self.sides = int(input("Enter the side of the square: "))
        else:
            self.sides = [float(input("Enter Side"+str(i+1)+":")) for i in range(self.n)]
    def dispsides(self):
        if self.n ==4:
            print("The side of the square is: ",self.sides)
        else:
            for i in range(self.n):
                print("side", i+1, "is:", self.sides[i])
###derive/child class
class triangle (polygon):
    def __init__(self):
        #self.n = no_of_sides
        polygon.__init__(self,3)
    def findperimeter(self):
        a,b,c = self.sides
        s=(a+b+c)/2
        print("The Perimeter:", s)
class square(polygon):
    def __init__(self):
        polygon.__init__(self,4)
    def findperimeter(self):
        a= self.sides
        s=(4*a)
        print("The Perimeter:", s)
t =triangle()
t.inputsides()
t.dispsides()
t.findperimeter()
s = square()
s.inputsides()
s.dispsides()
s.findperimeter()

#### Multiple inheritence
# class base1:
#     def __init__(self, a):
#         self.a =a
#     def read_a(self, x):
#         self.x =x
#         return self.x
# class base2:
#     def __init__(self, b):
#         self.b =b
#     def read_b(self, y):
#         self.y =y
#         return self.y
# class derived(base1, base2):
#     def __init__(self):
#         base1.__init__(self, 3)
#         base2.__init__(self, 4)
#     def sum_ab(self):
#         return self.x + self.y
# ###instantiation
# d = derived()
# # print(d.sum_ab())
# print(d.read_a(10))
# print(d.read_b(20))
# print(d.sum_ab())

###Hierarchical Inheritance
# class parent:
#     def func1(self, a):
#         print("This is my parent class")
#         self.a = a
#         return self.a
# class leftchild(parent):
#     def func2(self):
#         print("This is my left child class")
#         print("square of a number is:", self.a * self.a)
# class rightchild(parent):
#     def func3(self):
#         print("This is my right child class")
#         print("cube of a number is:", self.a * self.a * self.a)

# o1 = leftchild()
# o2 = rightchild()
# o1.func1(10)
# o1.func2()
# o2.func1(10)
# o2.func3()
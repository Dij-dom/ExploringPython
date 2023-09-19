# class A(object):
#     def __init__(self, something):
#         print("A init called")
#         self.something = something
#         print(self.something)

# class B(A):#inheritance All the properties of the class A is given to B.
#     def __init__(self):
#         # Calling init of parent class
#         A.__init__(self, "something from B")
#         print("B init called")
#         #### Instantiating: each object has it's own requirements
# obj = B()#only object for the child class is created as the properties of A is in B


# class Rectangle:

#     sname = "Rectangle Plots" ###class attribute: common for the class. 
#     def __init__(self, l,b, unitcost =1): ## unitcost is a default parameter
#         self.l = l
#         self.b = b
#         self.unitcost = unitcost
#     def get_area(self):
#         return self.l * self.b
#     def cal_cost(self):
#         area = self.get_area()
#         cost = area*self.unitcost
#         return cost
# r1 = Rectangle(160,120) ###object1
# r2 = Rectangle(160,120,1000) ###object2
# r1.sname= "R1 Plot" #changing the value of the class attribute
# r2.sname= "R2 Plot"
# print("\n====R1 Details=====")
# print("Area of the plot in sqmt is:", r1.get_area())
# print("cost of the plot is Rs.:",r1.cal_cost())
# print("The name of the my class w.r.t. object r1 is:", r1.sname)

# print("\n====R2 Details=====")
# print("Area of the plot in sqmt is:", r2.get_area())
# print("cost of the plot is Rs.:",r2.cal_cost())
# print("The name of the my class using classname is:", Rectangle.sname) #class attribute: accesing the attribute using class name
# print("The name of the my class w.r.t. object r2 is:", r2.sname) #object attribute: 
# print("\n====R1 and R2 Details=====")
# r1.unitcost=50
# r1 = Rectangle(160,120, r1.unitcost) ###object1
# print("Cost of the r1's plot is Rs.*:",r1.cal_cost())
# print("The name of the my classattribute w.r.t. object r1 is:", r1.sname)
# print("The name of the my classattribute w.r.t. object r2 is:", r2.sname)
# r2.unitcost=30
# r2 = Rectangle(160,120, r2.unitcost) ###object2
# print("cost of the r2's plot is Rs.*:",r2.cal_cost())
# print("The name of the my classattribute w.r.t. object r1 is:", r1.sname)
# print("The name of the my classattribute w.r.t. object r2 is:", r2.sname)
# print("\n====Correct way of accessing class attribute=====")
# Rectangle.sname= "My Plot" ###Correct way
# print("The name of the my classattribute w.r.t. object r1 is:", r1.sname)
# print("The name of the my classattribute w.r.t. object r2 is:", r2.sname)

class Guardian():
    def __init__(self,name,age):
        self.name = input("Enter the name of the Guardian: ")
        self.age = int(input("\nEnter the age of the guardian: "))
class Student():
    def __init__(self,name):
        self.name = input("\nEnter the name of the Student: \n")
        self.RegNum = int(input("\nEnter the student's register number: \n"))
class Teacher():
    def __init__(self,name,subject):
        self.name = input("\nEnter the name of the Teacher: \n")
        self.sub = input("\nEnter the subject: ")

g1 = Guardian()
s1 = Student()
t1 = Teacher()

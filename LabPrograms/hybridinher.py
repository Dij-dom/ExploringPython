class RegisterException(Exception): #exception raised if Lucky is not willing to register
    def __init__(self, message="Registration exception was raised"):
        self.message = message
        super().__init__(self.message)

class Grandfather:
    def gmoney(self,money):
        print("Lucky, Congragulations. You are about to recieve 5 million dollars from your Grandfather.")
        self.money = money

class Father(Grandfather):
    def fprop(self,fproperty):
        print("Lucky, you are receiving one Villa from your father.")
        self.fproperty = fproperty

class Mother(Grandfather):
    def mprop(self,mproperty):
        print("Finally you are recieving 10 acres of land from your Mother.")
        self.mproperty = mproperty

class Lucky(Father, Mother):
    def lprop(self):
        reply = input("Do you wish to register the properties now? (Y/N)")
        if reply =="Y":
            self.register()
        else:
            raise RegisterException("You must register to get the property.")
    def register(self):
        print(f"Lucky,the following properties are registered successfully.\n{self.money}\n{self.fproperty}\n{self.mproperty}.\n Enjoy your life wisely.")
# Creating an object of class D
obj = Lucky()
obj.gmoney(5000000000)  # Accessing method from class A
obj.fprop("1 Villa")  # Accessing method from class B
obj.mprop("10 acres")  # Accessing method from class C
obj.lprop()
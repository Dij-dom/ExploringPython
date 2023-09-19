# class CS:
#     ptype = "PG"

#     def __init__(self,pname,cstrength):
#         CS.pname = pname
#         self.cstrength = cstrength
# p1 = CS("MCA",60)
# p2 = CS("MSc",55)
# print("P1 is a {}".format(p1.__class__.ptype),"program")
# print("{} is having {} students".format(p1.pname, p1.cstrength))
# print("{} is having {} students".format(p2.pname, p2.cstrength))
# print(type(CS.pname)) #pnamw can be accessed using the class but we can't initialize a variable using the class takes the last value passed by the last object
# print(type(p1.cstrength))
# print((p1.__class__.ptype))

#ACCESS SPECIFIERS
#   1. Private
#   2. Protected
#   3. Public


class Computer:
    price = input("Input the price: ")
    def __init__(self):
        self.maxprice = self.price
        print("The Max Price is: ", self.maxprice)
        
    def sell(self):
        print("Selling Price: {}".format(self.maxprice))
    
    def setMaxPrice(self,price):
        self.maxprice = price
    class MyComputers(Computer):
        print("Entered the child class")
        c = MyComputers()
        c.sell()
        c.maxprice = 1200
        print("Trying to change the value of the private variable")
        c.sell()
        #using setter function
        c.setMaxPrice(1000)
        c.sell()

        if(c.price ==c.maxprice):
            print("No price change")
        elif(c.price>c.maxprice):
            print("THe hghest price is", c.price)
        else:
            print("The highest rice is ", c.__maxprice)
obj = Computer()

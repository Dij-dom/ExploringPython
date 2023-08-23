#To check whether the entry is valid or not
# val  = input("ENter the value")
# obj1 = MYError(val)
# obj1.__str__()
# try:
#     if not type(val) is str:
#         print("Valid Entry.")
#     else:
#         raise (MyError(-1*1))
# except MyError as error:
#     print('A new exception has occured, program terminated with a value:',error.value)
# finally:
#     print("Please try again")

# class MyError(Exception):
#     def __init__(self):
#         pass
#     def sums(self,x,y):
#         self.x = x
#         self.y = y
#         try:
#             result = self.x + self.y
#         except(TypeError):
#             print("Datatype mismatched")#complex and int entry,output will be the superset
#         else:
#             print("Result is", result)
#         finally:
#             print("Done bhai done")
# obj = MyError
# obj.sums(5,10)

##KeyError
name = {'Amar': 30,'Akbar': 28, }
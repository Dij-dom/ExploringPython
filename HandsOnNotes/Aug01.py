# x = lambda a : a*a
# print(x(5))

#filter() map() reduce()
# l = [7,8,6,9,5,14,2,35]
# op_list = list(filter(lambda x: x%2 == 1 and x>7,l))
# print(op_list)


# x = lambda a,b,c:(a+b)
# l = list(range(1,6)) ### builtin generator
# op_list = list(map(lambda x:(x+2), l)) ####maps the expression with each element of the list
# print(op_list)


# from functools import reduce
# l = list(range(1,6)) ### builtin generator
# print("List elements are: ",l)
# factorial = reduce((lambda x,y : x*y), l) # to reduce the final result as a single value outcome
# print("The factorial result is:", factorial)

# from functools import reduce
# l2 = [1,2,3,4,5]
# op_list= list(map(lambda x: x*2,l2))
# print(op_list)
# sum_result = reduce(lambda a,b:a+b ,op_list)
# print(sum_result)

# def  function_count():
#     l2 = [1,2,2,4,3,5]
#     x = 0
#     for i in l2:
#         x = x+1
#     print(x)
# function_count()


# def  function_count():
#     l2 = [1,2,2,4,3,5]
#     sett = set(l2)
#     print(sett)
#     x = 0
#     for i in sett:
#         x = x+1
#     print(x)
# function_count()

#Implement trignometric functions
#calculate simple and compound interest

#Exceptions
#Zero Division Error
# s = "hi"
# c = 3*s
# print(c)
# print(4+c)

#How to handle the expections
# var = 0
# try:
#     print(var1)
#     print(var)
# except NameError:
#     print("Variabe is not defined.")
# except:
#     print("Something else went wrong")

# try:
#     x = 10
#     print("Result", 100/x)
# except:
#     print("Something went wrong.")
# else:
#     print("Nothing went wrong.")

# def f():
#     x = int("Four")
# try:
#     f()
# except ValueError as e:
#     print("Got it",e)
# finally:#get's executed always
#     print("Let's go")

# try:
#     x = (input("Enter the value of x\n"))
#     x = int(x)
#     print(100/x)
# except:
#     print("Something went wrong.")
# else:
#     print("Nothing went wrong.")
# finally:
#     print("THe value of X you entered is:", x)

# import sys
# randomList = ['a',0,2]
# for entry in randomList:
#     try:
#         print("The entry is ", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops",sys.exc_info()[2]," occured.")
#         print("Next Entry")

# print("The reciprocal of", entry, "is",r)


# x = (input("Enter the value of x\n"))
# x = int(x)
# print(x)

abc = {"a":1,"b":3}
print(abc.items())


# def BasicMath():
#     a = float(input("Enter the first value: \n"))
#     b= float(input("Enter the second value: \n"))
#     sum = a+b
#     diff = a-b
#     pdt = a*b
#     div = a/b
#     rem = a%b
#     fd = a//b
#     print("The sum is: ",sum)
#     print("The difference is: ", diff)
#     print("The product is: ",pdt)
#     print("The quotient is: ",div)
#     print("The reminder is: ",rem)
#     print("Floor division is",fd)
# BasicMath()

# def grader(name,mark):
#     if mark >80:
#         gradee = "A"
#         print(f"{name} got A grade.\n")
#     elif (mark>60 and mark<=80):
#         print(f"{name} got B grade.\n")
#     elif (mark>40 and mark<=60):
#         print(f"{name} got C grade.\n")
#     else:
#         print(f"{name} got D grade. Study well!\n")
# name= input("Enter the name of the student: ")
# mark = int(input("Enter the mark of student: "))
# grader(name, mark)

#Default parameter
# def myfun(name, sub = "PYTHON",mark = 50):
#     print("Name ",name ,"\nSubject: ",sub, "\nMark: ",mark)
# myfun("Dijin","python",99)

##*args
# def myfun3(*args):
#     print("The members of the community are ",*args)
# myfun3("Aaa","bbb","ccc")

#key value argument(kwargs)
# def myfun4(c1,c2,c3,c4):
#     print("The eldest son of King dasharata is: ",c1)
# myfun4(c1="Rama",c2="Lakshmana",c3 = "Bharatha", c4 = "aaaa")
#to hide some content from the user.

#**args
# to pass any no. of kw pairs
# def myfun5(**args):
#     print("The elder child of king Dasharatha is", args['c1'])
# myfun5(c1="Rama",c2="Lakshmana",c3 = "Bharatha", c4 = "Shatrugna")

#to print as a dictionary
def myfun5(**args):
    print("The elder child of king Dasharatha is", args)
myfun5(c1="Rama",c2="Lakshmana",c3 = "Bharatha", c4 = "Shatrugna")


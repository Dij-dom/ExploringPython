#Function Overloading
#Polymorphism
# def f1(a,b):
#     sum = a + b
#     print("The sum is", sum)
# def f1(a,b,c):
#     pdt = a*b
#     print("The product is", pdt)
# f1(5,6)

#Python does not suppport function overloading
#can be donw using *args and dispatcher

# def f1(a,b):
#     sum = a + b
#     print("The sum is", sum)
# def f1(*args):
#     pdt =1
#     for i in args:
#         pdt = pdt*i
#     print("The product is", pdt)
# f1(5,6)

def myfun(*kwargs):
    for i in args:
        print(i)
        valueRes = L[1].values()
        print("valRes is",valueRes)
        getRes = L[1].get("MST272")
        print(getRes)
        L.append(10)
        x = lambda mylist:len(mylist)
        print("My list contains: ",L)
    return(x(L))
L = {{1:"Anna"},{"MST272":"Python"},{2174:"US"}} #3 different dictionary
myfun(L)


#Dataypes
# Basic: String, int, float, Complex
# User defined: Lists, Tuples, Sets, Dictionary
#List
#Mutable ddquential collection of Heterogenous data, Indexed
#Tuples: Un-Mutable, Heterogenous data, Indexed
#Sets
#Dictionary: Key-value pair

#list
# x = 10
# y = x
# print("Add. of x", id(x))
# print("Add. of y", id(y))

# x +=10
# print("Add. of x", id(x))
#value changes, memory allocated to that updated value. Or, if the value is same, it points to the same memory location

m = list([1,2,3]) #list constructor
# n = m
# print(type(n))
# print("Index location of m: ",id(m))
# print("Index location of n: ",id(n))
# print(id(m) == id(n))
# m.pop()
# print(m)
# print(n)

# copy(), insert(), append
o = m.copy()
print(o)

o.insert(1,"hehe")
print(o)

o.append("helloo")
print(o)

# o.replace(1,3) #doesn't work in python lists
# o

o.replace(o(0),10) #only work with string
print(o)

#clear:clear the content and make it an empty list
#del: delete the entire list

#extend: adding multiple list together whereas insert add elements. 

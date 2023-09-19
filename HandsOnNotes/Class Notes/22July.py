                    # list        Tuple           set             Dictionary
# Mutability         y              n               n                       y
# Indexibility       y              y               n                       y
# Duplication        y              y               n                       y #values can be duplicated, key's cannot
# Heterogenity       y              y               y                       y


# t1 = ('1')
# t2 =(" A")
# t3 = t1+t2
# print("tuple t3 is a new variable", t3, len(t3))   #white spaces are counted in len()
# print(t3[0])


# tt = (12,13,24,25,16)
# print(sorted(tt))
# print(type(sorted(tt)))
#sorted method convert tuple into list and then sort the tuple

# in and not in for finding whether the element is present in the tuple

#stepIndexing
# ttt = (0,1,2,3,4,5,6,7,8,9)
# print(ttt[1:5])
# print(ttt[1:5:2])


#SET
# Set is a non index heterogeneous collection of elements.
#denoted by {}
# myset = {1,2,3,4,"haii"}
# myset1 = set(("a",123,3.14))
# myset2 = set(["A",100,45.8])
# print(type(myset))
# print(type(myset1))
# print(type(myset2))

# print(myset[1]) #it is not indexible

# myset3 = {}
# print(type(myset3))
# #for dictionary and set we use {}. 
# myset4 = {""} # empty set
# print(type(myset4))
# myset5 = {[]}
# print(type(myset5))

#Set operations
# a1={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5}
# c = {3, 4, 5, 6}
# d = {4, 5, 6, 7}
# print("a union b,c,d : ",a.union(b, c, d))
# print("a intersection b,c,d : ",a.intersection(b, c, d))
# print("a difference b,c : ",a.difference(b, c)) #element in a not in b and c.
# print("The symmetric_difference between a and b : ",a.symmetric_difference(b)) #returns the common/unique element
# print("The set a is a subset of set a1: ",a.issubset(a1))
# print("The set a is a superset of set a1: ",a.issuperset(a1))

#Set doesn't allow duplicate.
#Set isn't mutable

# mysett = {10,20,30,["A","e"]}
# print(mysett)
#can't add list inside a set(mutable)


# mysett1 = {10,20,30,("A","e")}
# print(mysett1)
#can enter tuple inside a set.(immutable)

#Union |
#Intersection &
#Difference -
#Symmetric difference: ^

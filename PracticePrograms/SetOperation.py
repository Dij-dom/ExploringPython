def input_set():
    s1 = input("Enter the set of elements with commas as seperator\n")
    return set(s1.split())
def unionn():
    union_result = sett1.union(sett2)
    print(union_result)
def intersec():
    intersection_result = sett1.intersection(sett2)
    print(intersection_result)
def setdiff():
    difference_result = sett1.difference(sett2)
    print(difference_result)

print("Set Operations Helper\n")
sett1 = input_set()
sett2 = input_set()
while True:
    print("Enter your Choice:\n"+"Press 1 for Union\n"+ "Press 2 for Intersection\n"+ "Press 3 for Set Difference\n"+ "Press 4 to Quit\n")
    ch = int(input())
    if ch ==1:
        unionn()
    elif ch ==2:
        intersec()
    elif ch ==3:
        setdiff()
    elif ch ==4:
        break
    else:
        print("Enter a valid choice\n")
    

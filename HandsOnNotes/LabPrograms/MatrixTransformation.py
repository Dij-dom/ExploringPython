#Given x,y
#Scaling
# Input the scaling factors
# create a matrix [Sx,0,0,Sy]
# form a column matrix with values x,y
# multiply both we get the final value
#Rotation
# input the angle theta
# create the matrix [cos(theta) ,sin(theta), -sin(theta), cos(theta)]
# form a column matrix with values x,y
# multiply both we get the final value
#Translation
#add the translation factors tx,ty to x and y.

import numpy as np

def scaling(m):
    Sx,Sy = map(int,input("Enter the Scaling factors: ").split())
    mL = [Sx,0,0,Sy]
    Sm = np.array(mL)
    Sm = Sm.reshape(2,2)
    transformed_matrix = np.dot(Sm,m)
    print("The tranformed values are:\nX' = ",transformed_matrix[0,0],"\nY' = ",transformed_matrix[1,0])

def rotation(m):
    theta = int(input("Enter the rotating angle: "))
    mL = [np.cos(theta) ,-np.sin(theta), np.sin(theta), np.cos(theta)]
    Sm = np.array(mL)
    Sm = Sm.reshape(2,2)
    transformed_matrix = np.dot(Sm,m)
    print("The tranformed values are:\nX' = ",round(transformed_matrix[0,0],2), "\nY' = ",round(transformed_matrix[1,0],2))

def translation(m):
    Tx,Ty = map(int,input("Enter the translating factors: ").split())
    mL = [Tx,Ty]
    Sm = np.array(mL)
    Sm = Sm.reshape(2,1)
    transformed_matrix = np.add(Sm,m)
    print("The tranformed values are:\nX' = ",round(transformed_matrix[0,0],2), "\nY' = ",round(transformed_matrix[1,0],2))

x,y = map(int,input("Enter the value of x and y: ").split())
l = [x,y]
m  = np.array(l)
m = m.reshape(2,1)
while True:
    ch = int(input("Enter your choice\n1 for Scaling\n2 for Rotation\n3 for Translation\n4 to Quit."))
    if ch ==1:
        scaling(m)
    elif ch ==2:
        rotation(m)
    elif ch ==3:
        translation(m)
    elif ch ==4:
        break
    else:
        print("Enter a valid choice.")

#This is a program to find the square of a number and implement Unbound Local error
def cal_square():
    try:
        print("Square of x:", x**2)  # This line will raise an UnboundLocalError.
    except UnboundLocalError as e:
        print("Error:", e)
        print("Caught the UnboundLocalError. Enter the value for x: ")
        x = int(input())
        print("Square of x (after initialization):", x**2)
cal_square()

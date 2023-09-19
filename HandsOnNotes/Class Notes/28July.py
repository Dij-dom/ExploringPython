# d = dict({1:"a",2:"b"})
# print(d)

#Recurrsive FUunction
# def myfactorial(num):
#     if num ==1:
#         return 1
#     else:
#         return num * myfactorial(num-1)
# num = int(input("Enter the number: \n"))
# print(f"The factorial of {num} is {myfactorial(num)}")


def binary_search(arr, low, high, x):
# Check base case
    if high >= low:
        mid = (high + low) // 2
# If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
# Element is not present in the array
        
# Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 50
# print("Enter the total elments in the array: ")
# n = int(input())
# print("Enter the array: \n")
# for i in range(n):
#     arr = arr[i]

# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")
import random
import names

def generate_mail_id(first_name, last_name):
    return f"{first_name.lower()}.{last_name.lower()}@gmail.com"

# Create a list to hold the observations
observations = []

# Generate 100 observations
for _ in range(100):
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    mail_id = generate_mail_id(first_name, last_name)
    observations.append((f"{first_name} {last_name}", mail_id))

# Print the observations
for i, observation in enumerate(observations, 1):
    print(f"{i}. {observation[0]:<20} {observation[1]}")

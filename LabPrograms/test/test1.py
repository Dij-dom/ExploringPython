# sum = 0
# for i in range(1,11):
#     if i%2 == 0:
#         print(i)
#         sum  += i
# print(sum)

# l = []
# print()
# n = int(input("Enter the number of elements to be added: "))
# for i in range(n):
#     print("Enter the ",i+1, "-th","element: ")
#     a = int(input())
#     l.append(a)
# print(l)


# y = lambda a: a**2
# print(y(5))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
score_query = list(student_marks[query_name])
s = sum(score_query)
avg = s/len(score_query)
print("The average is ", round(avg,2))

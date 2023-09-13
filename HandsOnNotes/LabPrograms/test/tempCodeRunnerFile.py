n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
score_query = list(student_marks[query_name])
sumq = 0
for i in score_query:
    sumq += i
avg = sumq/len(score_query)
print("The average is ", round(avg,2))
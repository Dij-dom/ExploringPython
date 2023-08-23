import re
pat2 = "(\w+)@((\w+\.)+(com|org|net|edu|in))"
r2 = re.match(pat2,"Raheem@cs.christuniversity.in.inoo")
print("full pattern match is obtained by r2.group(0) or r2.group()", r2.group(0))
print("first part of the pattern is given by r2.group(1)", r2.group(1))
print("Second part of the pattern is given by r2.group(2)",r2.group(2))
print("Third part of the pattern is given by r2.group(3)",r2.group(3))
print("Fouth part of the pattern is given by r2.group(4)",r2.group(4))
print(r2.group(5))##gives error as we don't have any 5th group there are only four groups here
###Findout what happens if .in is replaced by .uk?
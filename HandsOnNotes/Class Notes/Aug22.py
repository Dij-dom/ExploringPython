###Regular expressions in python
import re #re is the object to access the package
### Searching all occurences of a pattern anywhere in the given string
str = "Going to watch FIFA @Spain in the train. In train less pain as it doesnt strain."
x = re.findall('in', str) ###NOTE: Only findall() works with count() function.
print(x)
print("No.of times the search pattern repeated is:",x.count('in'))
####find() leads to an error why? because find is a string method whereas re is not


#to check whether it starts with Going and ends with train
import re
input_str = "Going to watch FIFA Spain in the train. In train it doesnt strain"
x = re.search("^Going.*train$", input_str)
print(x)

import re
#### Tosearch the exact element
str = "Going to watch FIFA @Spain in the train. In train it doesnt strain."
x = re.findall("\s", str)
print("The first white-space character is located in position:", x)
y = re.search("Spain", str)
print(y)
z = re.search("Portugal", str)
print(z)

import re
#str = "Going to watch FIFA @Spain in the train. In train it doesnt strain."
str="V,I,B,G,Y,O,R" # str="V,IB, G,YO,R"
x = re.split(",", str) #, is the delimiter here
print(x) # x is a list
### If want to restrict the number of splitted words
y = re.split("\s", str,5)
print(y)

#with the delimiter as G
import re
str="V,I,B,G,Y,O,R"
x = re.split("G", str) 
print(x)

###sub() function substitute the string
import re
str = "Going to watch FIFA @Spain in the train. In train it doesnt strain."
x = re.sub("\s", "_", str)
print(x)
z = re.sub("@Spain", "-Portugal", x)
print(z)
#### Replace first five occurences
y = re.sub("\s", "_", str, 5)
print(y)

#find a range of numbers
import re
x = "a sdf  sdfsfj sdfwin sdfgkm sdlkf "
y = re.findall('[0-9]+',x) #to find one or more digits
print(y)

import re
x = "a sdf sdfsfj sdfwin sdfgkm sdlkf "
y = re.search('[0-9]+',x) #to search one or more digits
print(y)

#how to find out the index od all the matching occurences using search or other inbuils finctio in  re. IN case if no inbuilts function is identified create your own user defined function to find ithe index if all the occurences matching the search pattern

import re
x = 'From : using the : chatacter'
y = re.findall('^F.+:',x)
print(y)


import re
x = 'From : using the : chatacter'
y = re.findall('\S+@\S+',x)
print(y)

import re
x = 'From : using the : chatacter'
# y = re.findall('\S+@\S+',x)
y =re.findall('^the (\S+@\S+)',x)
print(y)

import re
x = 'From : using the : chatacter'
# y = re.findall('\S+@\S+',x)
y =re.findall('^From (\S+@\S+)',x)
print(y)

#extracting a host iusing find and string slicing
data  = 'From stephen.marquard@uct,ac,za Sat Jsn 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find('', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

import re
pat = "\w+@(\w+\.)+(com|org|net|edu|in)"
r1 = re.match(pat,"Raheen@cs.christuniversity.in")
print(r1.group())

import re
pat2 = "(\w+)@((\w+\.)+(com|org|net|edu|in))"
r2 = re.match(pat2,"Raheem@cs.christuniversity.in")
print("full pattern match is obtained by r2.group(0) or r2.group()", r2.group(0))
print("first part of the pattern is given by r2.group(1)", r2.group(1))
print("Second part of the pattern is given by r2.group(2)",r2.group(2))
print("Third part of the pattern is given by r2.group(3)",r2.group(3))
print("Fouth part of the pattern is given by r2.group(4)",r2.group(4))
print(r2.group(5))##gives error as we don't have any 5th group there are only four groups here
###Findout what happens if .in is replaced by .uk?



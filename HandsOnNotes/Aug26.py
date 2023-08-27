#file 
f = open("ExploringPython\HandsOnNotes\AboutME.txt","a")
#a : append mode
#r : read mode
f.write("I am 22 years old.")
f.close()


f = open("ExploringPython\HandsOnNotes\AboutME.txt","rb")
print(f.read())
f.close()

f = open("ExploringPython\HandsOnNotes\AboutME.txt","r")
print(f.readline()) #returns only the first line.and

f = open("ExploringPython\HandsOnNotes\AboutME.txt","r")
print(f.readlines(5)) #returns only the first 3 lines

f = open("ExploringPython\HandsOnNotes\AboutME.txt", "r")
print(f.readline())
print(f.readline())
f.close()

f = open("ExploringPython\HandsOnNotes\AboutME.txt", "r")
count = 1
for lines in f:
    count = count+1
    print(lines)
    if count==3:
        break
f.close()

f = open("ExploringPython\HandsOnNotes\AboutME.txt", "r")
#print(f.readlines(10))
f.seek(10)
print(f.tell())
print(f.readline())
f.close()

# Open a file
fo = open("ExploringPython\HandsOnNotes\AboutME.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)
# Check current position
position = fo.tell() # to get the current cursor position
print("Current file position : ", position)
# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(25)
print("Again read String is : ", str)
# Close opend file
fo.close()

img = open("ExploringPython\HandsOnNotes\img.jpg","rb")
print(img.read())




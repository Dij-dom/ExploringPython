#Checking for value error
import sys
try:
    f = open("Notes\HandsOnNotes\sample.txt",'w')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}:{1}".format(errno,strerror),errorss)
    print(e)
except ValueError:
    print("Value error. No value integer in line.")
except:
    print("Unexpected error:",sys.exc_info()[1])



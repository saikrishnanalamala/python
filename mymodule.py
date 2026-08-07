'''def greetings(name):
    print("welcome",name)'''



'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''


'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''        



#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.log(2))
print(math.tan(45))
print(math.sin(60))
print(math.cos(30))
print(math.ceil(2.9))
print(math.ceil(5.9))
print(math.floor(2.7))'''


'''from math import pi,log,sqrt
print(pi)
print(log(10))
print(sqrt(2))'''



'''#sys module
import sys
print(sys.path)
print(sys.version)'''



#os module-opterating system
import os
'''print(os.path)
print(os.getcwd())
print(os.listdir())'''



'''print(os.mkdir("aug4"))
print(os.listdir())'''


'''print(os.chdir("C:\\Users\\ASUS\\Downloads"))
print(os.listdir())'''



#ASCII
'''print(chr(67))

print(chr(65))

print(chr(90))

print(chr(93))

print(ord("a"))

print(ord("z"))
#print(ord(97))#error
print(chr(97))'''



'''for i in range(65,91):
    print(chr(i),end=" ")'''



'''for i in range(97,123):
    print(chr(i),end=" ")'''



'''a=input("name")
for i in a:
    print(i,"-",ord(i))'''



#random module-is used to genrate random numbers in python,randint is used and these function is defined in random module

#sample

'''import random
a=random.sample(range(10,50),10)
print(a)'''



#randiant

'''import random
a=random.randint(40,50)
print(a)'''



#choice
'''import random
a=[10,40,50,60,70]
b=random.choice(a)
print(b)'''



#regular expression:regular expression are powerful tools (module) embedded in python which is mainly use to find pattern within a given string or statement or files and we mainly used for text manipulation.

#regex(regular expression)
'''a="codegnan is in vij"
print(a)'''


'''a="codegnan\nis\tin\nvja"
print(a)'''


#rstring
'''a=r"codegnan\nis\t\nvja"
print(a)'''


#compile(),search(),findall(),split(),sub
#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D-> it matches non digit
\s->it represents white spaces
\S->it represents non-white spaces'''



#compile()

import re
a="map maths cat code cash money mat cup cap monkey"
'''b=re.compile(r"m\w\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''


'''b=re.search(r"m\w+",a)
print(b)'''



#findall()
'''c=re.findall(r"m\w+",a)
print(*c)'''



'''d=re.findall(r"c\w+",a)
print(d)'''



#split()
'''d=re.split(r"m",a)
print(d)

e=re.split(r"\s",a)
print(e)'''

#sub()
'''f=re.sub(r"m","a",a)
print(f)'''



import re
'''a="year 2026 month 8 date 6"
b=re.findall(r"\d+",a)
print(b)'''





#error handling

#1.syntax errors-compiler errror
#2.run_time error-during execution time it will happens
#3.logical error-error in logical(it is invisible)



#syntax errors
'''for i in range(20)
print(i)'''



#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''#10//0->zero division error


#logical error
'''a=10
b=20
print(a-b)'''

























#Syntax
#oops
'''class classname():
    #attributes
    name="sai"
    age=22
    place="vja"
    def fname(method_name):
        print("statement.............")
a=classname()
print(dir(a))
a.fname()'''




#class declaration
'''class details():
    name="sai"
    age=22
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''




#object instantiation
'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("sai",22,"vij")
a.display()
b=details()
b.data("ganesh",21,"ogole")
b.display()
c=details()
c.data("harish",19,"hyd")
c.display()'''



#object intialization
'''class data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=data("sai",22,"vja")
print(dir(a))
a.display()
b=data("sonu",22,"hyd")
print(dir(b))
b.display()'''





'''class data():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=data()
print(dir(a))
a.display()'''




#diff blw _ and __
#when user want to create a variable in python by using __ underscore our python interpreter treats it as special variable to avoid name conflicts with methods and inner classes

'''class Employee():
    def __init__(self):
        self.name="pooja"  #public
        self._mailid="pooja@codegnan.com"  #protected
        self.__salary=10000  #private variable
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee__salary)

class Employee1():
    def __init__(self):
        self.name="yuvaraj"  #public
        self._mailid="yuvaraj@gmail.com"  #protected
        self.__salary=10000  #private variable
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)'''


#polymorphism

#operator overloading

'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(6))
print(a.__pow__(2))
#print(a.__div__(4))
print(a.__eq__(4))
print(a.__le__(8))
print(a.__ge__(10))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())'''

#operator overriding

'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
#x=6
#y=4
print(x+y)'''

#method overloading

'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("product is",a*b)
        else:
            print("program ends......")
a=new()
#a.sum()
#a.sum(3,6,8)
a.sum(4,5)'''

#method overriding

'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#task

'''class car():
    def vehicle(self):
        print("thar")
class bike():
    def vehicle(self):
        print("vespa")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''






#inheritance
#single-inheritance
'''class RBI():#parent class
    cash=100000
    def availble_cash(cls):
        #print("availble cash is",cls.cash)
        print("availble cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+cls.cash)
a=HDFC()
a.availble_cash()
a.new_cash()'''




#multi-inheritance
'''class father():
    def height(self):
        print("height is 6ft")
class mother():
    def weight(self):
        print("weight is 65kg")
class kid(father,mother):
    def dob(self):
        print("just born............")
a=kid()
a.height()
a.weight()
a.dob()'''



#multi level inheritance
'''class grandparent():
    def land(self):
        print("land is 1acre land")
class parent(grandparent):
    def house(self):
        print("parent has house")
class kid(parent):
    def bike(self):
        print("pulsar")

a=kid()
a.land()
a.house()
a.bike()'''




#hierarchical inheritance

#hierarchical inheritance is one parent class is inheritant by multiple child classes.

'''class employee():
    def company(self):
        print("company name is delitee")
class trainer(employee):
    def teaching(self):
        print("trainer teach the code")
class developer(employee):
    def develop(self):
        print("developer develops the code")

a=trainer()
a.company()
a.teaching()
b=developer()
b.develop()'''

#hybrid inheritance
'''it means combine one or more than one type of inheritance for example-multi level,multiple'''
class person():
    def details(self):
        
    





























        






















    
    
    
















        











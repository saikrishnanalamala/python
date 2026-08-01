'''a="hello world"
print(a)'''


'''a=[2,3,4,5,6]
print(max(a))'''



'''b=[7,8,3,5,6]
print(min(b))'''


'''#fromkeys()
a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))
b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"sai")
print(c)
c["o"]="python"
print(c)'''



#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''



'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''


'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''





#zip()-it can combine multiple collections into one collection

'''a=[10,20,30,40,50]
names=["sai","krishna","GANESH","harish","sonu"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)


c=tuple(zip(a,names))
print(c)


c=set(zip(a,names))
print(c)


c=dict(zip(a,names))
print(c)

d=list(zip(a,names))
print(*d)'''

names=["hemanth","vasu","sai","roop","spider"]
'''for i in range(len(names)):
    print(i)'''


'''b=dict(enumerate(names))
print(b)'''


'''b=dict(enumerate(names,100))
print(b)'''





                                      #train ticket application


'''while True:
    def railway_ticket():
     ticket=1000
    gender=input("enter the gender")
    age=int(input("enter the age"))
    if gender=="m":
        if age>=60:
            print("senior citizen")
            ticket=ticket-30/100*ticket
            print(ticket)
        elif age<60:
                print("normal citizen")
                print(ticket)
        elif gender=="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
        elif age<60:
            print("normal citizen")
            ticket=ticket-30/100*ticket
            print(ticket)
    railway_ticket()'''
   
            
            

#anonnymous functions: are name less function and we use  a keyword called lambda to create annonymous function 



'''def f(x):
    print(2*x+5)
f(5)'''




'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''




#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''




'''a=int(input("enter thge number"))
b=lambda x:3*x+5
print(b(a))'''



'''a=str(input("enter the names"))
b=lambda a:a.upper()
print(b(a))'''


'''a="python course"
#python course
b=lambda a:a.title()
print(b(a))'''


'''a=lambda x,y:x*y
print(a(2,4))'''


'''a=int(input("enter the value"))
b=int(input("enter the value"))
c=lambda a,b:a*b
print(c(a,b))'''



'''fname="sai"
lname="krishna"
c=lambda x:fname+lname
print(c(0))'''


'''a,b=[x for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b)'''




#filter()
a=[10,20,30,50,45,23,60,70]
'''if a%2==0:
    print(a)'''


'''for i in a:
    if i%2!=0:
        print(i)'''


'''b=list(filter(lambda x:x%2==0,a))
print(b)'''



#[],(),{}

'''a=[]
print(type(a))'''


'''b=()
print(type(b))'''


'''c={}
print(type(c))'''


'''d=set()
print(type(d))'''



'''a=[[],(),set()," ",None,3,5.6,"python",2+3j,True,False]
b=list(filter(None,a))
print(b)'''



#map()-each object from a collection and forms a new collection
'''a=[2,5,7,9,10,20,30,80]
b=[1,9,20,50,60,4,25,80]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''






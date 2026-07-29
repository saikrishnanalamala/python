'''#functions
1.function is a block of organized,reusedble code and i.e used to perform a single or multiple tasks.
2.python gives inbulit functions like print,function you can make ur own function also and these are user defined functio
3.function block  begin with the key word def  followed by perastatic ().'''



#sum,diff,product()
'''a=10
b=20
print("the sum is",a+b)
print("the diff is ",a-b)
print("the product is",a*b)'''

'''a=200
b=500
print("the sum is",a+b)
print("the diff is ",a-b)
print("the product is",a*b)'''



'''a=1000
b=2000
print("the sum is",a+b)
print("the diff is ",a-b)
print("the product is",a*b)'''




#functions
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is ",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''




'''def calculator(a,b):
   print("the pow is",a**b)
   print("the  intdiv is ",a//b)
   print("the mod is",a%b)
calculator(10,20)
calculator (3,5)
calculator(4,6)'''

'''def add(a,b):
 print(a+b)
add(5,7)'''



'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add() '''



'''def add():
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()
add()'''


#print and return difference()
#print just shows the human user output in  a conusole.
#return is a keyword and written is  used to terminate the function and gives back value from the function.'''


'''def mul(a,b):
    print(a*b)
mul(4,5)'''




'''def mul(a,b):
  return a*b
print(mul(4,6))'''



'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,6))'''






'''while True:
 def cal():
     a=int(input("enter the a value"))
     b=int(input("enter the b value"))
     option=int(input(choose the option
                           1.add
                           2.mul
                           3.mul))
     if option==1:
         print(a+b)
     elif option==2:
         print(a-b)
     elif option==3:
         print(a*b)
 cal()'''
 
    
            
          
    
#spilt bill
#1normal2.fstring.3.format

'''amount=int(input("enter the value"))
p=int(input("enter the person count"))
c=amount/p
print(c)'''


'''def spiltbill():
    amount=int(input("enter the value"))
    p=int(input("enter the person count"))
    print(f"per head bill is{p//amount}")
    print("per head bill is {}".format())
spiltbill()'''


#keywords and postional aruguments
'''def details(id,name,mailid):
    id=12
    name="sai"
    mailid="sai0123@gmail.com"
    print("id,name,mailid")
details(id="id",name="name",mailid="mailid")'''



'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="sai",mailid="mahesh@gmail.com")
details(id=30,name="krishna",mailid="saikrishna@gmail.com")
details("raju","rju@gmail.com",17)'''



#default  arguments
'''def grocery(item,price):
           print("item is %s"%item)
           print("price is %.2f"%price)
grocery("rice",1200)'''




'''def grocery(item="sugar" ,price=600):
           print("item is %s"%item)
           print("price is %.2f"%price)
grocery()'''




'''def grocery(item,price=200):
           print("item is %s"%item)
           print("price is %.2f"%price)
grocery("dhal")'''



'''def grocery(item="ghee",price):
    #non def arg follows def arg
           print("item is %s"%item)
           print("price is %2f"%price)
grocery(1340)'''




#cake,price,quantity
'''def bakery(cake,price,quantity):
    print("items is %s"%cake)
    print("price is %.2f"%price)
    print("qunatity is %s"%quantity)
bakery("choclate",500,"1kg")'''




'''def bakery(cake="butterscoth",price=700,quantity="1kg"):
    print("items is %s"%cake)
    print("price is %.2f"%price)
    print("qunatity is %s"%quantity)
bakery()'''




'''def bakery(cake,price,quantity="1/2kg"):
    print("items is %s"%cake)
    print("price is %.2f"%price)
    print("qunatity is %s"%quantity)
bakery("pineapple",500)'''




'''def bakery(cake="vinnela",price=700,quantity):
    #non def arg is follows def arg 
    print("items is %s"%cake)
    print("price is %.2f"%price)
    print("qunatity is %s"%quantity)
bakery(quantity="1kg")'''



#* arguments(* is used to unpack the elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)'''


'''a=(10,20,30,40,50)
print(a)
print(*a)'''


'''a={10,20,30,40,50}
print(a)
print(*a)'''



'''a={"name":"sai","year":2026}
print(a)
print(*a)'''



'''a,b,c=2,3,4,5,6,7,8,9,0
print(a)
print(b)
print(c)'''



'''(a,*b,c)=2,3,4,5,6,7,8,9,0
print(a)
print(*b)
print(c)'''



'''(*a,b,c)=2,3,4,5,6,7,8,9,0
print(*a)
print(b)
print(c)'''





'''(a,*b,c)="codegnan"
print(a)
print(*b)
print(c)'''


#variable len aruguments: variable len arugements are automatic stored in tuple we use *arugements


'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[4,5,6,7,8]
check(*b)
c={6,7,8,9,10}
check(*c)5
d={"name":"sai","city":"vij"}
check(*d)'''




'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
           d=d+i
           print(d)
check1()
check1(2,3,4,5,6,7)
check1(1,3,4,5.2,3.4)
check1(3,4,2,5,3.6,2.4,"pooja",True,2+3j)'''



#kwargs(**)
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnoms":[10,20,30],
         "names":["sai","krishna","visesh"],
          "status":["p","a","p"]}
check(**details)'''


#both * and **usage
'''def final(*a,**b):
    d=3#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6.2)
final(*data)
details={"idnoms":[10,20,30],
         "names":["sai","krishna","visesh"],
          "status":["p","a","p"]}
final(**details)
final(*data,**details)'''




#max(),min(),sum()

'''print(max(5,7,9,10,20,40))'''


'''print(min(5,7,9,10,20,40))'''

'''a=2,3,4,5,5,67
print(sum(a))'''



#task :
#marks analysis report

'''students=int(input("enter no.of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student{i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print("............ marks analysis report..................")
print("total students",students)
print("heighest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average",sum(marks)/students)'''

    













       
    


    












    
    







            















   






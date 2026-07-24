#list comprehension:
'''every list comprehension will be written as loop but every loop canot rewritten in list.'''

#["python","java","dsa"]
'''a=["python","java","dsa"]
b=str(a)
print(b.upper())'''

'''a=["python","java","dsa"]
for i in a:
    print(i.upper(),end=" ")'''


#syntax()
#a=[expr for var in collection/range]
'''a=["python","java","dsa"]
a=[i.upper() for i in a]
print(a)'''

'''a=["codegnan","course","python"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,3,4,5,6,8,12,13]
#[1,9,16,25,36,64,144,169]
b=[i**2 for i in a]
b=[pow (i,2) for i in a]
print(b)'''

'''a=[ i for i in range(0,21) if i%2==0]
print(a)'''

'''a=[ i for i in range(0,21) if i%2!=0]
print(a)'''


'''a=a=[i*i for i in range(0,21) if i%2==0]
print(a)'''


a=["apple","banana","mango","dragon","kiwi","berry"]
'''b=[i for i in a if "a" in i]
print(b)'''


'''b=[i for i in a if "a" not in i]
print(b)'''


'''a=[i**2 if i%2==0 else i*5 for i in range(16)]
print(a)'''



a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6,6]
'''c=[a[i]+b[i] for i in range(len(a))]
c=[a[i]+b[i] for i in range(5)]
print(c)'''



                                    #attendence  report

'''students=int(input("Enter the total number of students"))
p=0
a=0
for i in range(1,students+1):
    attendence=input(f"student{i}(p/a)")
    if attendence=="p":
        p+=1
    elif attendence=="a":
        a+=1
print(".......student report.......")
print("total students attendence",students)
print("total students present",p)
print("total students absent",a)'''
        
                     



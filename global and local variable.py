#global and local variable
#a variable is defined above the function and  is accesiable to the global space is called global and local variable
#a variable is defined inside function is called local variable.



'''a=2
def check1():
    print("the inside value is",a)
check1()
print("outside value is",a)'''


#second case of global variable
'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''


#third case of global variable
'''a=3
b=8
def check3():
    a=6
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''



#usage of global keyword
#when user wants to create a variable inside the function and carry forword the update the value then we can use global keyword


'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("updated value is",a)
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is ",a)
print("b value is ",b)'''



#generators
# no tuple comprahension in above cases if we remove there braces and keep paranthesis then the outcome is generator.

#a=[expr for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''


'''a=(i for i in range(16))
print(*a)
print(type(a))'''


'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''



#a generator is also a function which can be used an interator(loop)
'''by producing group of values and we can use yield key word'''
#yield vs return
'''return will terminated the function,where as yield can pass the function and go with succesive interartion'''


'''a,b=(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''



'''a,b=(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        #return a
        return a
print(check(a,b))'''



'''def mygen():
    #return "vij"
    #return "hyd"
    #return "viz"
    return "vij","hyd","viz"
print(*mygen())'''



def mygen():
    yield "python"
    yield "java"
    yield "c++"
print(*mygen())


#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))#stop iteration












  










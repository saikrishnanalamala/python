#exception handling
#try-imstructions from which we are expecting the exceptions
#except->exceptions are raised in try block it will be handle by the block
#else:no exceptions(optional)
#finally-always it will display


'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exception")
    finally:
        print("program ends............")'''





#file handling
#write()
'''a=open("sai.txt","w")
b=a.write("python full stack")
a.close()'''



'''a=open("sai.txt","w")
b=a.write("codegnan it solutions")
a.close()'''



#append()
'''a=open("sai.txt","a")
b=a.write("\tsai")
a.close()'''


'''a=open("sai.txt","w")
b=input("data")
a.write(b)
a.close()'''


#readlines()
'''a=open("sai.txt")
#print(a.read())#it will display entire content
#print(a.readline()#it will display firstline
#print(a.readline()#it will display in list with\n
print(a.read(7))#it will display no.of characters'''




#writelines()->it makes every object side by side
'''a=open("priya.txt","w")
b=["sai","harish","ganesh","sagar","sonu"]
a.writelines(b)
a.close()



a=open("priya.txt","w")
b=["sai","harish","ganesh","sagar","sonu"]
a.writelines("\n".join(b))
a.close()'''




'''a=open("variables.py")
print(a.read())'''
























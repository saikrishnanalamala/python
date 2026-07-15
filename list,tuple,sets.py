Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list[]
KeyboardInterrupt
a=[2,3.5,3+2j,"sai",True,False]
type(a)
<class 'list'>
print[a]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
c=[7.9]
type(c)
<class 'list'>
#extended
a=["java,python,html"
print(a)
   
SyntaxError: '[' was never closed
a=["java,python,html"]
   
print(a)
   
['java,python,html']
#insert
   
a=["vij,cpt,ongole"]
   
a.insert(2,"chennai")
   
a
   
['vij,cpt,ongole', 'chennai']
#index
   
a=["apple,banana,grapes"]
   
a.index("grapes")
   
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.index("grapes")
ValueError: 'grapes' is not in list
#sort()
   
a=["mango","apple","kiwi"]
   
a.sort()
   
a
   
['apple', 'kiwi', 'mango']
a=["di","mi","lu"]
   
a.reverse()
   
a
   
['lu', 'mi', 'di']
b=["2,5,1,7,9,4"]
   
b.reverse()
   
b
   
['2,5,1,7,9,4']
#pop()
   
a=["red","blank","blue"]
   
a.pop()
   
'blue'
a.pop(1)
   
'blank'
b=["1,2,4,6,77"]
   
b.pop(4)
   
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    b.pop(4)
IndexError: pop index out of range
b.remove(4)
   
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b.remove(4)
ValueError: list.remove(x): x not in list
b=["raju","sai","kvaan"]
   
b.remove(1)
   
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b.remove(1)
ValueError: list.remove(x): x not in list
b.pop()
   
'kvaan'
#clear
   
a=["ap","ts","ka"]
   
a.clear()
   
a
   
[]
a.clear(2)
   
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.clear(2)
TypeError: list.clear() takes no arguments (1 given)
a.append()
   
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
b=[]
   
b.append("sai")
   
b
   
['sai']
a=[10,20,30,40,"code"]
   
a.extend("code")
   
a
   
[10, 20, 30, 40, 'code', 'c', 'o', 'd', 'e']
#tuple()
   
a=(1,2.6,"vijaya",3+6j,True,False)
   
print(a)
   
(1, 2.6, 'vijaya', (3+6j), True, False)
type(a)
   
<class 'tuple'>
a.index(3+6j)
   
3
len(a)
   
6
a.count(False)
   
1
a.count(True)
   
2
#sets{}
   
a={3,4,5,6,7,9}
   
print(a)
   
{3, 4, 5, 6, 7, 9}
type(a)
   
<class 'set'>
c={15,11,20,15,4,2,7}
   
print(c)
   
{2, 4, 20, 7, 11, 15}
type(c)
   
<class 'set'>
a={1,75,7,8,9,4,6}
   
b={6,7,8,4}
   
b.issubset()
   
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    b.issubset()
TypeError: set.issubset() takes exactly one argument (0 given)
b.issubset(a)
   
True
b.issuperclass(b)
   
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    b.issuperclass(b)
AttributeError: 'set' object has no attribute 'issuperclass'
b.issubset(b)
   
True
b.issuperset(a)
   
False
#union()
   
a={1'3'5'7'8'9}
   
SyntaxError: unterminated string literal (detected at line 1)
a={1,3,5,7,8,9}
   
b={3,7,8}
   
a.union(b)
   
{1, 3, 5, 7, 8, 9}
#intersection()
   
a={1,3,4,5,6,7,9}
   
b={3,4,5,7}
   
a.intersection(b)
   
{3, 4, 5, 7}
#difference()
   
p={2,4,6,7,8,9,1}
   
q={3,5,6,7,8,9,}
   
p.difference(q)
   
{1, 2, 4}
q.difference(p)
   
{3, 5}
#update()
   
b={1,3,4,6,7,8,9]
   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
b={1,3,4,6,7,8,9}
   
C={3,4,5,7,8}
   
B.update(c)
   
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    B.update(c)
NameError: name 'B' is not defined. Did you mean: 'b'?
b.update(c)
   
b
   
{1, 2, 3, 4, 6, 7, 8, 9, 11, 15, 20}
c.update(b)
   
c
   
{1, 2, 3, 4, 6, 7, 8, 9, 11, 15, 20}
symmetricdifference()
   
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    symmetricdifference()
NameError: name 'symmetricdifference' is not defined
#symmetricdifference()
   
a={1,3,4,5,6,7,,9}
   
SyntaxError: invalid syntax
a={1,3,4,5,6,7,9}
   
b={3,5,7,9}
   
b.symmetricdifference(a)
   
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    b.symmetricdifference(a)
AttributeError: 'set' object has no attribute 'symmetricdifference'. Did you mean: 'symmetric_difference'?
b.symmetric_difference(a)
   
{1, 4, 6}
#difference_update()
   
a={3,4,5,6,7,8,9}
   
b={5,6,7,8,9}
   
a.update_difference(b)
   
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.update_difference(b)
AttributeError: 'set' object has no attribute 'update_difference'
a.difference_update(b)
   
a
   
{3, 4}
b.difference_update(a)
   
b
   
{5, 6, 7, 8, 9}
a={3,4,6,8,9,7}
   
c={4,7,8,10,9}
   
a.intersection_update(b)
   
a
   
{8, 9, 6, 7}
c.intersection_update(a)
   
c
   
{8, 9, 7}
a=
   
SyntaxError: incomplete input
a=
   
SyntaxError: incomplete input


KeyboardInterrupt
a={10,20,30,40}
   
a.copy()
   
{40, 10, 20, 30}
b=a.copy()
   
b
   
{40, 10, 20, 30}
#discard()
   
>>> b.discard(10)
...    
>>> b
...    
{40, 20, 30}
>>> a.clear()
...    
>>> a
...    
set()
>>> a=set()
...    
>>> b.add(a)
...    
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    b.add(a)
TypeError: unhashable type: 'set'
>>> a={2,4,6,7,9,8}
...    
>>> a.isdisjoint
...    
<built-in method isdisjoint of set object at 0x000002E88ABD12A0>
>>> a.isdisjoint(b)
...    
True
>>> b.issubset(a)
...    
False

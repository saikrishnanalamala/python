Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#datatypes
a=2
type(a)
<class 'int'>
b=15
type(b)
<class 'int'>
x=12.1
type(x)
<class 'float'>
y=5.79
type(y)
<class 'float'>
a='sai'
type(a)
<class 'str'>
b="krishna"
type(b)
<class 'str'>
c='''python'''
type(c)
<class 'str'>
a=7+2j
type(a)
<class 'complex'>
b=2j+4
type(b)
<class 'complex'>
a=true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a="true"
type(a)
<class 'str'>
#int
int(4)
4
int(2.7)
2
print("sai")
sai
int(2+1j)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int(2+1j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int=5j+2
int=(true)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int=(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(true)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(true)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(TRUE)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(TRUE)
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
int(True)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(True)
TypeError: 'complex' object is not callable
int(True)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(True)
TypeError: 'complex' object is not callable
#float
float(5)
5.0
float(2.7)
2.7
int(True)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(True)
TypeError: 'complex' object is not callable
>>> #int
>>> int(True)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(True)
TypeError: 'complex' object is not callable
>>> 
>>> float(False)
0.0
>>> float(True)
1.0
>>> complex(4)
(4+0j)
>>> complex(6)
(6+0j)
>>> complex(5.6)
(5.6+0j)
>>> complex("sai")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex("sai")
ValueError: complex() arg is a malformed string
>>> complex(9+2j)
(9+2j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(6)
True
>>> bool(2.5)
True
>>> bool("sai")
True
>>> bool(2+3j)
True
>>> bool(True)
True
>>> bool(False)
False

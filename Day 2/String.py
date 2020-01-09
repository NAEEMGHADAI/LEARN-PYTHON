C: \Users\naeem noman\Desktop\PYTHON\Day 2 > py
Python 3.8.1 (tags/v3.8.1: 1b293b6, Dec 18 2019, 22: 39: 24)[MSC v.1916 32 bit(Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>> > 'NAEEM GHADAI'
'NAEEM GHADAI'
>> > "NAEEM GHADAI"
'NAEEM GHADAI'
>> > WASN'T
File "<stdin>", line 1
WASN'T
^
SyntaxError: EOL while scanning string literal
>> > WASN\'T
File "<stdin>", line 1
WASN\'T
^
SyntaxError: unexpected character after line continuation character
>> > WASN \'T
File "<stdin>", line 1
WASN \'T
^
SyntaxError: unexpected character after line continuation character
>> > "wasn't"
"wasn't"
>> > 'wasn't'
File "<stdin>", line 1
'wasn't'
^
SyntaxError: invalid syntax
>> > 'wasn\'t'
"wasn't"
>> > print('hello world. welcome to visual labs')
hello world. welcome to visual labs
>> > print('hello world.\n welcome to visual labs')
hello world.
welcome to visual labs
>> > print('c:\visual labs\name')
c:
  isual labs
ame
>> > print('c:\\visual labs\\name')
c: \visual labs\name
>> > print(r'c:\visual labs\name')
c: \visual labs\name
>> > print(""" pattern
... *
... **
... ***
... ****
... """)
pattern
*
**
***
****

>> > print('ba'+2*'ta')
batata
>> > print('naeem' 'ghadai')
naeemghadai
>> > print('naeem', 'ghadai')
naeem ghadai
>> > name = 'AIMAN'
>> > name[2]
'M'
>> > name[-1]
'N'
>> > name[-3]
'M'
>> > name[-6]
Traceback(most recent call last):
  File "<stdin>", line 1, in < module >
IndexError: string index out of range
>> > name[0:2]
'AI'
>> > name[:4]
'AIMA'
>> > name[:3]+name[3:]
'AIMAN'
>> > name[0]
'A'
>> > name[0] = 'M'
Traceback(most recent call last):
  File "<stdin>", line 1, in < module >
TypeError: 'str' object does not support item assignment
>> > name[5] = 'Z'
Traceback(most recent call last):
  File "<stdin>", line 1, in < module >
TypeError: 'str' object does not support item assignment
>> > newname = 'M'+name[1:]
>> > print(newname)
MIMAN
>> > newname = name[0:2]+'K'+name[3:]
>> > print(newname)
AIKAN

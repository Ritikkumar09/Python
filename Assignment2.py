#1.Write a python script to add comments and print “Learning Python” on screen.
print("Learning Python")

#2. Write a python script to add multi line comments and print values of four variables,each in a new line. Variable contains any values.
name="Ritik"
age=24
price=230.4
need=True
print(age)
print(price)
print(need)
print(name)

#3. Write a python script to print types of variables. Create 5 variables each of them
# containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

a=35
b=True
c="MySirG"
d=5.46
e=3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#4.Write a python script to print the id of two variables containing the same integer values.

a=1234
b=1234
print(id(a))
print(id(b))

#5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable

a=35
b=True
c="MySirG"
d=5.46
e=3+4j
print(a)
print(b)
print(c)
print(d)
print(e)
print((a),type(a),id(a))
print((b),type(b),id(b))
print((c),type(c),id(c))
print((d),type(d),id(d))
print((e),type(e),id(e))

#6.Write a python script to print all the keywords
import keyword
print(keyword.kwlist)

#7.On Python shell use help() function and display the list of keywords
help()

#8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
# value to it. Write a python script to import A1 module in A0 and print value of the
# variable created in A0.py




#9.Name the keywords, used as data in the Python script.

True and False

# 10. Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and
# 9:00 PM)
 
from datetime import datetime
dt = datetime.today();
print(dt)
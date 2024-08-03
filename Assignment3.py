#1. Write a python script to convert a number into str type.
x=10
print(type(str(x)))

#2. Write a python script to print Unicode of the character ‘m’
print(ord("m"))
print(chr(50))

#3. Write a python script to print character representation of a given unicode 100.
print(chr(100))

#4. Write a python script to print any number and its binary equivalent
x=20
print(x,bin(x))

#5. Write a python script to print any number and its octal equivalent.

x=30
print(x, oct(x))
print(0o36)
#6. Write a python script to print any number and its hexadecimal equivalent.
x=30
print(x,hex(x))
print(0x1e)

#7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
y=0b1100101
print(y)

#8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
z=0x2F
print(z)

#9. Write a python script to store an octal number 125 in a variable and print it in binary format.
c=0o125
print(c,bin(c))

#10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.
a=0o25
b=0x39
print(a+b, bin(a+b))
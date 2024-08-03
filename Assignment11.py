# #     Loops

# #1. Write a python script to calculate sum of first N natural numbers
# n=int(input("enter your no. "))
# r1=range(n)
# s=0
# for i in r1:
#     s=s+(i+1)
# print(s,end=' ')
# print()
# # 2. Write a python script to calculate sum of squares of first N natural numbers
# n=int(input("enter your no "))
# s=0
# for i in range(n):
#     s=s+((i+1)**2)
# print(s,end=' ')
# print()
# # 3. Write a python script to calculate sum of cubes of first N natural numbers
# n=int(input("enter your no. "))
# s=0
# for i in range(n):
#     s=s+((i+1)**3)
# print(s,end=' ')
# print()

# # 4. Write a python script to calculate sum of first N odd natural numbers
# n=int(input("enter your no. "))
# s=0
# for i in range(1, 2*n, +2):
#     s=s+(i**2)
#     print(i**2, end=' ')
# print(s, end=' ')
# print()
# # 5. Write a python script to calculate sum of first N even natural numbers
# n=int(input("enter your no. "))
# s=0
# for i in range(2,2*(n+1),+2):
#     s=s+(i**2)
#     print(i**2,end=' ')
# print(s,end=' ')
# print()
# # 6. Write a python script to calculate factorial of a given number
# n=int(input("enter your no. "))
# f=1
# for i in range(n):
#     f=f*(i+1)
#     print(i+1,end=' ')
# print("= ",f,end=' ')
# print()
# # 7. Write a python script to count digits in a given number
# number=input("enter your no ")
# count=0
# for i in number:
#     count=count+1
#     print(int(i),end=' ')
# print(count,end=' ')
# print()
# 8. Write a python script to calculate sum of digits of a given number
number=input("enter your no. ")
s=0
for i in number:
    s=s+int(i)
    print(i, end=' ')
print(s,end=' ')
print()

# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
    
# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method
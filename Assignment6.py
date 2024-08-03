# # 1. Write a python script to check whether a given number is positive or non-positive
# x=int(input("enter your no. "))
# if x>0:
#   print("positive")
# else:
#     print("non-positive")

  

# # 2. Write a python script to check whether a given number is divisible by 5 or not
# x=int(input("enter your no. "))
# if x%5==0:
#   print("Divisibal")
# else:
#   print("not visible")
# print("number is visible by 5") if int(input("Enter your no"))%5==0 else print("The number is not divisible by 5")
# print("number is not visible" if int(input("enter your no"))%5 else "number is visible")


# # 3. Write a python script to check whether a given number is even or odd
# x=int(input("enter your no. "))
# if x/2==0:
#    print("even")
# else:
#    print("odd")
# print("odd" if int(input("enter your no"))%2 else "even")


# # 4. Write a python script to print greater between two numbers. Print number only once
# # even if the numbers are the same.
# print("enter your no")
# a,b=int(input()),int(input())
# print(a if a>b else b)

# # 5. Write a python script to print two given words in dictionary order
# w1=input("enter your word")
# w2=input("enter your 2nd word")
# if w1<w2:
#    print((w1,w2))
# else:
#    print((w2,w1))
# print("enter your two words")
# print()
# a, b=input(),input()
# print((a,b) if a<b else (b,a))

# # 6. Write a python script to check whether a given number is a three digit number or not.
# a=int(input("enter your  no "))
# if a>99 and a<1000:
#    print("no is three digit")
# else:
#    print("not three digit")

# print("no is three digig=t" if 99<int(input("enter your no"))<1000 else "no is not three digit")

# # 7. Write a python script to check whether a given number is positive, negative or zero.
# a=int(input("enter your  no "))
# if a>0:
#    print("positive")
# elif a==0:
#    print("zero")
# else:
#    print("negative")

# # 8. Write a python script to check whether a given quadratic equation has two real &
# # distinct roots, real & equal roots or imaginary roots
# a,b,c=int(input("enter your a ")),int(input("enter your b ")),int(input("enter your c "))
# d=b**2-4*a*c
# if d>0:
#     print("Real and distinct root")
# elif d == 0:
#     print("Real and equal root")
# else:
#     print("Imaginary roots")

# # 9. Write a python script to check whether a given year is a leap year or not.
# y=int(input("enter year"))
# if y%400==0 or y%100!=0 and y%4==0:
#    print("leap year")
# else:
#    print("normal year")


# # 10. Write a python script to print greater among three numbers. Print number only once
# # even if the numbers are the same.
# a,b,c=int(input("enter your a ")),int(input("enter your b ")),int(input("enter your c "))
# if a==b==c:
#    print("all are equal")
# elif a>b>c:
#    print("greater no is ",a)
# elif a<b<c:
#    print("greater no is ",c)
# else:
#    print("greater no is ",b)

# print("enter your three no")
# a,b,c= int(input()), int(input()), int(input())
# (a if a>c else c) if a>b else (b if b>c else c)


# # 11. Write a python script to take the month value in numeric format and display the
# # number of days in it.
# m=int(input("enter your month in month"))
# if m==2:
#    print("in this month 28/29 days")
# elif m in (1,3,5,7,8,10,12):
#      print("in this month 31 days")
# elif m in (4,6,9,11):
#    print(" in this month 30 days")
# else:
#    print("wrong input")

# 12. Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part
print("enter your complex no.")
x=complex(input())
print(x.imag) if x.imag>x.real else print(x.real)

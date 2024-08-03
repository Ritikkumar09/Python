# # 1. Write a python script to remove the last digit from a given number. (for example, if
# # user enters 2534 then your output should be 253)
# a=int(input("enter your no "))
# print(int((a/10)))

# # 2. Write a python script to get the last digit from a given number. (for example, if user
# # enters 2089 then your output should be 9)
# a=int(input("enter your no "))
# print(int((a%10)))

# # 3. Write a python script to swap data of two variables
# n1=int(input("enter your 1st no. "))
# n2=int(input("enter your 2nd no. "))
# print("1st and 2nd no is ",n1,n2, sep=",")

# n1, n2 = n2,n1

# print("after swaping 1st no is= ",n1)
# print("after swaping 2nd no is", n2)

# # 4. Write a python script to find x power y, where values of x and y are given by user

# x=int(input("enter your x "))
# y=int(input("enter your y "))
# print(x**y)
# 5. Write a python script which takes a three digit number from the user and displays
# only its first digit.

# n=int(input("enter your no "))
# print("1st digit of no is ", n//100)
# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.

# n=int(input("enter your three digit no "))
# n=n//10
# m=n%10
# print("midle digit is ", m)
# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.
# n=int(input("enter your three digit no "))
# n=n%10
# print("last digit is ", n)
# 8. Write a python script to use IN operator to display the data present in the list
a=input("Enter anything")
print( "r"  in a  )

# 9. Write a python script to use NOT IN operator to display the data not present in list
a=input("Enter anything")
print( "r"  not in a  )
# 10. Write a python script to use IS operator to display if both variables are the same
# object or not?
a=int(input("enter 1"))
b=int(input("enter2"))
print(a is b)
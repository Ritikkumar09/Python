               #MATCH CASE

# 1. Write a python script to display the number of days in a given month number.
# m=int(input("Enter your month no"))


# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division
# print("1. for addition")
# print("2. for subtraction")
# print("3. for multiplication")
# print("4. for division")
# c=int(input("enter your choice"))
# match c:
#     case 1:
#         a, b=int(input("enter your 1st no")),int(input("enter your 2nd no"))
#         print("addition is",a+b)
#     case 2:
#         a, b=int(input("enter your 1st no")),int(input("enter your 2nd no"))
#         print("subraction is",a-b)
#     case 3:
#         a, b=int(input("enter your 1st no")),int(input("enter your 2nd no"))
#         print("multiplication",a*b) 
#     case 4:
#         a, b=int(input("enter your 1st no")),int(input("enter your 2nd no"))
#         print("division is",a/b)


        

# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.
# print("1. Check whether a given set of three numbers are lengths of an isosceles triangle or not")
# print("2. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
# print("3. Check whether a given set of three numbers are equilateral triangle or not")
# print("4. Exit.")
# c=int(input("enter your choice from above"))
# match c:
#     case 1:
#         print("enter your three sides")
#         print()
#         s1,s2,s3=int(input()),int(input()),int(input())
#         if s1==s2 or s2==s3 or s1==s3:
#             print("isosceles triangle")
#         else:
#             print("not isolated triangle")
#     case 2:
#         print("enter your three sides")
#         s1,s2,s3=int(input()),int(input()),int(input())
#         if (s1*s1+s2*s2==s3*s3) or (s1*s1+s3*s3==s2*s2) or (s2*s2+s3*s3==s1*s1):
#             print("tringle is right angled")
#         else:
#             print("tringle is not right angle")
#     case 3:
#         print("enter your three sides")
#         s1,s2,s3=int(input()),int(input()),int(input())
#         if s1==s2==s3:
#             print("tringle is equalataral")
#         else:
#             print("tringle is not equalatral")
#     case 4:
#         exit("exit")
#     case other:
#         print("invalid choice")


# 4. Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.
# age=int(input("Enter Your age:- "))
# match age:
#     case age if age<10:
#      print("It's a kid")
#     case age if age < 20:
#      print("It's a teen ")

#     case  age if age < 40:
#      print("He or she is young")

#     case age if age < 60:
#      print("He is experienced")

#     case age if age >= 60:
#      print("Senior citizen")


# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.

# num = int(input("Enter the number:- "))

# match num :
#    case num if num%2==0:
#       print("Saurabh Shukla")
#    case num if num%2!= 0 and num <0:
#       print("Prateek Jain")

#    case num if num%2!= 0 and num > 0:
#       print("Aditya Choudhary")

    
# 6. Write a python program to check whether a given string is a multiword string or single
# word string using match case statement

# srt = input("Enter the string:- ")
# match srt :
#    case str if " " in srt :
#       print("It is multi word string")
#    case other:
#       print("It's single word string")

# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement

# num=int(input("Eneter the number"))
# match num:
#    case num if num>0:
#       print(num,"Is positive")
#    case num if num<0 :
#       print(num,"is negative")
#    case other:
#       print("Number is zero")
# 8. Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement
# srt1 = input("Enter the string: ")
# srt2 = input("Enter the string")

# match (srt1,srt2):
#    case (srt1, srt2) if srt1 == srt2:
#       print("Strings are indentical")

#    case (srt1,srt2) if srt1>srt2:
#       print("String1 comes before than srting2")

#    case (srt1, srt2) if srt1<srt2:
#       print("Print string2 comes before than string1 ")



# 9. Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year
# year=int(input("enter your year"))
# match year:
#     case year if year%100==0 and year%400==0 and year%4==0:
#         print("Century leap year")
#     case year if year%100!=0 and year%400==0 and year%4==0:
#         print("Non century leap year")
#     case year if year%100!=0 and year%4!=0: 
#         print("Non century non leap year")
#     case year if year%100==0 and year%4!=0:
#         print("Century non leap year")


# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday
color=input("enter your color")
match color:
    case "Yellow":
        print("Monday")
    case "Blue":
        print("Tuesday")
    case "Orange":
        print("Wednesday")
    case "White":
        print("Thursday")
    case "Black":
        print("Friday")
    case "Red":
        print("saturday")
    case other:
        print("Sunday")
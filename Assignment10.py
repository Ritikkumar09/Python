        # FOR LOOP & RANGE
# # 1. Write a python script to print the first 10 multiples of 5.
# r1=range(int(input("enter your no")))
# for i in r1:
#     print((i+1)*5, end=' ')
# print()
# # 2. Write a python script to print first 10 multiples of N
# r1=range(10)
# n=int(input("enter your no"))
# for i in r1:
#     print((i+1)*n, end=' ')
# print()
# # 3. Write a python script to print first M multiples of N.
# m=int(input("enter your 1st no."))
# n=int(input("enter your 2nd no."))
# r1=range(m)
# for i in r1:
#     print((i+1)*n, end=' ')
# print()
# # 4. Write a python script to print the first 10 multiples of N in reverse order.
# n=int(input("enter your no for multiply"))
# r1=range(10,0,-1)
# for i in r1:
#     print(i*n, end=' ')
# print()
# # 5. Write a python script to print table of user’s choice
# n=int(input("enter your table "))
# r1=range(10)
# print("your table is= ")
# for i in r1:
#     print((i+1)*n,end=' ')
# print()
# # 6. Write a python script to print first N even natural numbers.
# n=int(input("enter your even no "))
# r1=range(2,2*(n+1),+2)
# for i in r1:
#     print(i,end=' ')
# print()


# # 7. Write a python script to print first N odd natural numbers
# n=int(input("enter your odd no "))
# r1=range(1,2*n,+2)
# for i in r1:
#     print(i,end=' ')
# print()

# # 8. Write a python script to print squares of first N natural numbers.
# n=int(input("enter your no. "))
# r1=range(n)
# for i in r1:
#     print((i+1)**2, end=' ')
# print()

# # 9. Write a python script to print cubes of first N natural numbers.
# n=int(input("enter your no. "))
# r1=range(n)
# for i in r1:
#     print((i+1)**3, end=' ')
# print()


# 10. Write a python script to display all prime numbers within a range. range start = 15, end = 45
r1=range(15, 45, 1)
for num in r1:
    for i in range(2, num,1):
      if num % i == 0:
          break
      i=i+1
    if i==num:
      print(num)

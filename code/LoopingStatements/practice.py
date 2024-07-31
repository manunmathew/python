# # print multiplication table

# n = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(f"{i} * {n} = {i*n} ")

# # total of n natural numbers

# n = int(input("Enter the number : "))
# total = 0
# for i in range(1,n+1):
#     total += i
# print(f"total of {n} natural numbers = {total} ")

# # # reverse order
# n = int(input("Enter the number: "))
# for i in range(n, 0, -1):
#     print(i)

# loop control statement
# # prime number
# n = int(input("Enter the number: "))
# if n <= 1:
#     print("Enter a number greater than 1")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"The number {n} is not a prime number")
#     else:
#         print(f"The number {n} is a prime number")

# #  Write a program to take 2 inputs from the user
# # initial range and final range
# # Then display the prime numbers fall in the range
# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# if start <= 1:
#     print("Enter a start number greater than 1")
# else:
#     print(f"The prime numbers between {start} and {end} are : ")
#     for i in range(start, end):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i, end= ",")

# Write a program to take 2 inputs from the user
# initial range and final range
# Then display the prime numbers that fall in the range

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))

# if start <= 1:
#     print("Enter a start number greater than 1")
# else:
#     print(f"The prime numbers between {start} and {end} are: ")
#     current = start

#     while current <= end:
#         if current > 1:  # Ensure we only check numbers greater than 1
#             is_prime = True
#             i = 2
#             while i * i <= current:
#                 if current % i == 0:
#                     is_prime = False
#                     break
#                 i += 1
#             if is_prime:
#                 print(current, end=", ")
#         current += 1



# # print  the series 10,20,30,40,50

#
# # print the reverse order 5000, 4000, 3000, 2000, 1000

# # write a program to find the total of first 20 odd numbers


# # write a program to print the product of first 5 natural numbers
#
# # # write a program to find the sum of both even and odd numbers fall in the range 1-20
# # ##
# # write a program to count the total number of even numbers fall in the range 1-100
# # write a program to count the number of both even and odd numbers fall in the range 1500- 3000
#
#
# # write a program to find the factorial of a number input by the user
 # Write a program to find the sum of digits of a number input by the user
# # write a program to find the product of digits of a number input by user
# # write a program to find a number is harshad or not
# For
# n= int(input("Enter the number: "))
# s = 0

# for i in str(n):
#     s += int(i)
# if n % s == 0:
#     print(f"The number {n} is Harshad")
# else:
#     print(f"The number {n} is not Harshad")

# # while
# n= int(input("Enter the number: "))
# copy = n
# s = 0
# while n > 0 :
#     digit = n % 10
#     s += digit
#     n //= 10
# if copy % s == 0:
#     print(f"The number {copy} is Harshad")
# else:
#     print(f"The number {copy} is not Harshad")


# # Harshad number: if the number is divisible by the sum of its digits
# # Write a program to find a number is Disarium or not

# n = int(input("Enter the number: "))
# s = 0
# count = 1

# for i in str(n):
#     s += int(i) ** count
#     count += 1

# if n == s:
#     print(f"The number {n} is Disarium ")
# else:
#     print(f"The number {n} is not Disarium ")

# While

# n = int(input("Enter the number: "))
# c = n
# s = 0
# count = len(str(n))

# while count > 0:
#     digi = n % 10
#     s += digi ** count
#     n //= 10
#     count -= 1

# if c == s:
#     print(f"The number {c} is Disarium ")
# else:
#     print(f"The number {c} is not Disarium ")


# # Fibonacci Numbers
# n = int(input("Enter the number: "))
# a = 0
# b = 1

# if n >= 1:
#     print(a, end=", ")
# if n >= 2:
#     print(b, end=", ")

# for i in range(2, n):
#     a, b = b, a + b
#     print(b, end=", ")

# # Fibonacci Numbers
# n = int(input("Enter the number: "))
# a = 0
# b = 1
# print(a, end= " ,")
# print(b, end= " ,")
# count = 2
# while count < n:
#     a,b = b, a+b
#     print(b, end= " ,")
#     count += 1


# write a program to print Armstrong numbers fall in the range 1-1000

# n = int(input("Enter the number: "))
# length = len(str(n))
# s = 0
# for i in str(n):
#     s += int(i) ** length
# if n == s:
#     print(f"The number {n} is an Armstrong number ")
# else:
#     print(f"The number {n} is not an Armstrong number ")

# # print pattern
# Enter the Number: 5
# * * * * *
# * * * *
# * * *
# * *
# *
# n = int(input("Enter the Number: "))

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# n = int(input("Enter the Number: "))

# for i in range(n+1):
#     for s in range(n, i, -1):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end="   ")
#     print()
# print()


# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("*", end="   ")
#     print()

# Print a diamond pattern with stars.
n = int(input("Enter the Number: "))


for i in range(n):
    for s in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()


for i in range(n - 1):
    for s in range(i + 1):
        print(" ", end="")
    for j in range(n - i - 1):
        print("* ", end="")
    print()

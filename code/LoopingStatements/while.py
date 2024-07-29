# # write a program to print first 10 natural numbers using while
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# Write a program to print first 5 even numbers


# i = 1
# while i <= 10:
#     if i%2 ==0 :
#         print(i)
#     i += 1

# i = 1
# count = 0
# while count < 5:
#     if i % 2 == 0:
#         print(i)
#         count += 1
#     i += 1
# write a program to print first 20 odd numbers
# i = 1
# count = 1
# while count <= 20:
#     if i % 2 != 0:
#         print(i)
#         count += 1
#     i += 1
# i = 1
# while i <= 40:
#     print(i)
#     i += 2
# # write a program to find the sum of first 10 natural numbers
#
# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
# print(sum)

# # write a program to print the sum of both even and odd between the range 1 to 100
#
# i = 1
# even = 0
# odd = 0
# while (i <= 100):
#     if i%2 ==0 :
#         even += i
#     else:
#         odd += i
#     i += 1
# print(f"Sum of even numbers = {even} ")
# print(f"Sum of odd numbers = {odd} ")

# write a program to find the product of first 5 even numbers

# i = 1
# product = 1
# count = 1
# while count <= 5 :
#     if i % 2 == 0:
#         product *= i
#         count += 1
#     i += 1
# print("The product of the first 5 even numbers is:", product)

# # generate multiplication table of a number input by the user
#
# n = int(input("Enter the number: "))
# i = 1
#
# while (i <= 10):
#     print (f"{i}*{n} = {n*i}")
#     i += 1
#
# # find the factorial of a number
# n = int(input("Enter the number: "))
# i = 1
# factorial = 1
# while (i <= n ):
#     factorial *= i
#     i += 1
# print(f"Factorial of the number {n} is {factorial}")

# print the series in revers order

# numbers = [10, 20, 30, 40, 50]
# i = len(numbers) - 1
# while i >= 0:
#     print(numbers[i])
#     i -= 1

#
# i = 10
# while i >= 1:
#     print(i, end=' ')
#     i -= 1
# print()
#print() is called to move to the next line after the loop completes.
# write program to find reverse of a number input by the user
#
# n = int(input("Enter the number: "))
# rev = 0
# while n > 0 :
#     rem = n % 10
#     rev = rev * 10 + rem
#     n //= 10
# print ("The reverse of the number is: ", rev)
# # write a program to check a number is Deserium or not without using len
# n = int(input("Enter the number: "))
# copy = n
# sum = 0
#
# cn = n
# count = 0
# while cn >0 :
#     cn //= 10
#     count += 1
# while n > 0 :
#     rem = n % 10
#     sum += rem ** count
#     count -= 1
#     n //= 10
# if sum == copy:
#     print(f"{copy} is a Deserium number.")
# else:
#     print(f"{copy} is not a Deserium number.")

# # check a number is palindrome or not user input
#
# n = int(input("Enter the number: "))
# copy = n
# rev = 0
# while n > 0 :
#     rem = n % 10
#     rev = rev * 10 + rem
#     n //= 10
# if copy == rev:
#     print(f"{copy} is a Palindromic number.")
# else:
#     print(f"{copy} is not a Palindromic number.")
# # check a number is Harshad or not

# n = int(input("Enter the number: "))
# sum = 0
# copy = n
# while n > 0:
#     rem = n % 10
#     sum =+ rem
#     n //= 10
#
# if copy % sum == 0:
#     print(f"{copy} is a Harshad number.")
# else:
#     print(f"{copy} is not a Harshad number.")

# #  Armstrong Numbers
# n = int(input("Enter the number: "))
# copy = n
# sum = 0
# len = len(str(n))
# while n > 0 :
#     rem = n % 10
#     sum += rem ** len
#     n //= 10
# if sum == copy:
#     print(f"{copy} is a Armstrong number.")
# else:
#     print(f"{copy} is not a Armstrong number.")
# Fibonacci Numbers
# num = int(input("Enter the number of Fibonacci numbers to generate: "))
# a,b = 0,1
# print(a)
# print(b)
# count = 2
# while count < num :
#     c = a + b
#     print(c)
#     a = b
#     b = c
#     count += 1


#write a program to enter the numbers till the user input zero or negative value and at the end it should display the sum of positive entered by the user
# sum = 0
# while True :
#     n = int(input("Enter the number: "))
#     if n <= 0:
#         break
#     sum += n
# print(f"The sum of positive numbers entered is: {sum}")

# write a program to take input from the user till the user input 0 and at the end it should display the count of even numbers and odd numbers

even = 0
odd = 0
while True :
    n = int(input("Enter the number: "))
    if n == 0:
        break
    elif n %2 == 0:
        even += 1
    else:
        odd += 1
print(f"number of even numbers: {even}")
print(f"number of odd numbers: {odd}")


# write a program to print Armstrong numbers fall in the range 1-1000


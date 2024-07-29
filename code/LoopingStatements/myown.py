# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     scores = list(arr)
#     maxscore = max(scores)
#     scores_without_max = []
#     for score in scores:
#         if score != maxscore:
#             scores_without_max.append(score)
#     runner_up = max(scores_without_max)
#     print("Runner up is", runner_up)

# def split_and_join(line):
#     # write your code here

#  if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
#
# Write a program that calculates the sum of all even numbers between two numbers entered by the user using a for loop.

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# sum = 0
# for i in range(start, end+1):
#     if i %2 == 0 :
#         sum += i
# print(f"The sum of all even numbers is {sum}")


# # Write a program that takes a number as input from the user and checks if it is a prime number using a while loop.

# num = int(input("Enter the number: "))
# i = 2
# if num <= 1 :
#     print("Enter a natural number greater than 1")
# else:
#     while i*i <= num :
#         if num %i == 0:
#           print (f"{num} is not a prime number")
#           break
#         i += 1
#     else:
#         print (f"{num} is a prime number")

# # Write a program that calculates the factorial of a number entered by the user using a for loop and displays the result.

# n = int(input("Enter the number: "))
# product = 1
# for i in range(1, n+1):
#     product *= i
# print(f"Factorial of the number {n} is {product} ")


# # Write a program that prints the multiplication table of a number entered by the user, using a for loop.

# n = int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{i} * {n} = {i * n}")

# Write a program that takes a string input from the user and counts the number of vowels in the string using a for loop and conditional statements.

# s = input("Enter the string: ")
# count = 0
# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# for i in s:
#     if i in vowels:
#         count += 1
# print(f"Number of vowels in the string is {count}")

# # Write a program that takes a integer input from the user and checks if it is a palindrome using a while loop.
# n = int(input("Enter the number: "))
# copy = n
# rev = 0
# while n > 0 :
#     rem = n % 10
#     rev = rev *10 + rem
#     n //= 10
# print(rev)

# if copy == rev:
#     print(f"{copy} is a Palindromic number.")
# else:
#     print(f"{copy} is not a Palindromic number.")

# # Write a program that takes a number as input from the user and calculates its square root
# n = int(input("Enter the number: "))
# print(f"Square root of {n} is {n ** 0.5} ")

# Write a program that takes a number as input from the user and prints all its factors using while.

# n = int(input("Enter the number: "))
# print(f"Factors of {n} are:", end=" ")
# i = 1
# while  i <= n:
#     if n % i == 0:
#         print(i, end=", ")
#     i += 1
# print()


# # Write a program that takes a number as input from the user and prints all its factors using for loop.

# n = int(input("Enter the number: "))
# print(f"Factors of {n} are:", end=" ")

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=", ")
# print()

# # Write a program that takes two numbers as input from the user and calculates their Greatest Common Divisor (GCD) using a while loop.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# a = num1
# b = num2

# while b != 0 :
#     a , b = b, a % b
# print(f"The Greatest Common Divisor (GCD) of {num1} and {num2} is {a}")

# Write a program that takes a year as input from the user and checks if it is a leap year using conditional statements.

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


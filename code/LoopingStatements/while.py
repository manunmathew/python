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

numbers = [10, 20, 30, 40, 50]
i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i -= 1




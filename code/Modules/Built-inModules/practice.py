# Task

# You are given a date. Your task is to find what the day is on that date.

# Input Format

# A single line of input containing the space separated month, day and year, respectively, in  MM DD YYYY  format.

# import datetime


# date_input = input ("Enter the date in  MM DD YYYY format: ")

# month, day, year = map(int, date_input.split())

# mydate = datetime.date(year, month, day)
# day = (mydate.strftime("%A")).upper()
# print(day)

# def fibonacci(n):
#     # return a list of fibonacci numbers
#     numbers = []
#     a = 0
#     b = 1
#     for i in range(n):
#         numbers.append(a)
#         a, b = b, a + b
#     return numbers

# n = int(input())
# cube = list(map(lambda x: x**3, fibonacci(n)))
# print(cube)

# Write a Python program that takes a list of integers, filters out the odd numbers using filter, squares the remaining even numbers using map, and then sums them using reduce and lambda.

from functools import reduce
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = list(filter(lambda x: x%2 ==0, li))
print(x)
y = list(map(lambda i: i**2, x))
print(y)
z = reduce(lambda i, j : i + j, y)
print(z)

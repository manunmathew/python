x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Product of 3 arguments
x = lambda a, b, c : a * b * c
print(x(5, 6, 1))
# Square of an argument
x = lambda a : a ** 2
print(x(5))
# Cube of an argument
x = lambda a : a ** 3
print(x(5))
# Area of a circle
x = lambda r : 3.14 * r**2
print(x(5))
# Area of a triangle
x = lambda b, h : 0.5 * b * h
print(x(5,8))

# find the largest of 2 numbers
x = lambda a, b : a if (a >b ) else b
print(x(1,3))

# write program to check a number odd or even using lambda
x = lambda a: f"{a} is even" if a % 2 == 0 else f"{a} is odd"
print(x(3))
# check a number is positive or negative
x = lambda a: "positive" if a > 0 else "negative"
print(x(0))
# find a square of a number if the number is greater than zero or print None
x = lambda a : a ** 2 if a > 0 else "None"
print(x(3))
# convert a positive number to negative and a negative number to positive using lambda
x = lambda a: a * -1
print(x(3))

# check a number is positive or negative
x = lambda a: "positive" if a > 0 else ("zero" if (a == 0) else "negative")
print(x(3))

# Find the min of 3 values
x = lambda a, b, c: a if (a < b and a < c) else (b if b < c else c)
print(x(5, 8, 3))


# Find the max of 3 values
x = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)
print(x(5, 8, 3))

# write a program to find the max of 4 numbers
x = lambda a, b, c, d: a if (a > b and a > c and a > d) else (b if b > c and b > d else (c if c > d else d))
print(x(10, 11, 12, 13))

# write a program to find min of 5 numbers
x = lambda a, b, c, d, e: a if (a < b and a < c and a < d and a < e) else (b if (b < c and b < d and b < e) else (c if (c < d and c < e) else (d if (d < e) else e)))

print(x(5, 6, 7, 8, 9))



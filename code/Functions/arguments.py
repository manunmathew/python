# Positional Arguments

def add(a, b):
    print(a + b)

add(a = 1, b = 2)

# create a function product an pass three arguments into the function and print the product value

def product (a, b, c):
    print(a * b * c)

product(1,2,3)

# create a function odd_even() and pass 1 argument into a function and check whether it is odd or even.

def odd_even(a):
    if a % 2 == 0:
        print(f"{a} is an even number")
    else:
        print(f"{a} is an even number")

odd_even(8)

# find factorial of a number using function with argument

def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    print(f"factorial of the number { a } is { fact } ")

factorial(8)


# create quadratic equation solver using function with arguments

# Quadratic formula:
# x = (-b ± √(b^2 - 4ac)) / (2a)

def quadratic(a,b,c):
    z = (b**2) - (4 * a * c)
    x1 = (-b + z**0.5) / (2*a)
    x2 = (-b - z**0.5) / (2*a)

    print(f"quadratic value is { x1 }, { x2 } ")

quadratic(1, 5, 6)

# solve area of circle
def area_of_circle(radius):
    area = 3.14 * (radius ** 2)
    print(f"The area of the circle with radius {radius} is {area}")

area_of_circle(5)

# solve area of triangle

def area_of_triangle(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle with base {base} and height {height} is {area}")

area_of_triangle(10, 5)


# check a number is Deserium or not using function

def deserium(n):
    s = 0
    c = 1
    for i in str(n):
        s += int(i)**c
        c += 1
    if s == n:
        print(f"The number {n} is Deserium ")
    else:
        print(f"The number {n} is not a Deserium ")
deserium(135)

# check a number is Harshad or not using function

def harshad(n):
    s = 0
    for i in str(n):
        s += int(i)
    if n % s == 0:
        print(f"The number {n} is a Harshad number")
    else:
        print(f"The number {n} is not a Harshad number")

harshad(21)


# # generate fibinocci series

def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series:", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci(10)

# sum of digit of a number

def sum_of_digit (n):
    s = 0
    for i in str(n):
        s += int(i)
    print(f"The sum of digit of  {n} is {s}")

sum_of_digit(219)

# reverse of a number

def reve(n):
    rev =str(n)[::-1]
    print("".join(rev))

reve(219)

# Arbitrary Arguments,

def num(*a):
    print(type(a))
    print(a)
num(1,2,3,4,5,"b")

# create a function sum of numbers  that take any number of arguments and returns sum of the numbers

def sum(*a):
    s = 0
    for i in a:
        s += int(i)
    print(s)
sum(1,2,3,4,5)

# 1. create a function product_of_num
def product_of_num(*a):
    p = 1
    for i in a:
        p *= int(i)
    print(p)
product_of_num(1,2,3,4,5)

# 2. create a function min_value
def min_value(*a):
    min = a[0]
    for i in a:
        if i < min :
            min = i
    print(min)
min_value(1,2,3,4,5)


# 3. create a function max_value
def max_value(*a):
    max = a[0]
    for i in a:
        if i > max :
            max = i
    print(max)

max_value(1,2,3,4,5)
# 4. create a function that take any number of arguments and returns the sum of even numbers.

def sum_of_even(*a):
    s = 0
    for i in a:
        if i % 2 == 0:
            s += int(i)
    print(s)

sum_of_even(1, 2, 3, 4, 5)

# 5. create a function that take any number of arguments and returns two lists fist list of even and second list of odd

def even_odd(*a):
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)

even_odd(1, 2, 3, 4, 5)

# 6. create a function that takes strings and numbers it should return a dictionary with its type as value

def type_of(*a):
    type_dict = {}
    for i in a:
        if type(i) == int:
            type_dict[i] = "int"
        else:
            type_dict[i] = "str"
    print(type_dict)

type_of(1, 2, 3, 4, 5, "a", "b")




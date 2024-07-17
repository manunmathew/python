write a program to to add two numbers input by user

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Answer=", a+b)
print(f"")
sum = a+b
print("Answeer =", sum)

find the product, division , exponent, floor division of two number input by the user


product=
exponent
floor division
reminder
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
product = a * b
division = a / b
#exponent = a ** b
floor_division = a // b
remainder = a % b
print(f"Product = {product}")
print(f"Division = {division}")
print(f"Exponent = {exponent}")
print(f"Floor Division = {floor_division}")
print(f"Remainder = {remainder}")

write a program to find a the square of a number input by the use
Enter a number:
Square of 2 is 4

a = int(input("Enter a number: "))
square = a ** 2
print(f"Square of {a} is {square}")

write a program to find cube of a number
find area of circle, input radius
find area of triangle 1/2 bh
find square root of a number  (** 0.5)
find the last digit of the number input by user (divided by 10)

# write a program to find cube of a number
number = int(input("Enter a number to find its cube: "))
cube = number ** 3
print(f"Cube of {number} is {cube}")

# find area of circle, input radius
radius = float(input("Enter the radius of the circle: "))
circle = 3.14 * radius ** 2
print(f"Area of the circle with radius {radius} is {circle}")

# find area of triangle (1/2 bh)
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle = 0.5 * base * height
print(f"Area of the triangle with base {base} and height {height} is {triangle}")

# find square root of a number  (** 0.5)
square_number = int(input("Enter a number to find its square root: "))
square_root = square_number ** 0.5
print(f"Square root of {square_number} is {square_root}")

# find the last digit of the number input by user (divided by 10)
Last_number = int(input("Enter a number to find its last digit: "))
last_digit = Last_number % 10
print(f"The last digit of {Last_number} is {last_digit}")

#quadratic equation solving

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

d = (b**2 -4*a*c)**0.5
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)

print(x1)
print(x2)

#a =1, b = 5 , c = 6

comparison

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"a equal to b: {a==b}")
print(f"a greater than b: {a>b}")
print(f"a less than b: {a<b}")
print(f"a greater than or equal to b: {a>=b}")
print(f"a less than or equal to b: {a<=b}")
print(f"a not equal to b: {a!=b}")



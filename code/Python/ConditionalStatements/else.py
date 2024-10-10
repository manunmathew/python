# take alphabet from user and it should print vowel if the user input a,e,i,o,u

a = input("Enter the alphabet: ")
vowel = ['a', 'e' , 'i', 'o', 'u']
if (a in vowel):
   print("Vowel")
else:
   print("Not a vowel")

# Write a program to find the largest of 2 number input by the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if (a >b):
    print(a, " is greater")
else:
    print(b, " is greater")

# Write a program to find the smallest of 2 number input by the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if (a < b):
    print(a, " is smallest")
else:
    print(b, " is smallest")


# write a program to check a number is odd or even

# even = num%2 == 0
# odd = num%2 != 0 | num%2==1
a = int(input("Enter the number: "))
if (a%2==0):
    print(a, " is even number")
else:
    print(a, " is odd number")
# write a program to check the number is divisible of 5

a = int(input("Enter the number: "))
if (a%5==0):
    print(a, " is divisible of 5")
else:
    print(a, " is not divisible of 5")


# Write a program to check the number is divisible by both 2 and 3 else

a = int(input("Enter the number: "))
if (a%2==0 and a%3==0 ):
    print(a, " is divisible by both 2 and 3")
else:
    print(a, " is not divisible by both 2 and 3")

# eligible for vote

age = float(input("Enter your age : "))
if (age>= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# determine if a year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

print(leap)

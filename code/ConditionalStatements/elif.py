# # Write a program to find the largest of 3 numbers input by the user
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if (a > b and a > c):
#     print(a, " is largest")
# elif (b > a and b > c):
#     print(b, " is largest")
# else:
#     print(c, " is largest")
#
#
# # Write a program to find the largest of 3 numbers input by the user
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if (a > b and a > c):
#     print(a, " is largest")
# elif (b > c):
#     print(b, " is largest")
# else:
#     print(c, " is largest")

# input 5 subject mark, total mark , % mark , 90 a, 80 b


# physics = int(input("Enter the marks for Physics : "))
# chemistry = int(input("Enter the marks for Chemistry : "))
# maths = int(input("Enter the marks for Maths : "))
# english = int(input("Enter the marks for English : "))
# computer = int(input("Enter the marks for Computer : "))
# total = physics+chemistry+maths+english+computer
# percentage = (total/500)*100
# print("Total Marks =", total)
# print("Percentage =", percentage)
# if (percentage >= 90):
#     print("A Grade")
# elif (percentage >= 80):
#     print("B Grade")
# elif (percentage >= 70):
#     print("C Grade")
# elif (percentage >= 60):
#     print("D Grade")
# else:
#     print("Failed")
# # Accept the age of 4 persons display the youngest one
# # Accept the name and age from user
#
# n1 = input("Enter the name of fist person: ")
# a = int(input(f"Enter the age of {n1}: "))
# n2 = input("Enter the name of second person: ")
# b = int(input(f"Enter the age of {n2}: "))
# n3 = input("Enter the name of third person: ")
# c = int(input(f"Enter the age of {n3}: "))
# n4 = input("Enter the name of fourth person: ")
# d = int(input(f"Enter the age of {n4}: "))
# if (a < b and a < c and a < d ):
#     print(n1, " is youngest")
# elif (b < c and b < d):
#     print(n2, " is youngest")
# elif (c < d ):
#     print(n3, " is youngest")
# else:
#     print(4, " is youngest")
# Write a program to check whether the last digit of a number is divisible by 3

# a = int(input("Enter the number: "))
# d = a%10
# if (d%3==0):
#     print(d, " is divisible by 3")
# else:
#     print(d, " is not divisible by 3")
# Write a program to accept the cost price of a bike and
# display the road tax to be paid according to the following criteria
# cost price  above 100000  tax 15%
# cost price  50000 and <= 100000  10 %
#50000 <= 5%

# a = int(input("Enter the bike cost price: "))
# if (a > 100000):
#      print("Road tax = ", a*(15/100))
# elif (a > 50000 and a <= 100000):
#     print("Road tax = ", a*(10/100))
# else:
#     print("Road tax = ", a*(5/100))

#
a = int(input("Enter the Salary: "))
n = int(input("Enter the number of years service: "))
if (n > 10):
     print("Bonus Amount = ", a*(10/100))
elif (n >= 6 and n <= 10):
    print("Bonus Amount =  ", a*(8/100))
else:
    print("Bonus Amount =  ", a*(5/100))

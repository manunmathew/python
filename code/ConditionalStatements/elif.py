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


# Write a program to find the largest of 3 numbers input by the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if (a > b and a > c):
    print(a, " is largest")
elif (b > c):
    print(b, " is largest")
else:
    print(c, " is largest")

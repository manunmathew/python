# 1. How to count the number of upper and lowercase letters in a string
mystring = input("Enter the String: ")

lowercase = 0
uppercase = 0

for i in mystring:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    else:
        print(f"'{i}' is not an alphabet")

print(f"Number of uppercase letters is: {uppercase}")
print(f"Number of lowercase letters is: {lowercase}")


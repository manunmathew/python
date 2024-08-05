 # find the count of upper case letter and lower case letter in a string input by the user
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


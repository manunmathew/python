 # input a string from user and find the number of integer and alphabet in the string
mystring = input("Enter the String: ")

integer = 0
alphabet = 0

for i in mystring:
    if i.isnumeric():
        integer += 1
    elif i.isalpha():
        alphabet += 1
    else:
        print(f"'{i}' is not an alphabet")

print(f"Number of integers  is: {integer}")
print(f"Number of alphabet  is: {alphabet}")


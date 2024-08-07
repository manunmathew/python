# 1. create given dictionary using user input
#    {"emp_name": "Alen", "Company": "tcs", "designation": "Tester"}

# mydict = {}
# n = int(input("Enter number of Keys Values: "))
# for i in range(n):
#     key = input("enter the key")
#     value=input ("enter the value")
#     mydict.update({key:value})
# print(mydict)
#
# create dictionary
# {"student_id": 1, "Name": "Manu", "Reg_Num": 122344, "Phone" : 98678}
# mydict = {}
# n = int(input("Enter number of Keys Values: "))
# for i in range(n):
#     key = input("Enter the key: ")
#     value = input("Enter the value: ")
#     if value.isnumeric():
#         mydict.update({key: int(value)})
#     else:
#         mydict.update({key: value})
# print(mydict)

# create dictionary
# user input only key .. value should be length of key .. without len function

# mydict = {}
# n = int(input("Enter number of Keys : "))
# for i in range(n):
#     key = input("Enter the key: ")
#     length = 0
#     for i in key:
#         length += 1
#     mydict.update({key: length})
# print(mydict)
# create dictionary
# 1. input numbers from user and display the number is either even or odd {1: odd}

# mydict = {}
# n = int(input("Enter number of Keys: "))
# for i in range(n):
#     key = int(input("Enter the Number: "))
#     if key % 2 == 0:
#         mydict.update({key: "even"})
#     else:
#         mydict.update({key: "odd"})
# print(mydict)

# create dictionary
# 2. input numbers from user and display the numbers and their factorials

# mydict = {}
# n = int(input("Enter number of Keys: "))
# for i in range(n):
#     key = int(input("Enter the Number: "))
#     factorial = 1
#     for j in range(1, key + 1):
#         factorial *= j
#     mydict.update({key: factorial})
# print(mydict)

# # create dictionary
# # 3. input string from user and display the strings and their reverses
# mydict = {}
# n = int(input("Enter number of Keys: "))
# for i in range(n):
#     key = input("Enter the String: ")
#     reversed_string = key[::-1]
#     mydict.update({key: reversed_string})
# print(mydict)
# Calculate the bonus for each employee based on their performance score:
# If the score is 90 or above, the bonus is 20% of the score.
# If the score is between 80 and 89, the bonus is 10% of the score.
# If the score is below 80, there is no bonus.

n = int(input("Enter number of employees: "))
mydict = {}
for i in range(n):
    key = input("Employee Name: ")
    value = input("Employee Performance score: ")
    mydict[key] = value
sorted_dict = list(dict(sorted(mydict.items())))
for i in range(len(sorted_dict)):
    if int(sorted_dict[i[1]]) > 20 :



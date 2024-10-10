# import re

# rule = r'[a-z\s]+'  # r is raw string to avoid escape error
# name = input("Enter your name: ")
# match = re.fullmatch(rule, name)
# print(match)
# if match:
#     print("Name is valid")
# else:
#     print("Invalid")


# input name from user that can include both upper case and lower case letters with limit of 5

# import re

# rule = '[a-zA-z]{5}'
# word = input("Enter the Word: ")
# match = re.fullmatch(rule, word)

# if match:
#     print("Word is valid")
# else:
#     print("Invalid")

# input username that can include both upper and lower case  , space and number  and limit range from 5 to 8

# import re

# rule = r'[a-zA-Z0-9\s]{5,8}'

# UserName = input("Enter the User Name: ")
# match = re.fullmatch(rule, UserName)

# if match:
#     print("User Name is valid")
# else:
#     print("Invalid User Name")


# Name should start with upper case followed by lowercase  total limit of name is 5 to 8
# import re

# rule = '[A-Z][a-z]{4,7}'

# UserName = input("Enter the User Name: ")
# match = re.fullmatch(rule, UserName)

# if match:
#     print("User Name is valid")
# else:
#     print("Invalid User Name")


# the  name should only start with  uppercase A, B, or C
# followed by lower case, number should be included or not

# import re

# rule = '[ABC][a-z]+[0-9]*'

# UserName = input("Enter the User Name: ")
# match = re.fullmatch(rule, UserName)

# if match:
#     print("User Name is valid")
# else:
#     print("Invalid User Name")

# start with +91 .. then number should start with (987) total 10

import re

rule = '[+][9][1][987]{1}[0-9]{9}'

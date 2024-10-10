# String Operations in Python

# Define a string
x = "python programming"

# Indexing examples
first_char = x[0]
print("First character:", first_char)  # prints 'p'

second_char = x[1]
print("Second character:", second_char)  # prints 'y'

substring_0_15 = x[0:15]
print("Substring (0 to 14):", substring_0_15)  # prints 'python program'

last_char = x[-1]
print("Last character:", last_char)  # prints 'g'

substring_neg10_neg1 = x[-10:-1]
print("Substring (-10 to -2):", substring_neg10_neg1)  # prints 'rogrammin'

# Note: The slicing x[-1: -10] will result in an empty string because the start index is greater than the end index
substring_neg1_neg10 = x[-1: -10]
print("Substring (-1 to -10):", substring_neg1_neg10)  # prints ''

# String Methods
print("Upper case:", x.upper())  # converts to upper case: 'PYTHON PROGRAMMING'
print("Lower case:", x.lower())  # converts to lower case: 'python programming'
print("Title case:", x.title())  # converts to title case: 'Python Programming'
print("Swap case:", x.swapcase())  # swaps the case: 'PYTHON PROGRAMMING'
print("Capitalized:", x.capitalize())  # capitalizes the first letter: 'Python programming'

# Define another string
x = "123@"

# Boolean checks
print("Is upper:", x.isupper())  # checks if all characters are upper case: False
print("Is lower:", x.islower())  # checks if all characters are lower case: False
print("Is alpha:", x.isalpha())  # checks if all characters are alphabetic: False
print("Is numeric:", x.isnumeric())  # checks if all characters are numeric: False
print("Is alphanumeric:", x.isalnum())  # checks if all characters are alphanumeric: False

# Define another string
x = "find string in a paragraph in in"

# Finding substrings
print("First occurrence of 'in':", x.find("in"))  # finds the first occurrence of 'in': 5
print("First occurrence of 'hello':", x.find("hello"))  # returns -1 as 'hello' is not found
print("Index of 'in':", x.index("in"))  # finds the first occurrence of 'in': 5

# The following line will raise a ValueError if uncommented because 'hello' is not found in the string
# print("Index of 'hello':", x.index("hello"))  # raises ValueError as 'hello' is not found

print("Last occurrence of 'in':", x.rfind("in"))  # finds the last occurrence of 'in': 31
print("Last occurrence of 'hello':", x.rfind("hello"))  # returns -1 as 'hello' is not found
print("Count of 'in':", x.count("in"))  # counts the occurrences of 'in': 4

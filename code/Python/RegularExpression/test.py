import re
# # 1. Validate a postal code: Write a rege to validate a 5-digit US postal code using fullmatch)
# # (e.g., "12345" should match, but "1234a" or "12345-6789" should not).
# rule = r'[\d]{5}'

# postal_code = input("Enter the postal code: ")
# match = re.fullmatch(rule, postal_code)

# if match:
#     print(f"{postal_code} is a valid US postal code.")
# else:
#     print(f"{postal_code} is not a valid US postal code.")




# # 2. Check for digits only: Write a regex pattern to validate that a string contains only digits using fullmatch().

# rule = r'[\d]+'

# string = input("Enter the string containing only digits: ")
# match = re.fullmatch(rule, string)

# if match:
#     print(f"{string} is a valid string containing only digits.")
# else:
#     print(f"{string} is not a valid string containing only digits.")


# 3. Match a valid date in YYYY-MM-DD format: Ensure the string matches a date format using fullmatch). The valid format is YYYY-MM-DD.


rule = r'[0-9]{4}[-](0[1-9]|1[0-2])[-](0[1-9]|[1-2]\d|3[01])'

date_input = input("Enter the date in YYYY-MM-DD format: ")
match = re.fullmatch(rule, date_input)

if match:
    print(f"{date_input} is a valid date in YYYY-MM-DD format.")
else:
    print(f"{date_input} is not a valid date in YYYY-MM-DD format.")

# 4. Starts with a letter.
# Can contain only letters, digits, underscores, and hyphens.
# Is between 3 and 16 characters long.

# rule = r'[a-zA-Z][a-zA-Z0-9_-]{2,15}'

# username = input("Enter the string to validate: ")
# match = re.fullmatch(rule, username)

# if match:
#     print(f"{username} is a valid string.")
# else:
#     print(f"{username} is not a valid string.")

# # 5. Write a regex using fullmatch) to check if a string represents a valid hexadecimal color code (e.g., #FF5733).

# rule = r'[#][0-9A-Fa-f]{6}'

# color_code = input("Enter the hexadecimal color code: ")
# match = re.fullmatch(rule, color_code)

# if match:
#     print(f"{color_code} is a valid hexadecimal color code.")
# else:
#     print(f"{color_code} is not a valid hexadecimal color code.")

# # 6. Write a regex using fullmatch) to check if a string represents a valid hexadecimal color code (e.g., #FF5733).
# # 7. Match a valid email address: Use fullmatch() to validate an email address. The pattern should match:
# # A username consisting of letters, digits, underscores
# # An @ symbol.
# # Ends with gmail.com

# rule = r'[a-z][a-zA-Z0-9_]+@gmail[.]com'

# email = input("Enter the email address: ")
# match = re.fullmatch(rule, email)

# if match:
#     print(f"{email} is a valid Gmail address.")
# else:
#     print(f"{email} is not a valid Gmail address.")

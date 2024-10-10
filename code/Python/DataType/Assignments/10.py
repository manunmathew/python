#  # Remove space from a string input by user
# s = input("Enter a string: ")

# rmspaces = s.replace(" ", "")

# print(f"String without spaces: '{rmspaces}'")

s = input("Enter a string: ")
new = ""
for i in s:
    if i != " ":
        new += i
print(new)

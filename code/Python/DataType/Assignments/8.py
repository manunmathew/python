 # Check a string input by the user is palindrome or not

s = input("Enter a string: ")
revstr = ""
for i in range(len(s) - 1, -1, -1):
    revstr += s[i]
print(revstr)
if s == revstr:
    print(f"The string {s} is a palindrome.")
else:
    print(f"The string {s} is not a palindrome.")

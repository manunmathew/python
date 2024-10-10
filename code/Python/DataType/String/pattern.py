# s = "python"

# x =""
# for i in s:
#     x += i
#     print(x)
# for i in s:

mystring = input("Enter the String: ")

x = 0
for i in mystring:
    x += 1
    print(mystring[0:x])
for i in mystring:
    x -= 1
    print(mystring[0:x])

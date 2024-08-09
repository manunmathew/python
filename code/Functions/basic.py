# # syntax
# def function_name():
#     print("Hello from the first function")

# function_name()

# # create functions , add , multiply, subtact,  div
# #  add
# def add():
#     a = input("first number: ")
#     b = input("second number: ")
#     print(a+b)
# #  multiply
# def multiply():
#     a = input("first number: ")
#     b = input("second number: ")
#     print (a * b)

# #  subtract
# def subtract():
#     a = input("first number: ")
#     b = input("second number: ")
#     print (a - b)

# # divide
# def divide():
#     a = input("first number: ")
#     b = input("second number: ")
#     print (a / b)


# add()
# multiply()
# subtract()
# divide()


# function variable
## global
# count = 1

# def increment():
#     global count
#     count += 1
#     print(count)
# increment()

# print(count)

## local
def first():
    count = 1
    count += 1
    print(count)
first()

print(count) # can not access outside the function as it is local variable.

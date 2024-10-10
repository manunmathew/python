# try:
#     num = int(input("Enter a number"))
#     if num >= 1 and num <= 10:
#         print("Success")
#     else:
#         raise Exception

# except Exception:
# 	print("Please input a number between 1 and 10")


# try:
#     num = int(input("Enter the Age"))
#     if num >= 18:
#         print("Eligible")
#     else:
#         raise ValueError("Please enter age greater than 18")

# except ValueError as e:
#     print(e)
#     print(type(e))


# write a function verify age that take an integer value age as input. if the age is below zero raise a value error with the message "Age cannot be negative" if the age is greater than 12o raise an OverflowError message Age exceeds human limits. for a valid age print the message age is Valid

# def validate_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     elif age > 120:
#         raise OverflowError("Age exceeds human limits")
#     else:
#         print("Age is Valid")


# try:
#     age = int(input("Enter the Age: "))
#     validate_age(age)
# except (ValueError, OverflowError) as e:
#     print(e)

# write a function safe_divide that takes two numbers a and b if b is zero raise a zero division error with message , cannot divide by zero.if either a or b is not a number raise a type TypeError with message both argument bust be number .. else return the result a/b


def safe_divide(a, b):
    if not a.isdigit() or not b.isdigit():
        raise TypeError("Both arguments must be Numbers")
    elif int(b) == 0:
        raise ZeroDivisionError("Cannot divide by Zero")
    else:
        return int(a)/int(b)


try:
    a = input("First Number: ")
    b = input("Second Number: ")
    result = safe_divide(a, b)
    print(f"Result: {result}")
except (ZeroDivisionError, TypeError) as e:
    print(e)



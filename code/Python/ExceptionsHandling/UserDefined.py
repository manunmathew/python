#In users can define a custom exception by creating new class
#this exception clases to be derived either directly or indirectly from the build in exeption class


class NegativeError(Exception):
    pass
class ZeroError(Exception):
    pass
try:
    num = int(input("Enter the number: "))
    if num == 0:
        raise ZeroError("Zero error raised")
    elif num < 0:
        raise NegativeError("Negative Error raised")
    else:
        print("Success")
except (ZeroError, NegativeError) as e:
    print(e)

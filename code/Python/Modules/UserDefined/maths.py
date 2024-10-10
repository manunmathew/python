# function with return
# create a function add() that takes any number of arguments
# quartic solver
#numreverse
#quadratic_solver()
#num_reverse()

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def num_reverse(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

def quadratic_solver(a, b, c):
    y = ((b**2) - (4*a*c)) ** 0.5
    x1 = (-b + y) / (2*a)
    x2 = (-b - y) / (2*a)
    return x1,x2

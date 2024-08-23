# filter()

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = list(filter(lambda j: j % 2 == 0, li))
print(x)  # Output: [2, 4, 6, 8]


# filter negative number from the given list

li = [-1,0,2,-2,3,4]
x = list(filter(lambda i: i < 0, li))
print(x)
# filter vowels from user input

# s = input()
# vowels = "aeiouAEIOU"
# x = list(filter(lambda k: k in vowels, s))
# print(x)



# from the list filter out numbers which is divisible by 2 but not by 3 using lambda

li = [1,2,3,4,5,6,7,8,9,10]
x = list(filter(lambda m: (m % 2==0) and (m %3 != 0), li))
print(x)

# map()
# find the  square of numbers
li = [1, 2, 3, 4, 5]
x = list(map(lambda l: l**2, li))
print(x)

# using lambda map convert the first char of each strings into upper case?
words = ["welcome", "hello", "python"]
x = list(map(lambda o: o.capitalize(), words))
print(x)

# using lambda map print the reverse of each words in a list passing into a function

words = ["welcome", "hello", "python"]
x = list(map(lambda p: p[::-1], words))
print(x)

from functools import reduce


#find the product of the given list ?
li = [1,2,3,4,5]
x = reduce(lambda a,b : a+b , li)
print (x)
#find the min value from the given list
li = [5,3,1,2,3,4,5]
x = reduce(lambda a,b : a if a < b else b, li)
print (x)
# Find the max value

li = [8,3,1,2,3,4,5]
x = reduce(lambda a,b : b if a < b else a, li)
print (x)

def print_fibonacci(n, a=0, b=1):
    # Base case: if n is 0, stop the recursion
    if n == 0:
        return
    # Print the current Fibonacci number
    print(a, end=' ')
    # Recursive case: call the function with updated values
    print_fibonacci(n - 1, b, a + b)

# Example usage: print the first 10 Fibonacci numbers
print_fibonacci(0)

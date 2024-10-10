def my_function(x):
  return 5 * x

print(my_function(3))


# find square of a number passing into a function using function with return type
# def square(num):
#     return num* num

# print(square(5))

def square(num):
    return num* num
result = square(5)
print(f"The square of 5 is: {result}")

#1. find the min of 2 numbers passing into a function?
def find_min(a, b):
    if a < b:
        return a
    else:
        return b
result = find_min(10, 20)
print(f"The min number is : {result}")

#2. count the no: of vowels in a string ?
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"The number of vowels in {string} is: {vowel_count}")

#3. find hcf of a num?
def hcf(a, b):
    if a < b:
        smallest = a
    else:
        smallest = b

    for i in range(1, smallest + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans
result = hcf(8, 12)
print(f"The HCF of 8 and 12 is: {result}")

# create a quadratic equation solver function with return
def solve_quadratic(a, b, c):
    y = ((b**2) - (4*a*c)) ** 0.5
    x1 = (-b + y) / (2*a)
    x2 = (-b - y) / (2*a)
    return print(f"x1 = {x1}, x2 = {x2}")

solve_quadratic(1, 5, 6)

# Create multiplication table of a number passing to function using function with return

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        t = str(n) + " x " + str(i) + " = " + str(n * i)
        table.append(t)
    return table

x = multiplication_table(5)
for j in x:
    print(j)


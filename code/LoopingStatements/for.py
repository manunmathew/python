#
#    print(i)
for i in range(1, 13, 3):
    print(i)

for x in range(1, 100, 2):
    print(x)

# print multiplication table
num = int(input('Enter a number: '))
for i in range(1, 11):
    print(i, '*', num, '=', i*num)

# total of n natural numbers

n = int(input('Enter a number: '))
total = 0
for i in range(1, n+1):
    total += i
print(total)

# reverse order
for i in range(10, 0, -1):
    print(i)
# loop control statement
for i in range(20):
    if i > 10:
        break
    print(i)
for i in range(20):
    if i == 10:
        continue
    print(i)
for i in range(20):
    pass

# prime number

num = int(input("Enter the number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
elif num == 1:
    print("1 is not a prime number")
elif num == 0:
    print("you entered zero ..")
else:
    print("Please enter a positive integer")


#  Write a program to take 2 inputs from the user
# initial range and final range
# Then display the numbers fall in the range

start = int(input('Enter the start number: '))
end = int(input('Enter the end number: '))
for i in range(start, end+1):
    print(i)


# print  the series 10,20,30,40,50

start = int(input('Enter the start number: '))
end = int(input('Enter the end number: '))
for i in range(start, end+1, 10):
    print(i)

# print the reverse order 5000, 4000, 3000, 2000, 1000
start = int(input('Enter the start number: '))
end = int(input('Enter the end number: '))
for i in range(start, end-1, -1000):
    print(i)

# write a program to find the total of first 20 odd numbers
start = int(input('Enter the first number: '))
total = 0
if start % 2 == 0:
    start += 1
for i in range(start, start+40, 2):
    total += i
print(total)

# write a program to print the product of first 5 natural numbers

product = 1
for i in range(1, 6):
    product *= i
print(product)


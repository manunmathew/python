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

# # write a program to find the sum of both even and odd numbers fall in the range 1-20
# sumofodd=0
# sumofeven=0
# for i in range(1, 20, 2):
#     sumofodd+=i
#     sumofeven+=(i+1)
# print("Sum of odd = ", sumofodd )
# print("Sum of even = ", sumofeven )
# ##
sumofodd=0
sumofeven=0
for i in range(1, 20):
    if (i%2==0):
        sumofeven+=i
    else:
        sumofodd+=i
print("Sum of odd = ", sumofodd )
print("Sum of even = ", sumofeven )

# write a program to count the total number of even numbers fall in the range 1-100

count = 0
for i in range(1, 100):
    if (i%2 == 0):
        count += 1
print("Number of even = ", count )

# write a program to count the number of both even and odd numbers fall in the range 1500- 3000

even = 0
odd = 0
for i in range(1500, 3000):
    if (i%2 == 0):
        even += 1
    else:
        odd += 1
print("Number of even = ", even)
print("Number of odd = ", odd)


# write a program to find the factorial of a number input by the user


n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial of the number {n} = {fact}")

# Write a program to find the sum of digits of a number input by the user
n = int(input("Enter the number: "))
sum = 0
for i in str(n):
    sum += int(i)
print(f"sum of the digits of {n} = {sum}")


num = int(input("Enter the number: "))
sum = 0
len = len(str(num))
for i in range(len):
    rem=num%10
    sum+=rem
    num//=10
print(sum)

# write a program to find the product of digits of a number input by user
n = int(input("Enter the number: "))
product = 1
for i in str(n):
    product *= int(i)
print(f"product of the digits of {n} = {product}")
# write a program to find a number is harshad or not
# Harshad number: if the number is divisible by the sum of its digits

n = int(input("Enter the number: "))
sum = 0
for i in str(n):
    sum += int(i)
if (n%sum==0):
    print(f"The number {n} is a harshad number")
else:
    print(f"The number {n} is not a harshad number")



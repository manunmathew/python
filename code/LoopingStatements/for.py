#
#    print(i)
for i in range(1,13,3):
    print(i)

for x in range(1,100,2):
    print(x)

# print multiplication table
num = int(input('Enter a number: '))
for i in range(1,11):
   print(i, '*', num, '=', i*num)

# sum of n natural numbers

n = int(input('Enter a number: '))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

#reverse order
for i in range(10, 0, -1):
   print(i)
# loop control statement
for i in range(20):
    if i>10:
        break
    print(i)
for i in range(20):
     if i==10:
        continue
     print(i)

for i in range(20):
    pass

# prime number

num = int(input("Enter the number: "))
if num >1:
    for i in range(2, num):
        if num%i==0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
elif num==1:
    print("1 is not a prime number")
elif num==0:
    print("you entered zero ..")
else:
    print("Please enter a positive integer")

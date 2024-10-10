# # create a list that consist of first ten natural numbers using for loop

# li = []
# for i in range(1,11):
#     li.append(i)
# print(li)

# li = [i for i in range(1,11)]
# print(li)

# # genarate a list that consist of a squre of first 10 natural numbers

# li = [i**2 for i in range(1,11)]
# print(li)

# # find the square root of numbers range from 1-10
# li = [ x**0.5 for x in range(1,11)]
# print(li)
# # find the reverse of each strings in given tuple and generate new list
# t = ("hello", "hai", "welcome")
# li = [x[::-1] for x in t]
# print(li)
# # Find even numbers from the range 1-10 using listcomprehension

# li = [i for i in range(1,100) if i%2 ==0]
# print(li)
# 1) create a list of first 20 odd numbers?
li = [x for x in range(1,40) if x %2 != 0]
print(li)

# 2) given a list of strings, create a new list that contains only strings with more than 3 characters?
words = ["hi","hello","ab", "welcome"]
li = [x for x in words if len(x) >3 ]
print(li)
# 3) create a list of numbers in the range 1 -100 that are divisible by 3 or 5
li = [x for x in range(1,100) if x%3==0 or x%5==0 ]
print(li)
# 4) extract first character from each words in the given list
words = ["hi","hello","ab", "welcome"]
li = [x[0] for x in words]
print(li)
# you have a list of integers. write a list comprehension to create a new list where if the number is even square it if its odd cube it.
l = [3,8,12,5,14,10]

li = [x**2 if x%2==0 else x**3 for x in l]
print(li)

# 1, you have a list of strings. if the words contaon "a" the string convert to uppercase
words = ["apple",  "orange", "banana", "fig","cherry"]
li = [x.upper() if x.count("a") > 0 else x for x in words]
print(li)

# 2, you have a list of integeres if the number is greater than 10, subtract 5 from it if the number is 10 or less multiply it by 2

num = [5,12,18,7,3,14]
li = [x - 5 if x > 10 else x*2 for x in num ]
print(li)

# 3, multiply by 3 if its divisible by 5 else reduce by 2
num = [5,10,12,13,40]
li = [x*5 if x % 5 ==0 else x-2 for x in num ]
print(li)





# if the number ==3 **2

# if the numbers ==5 **3

# else i


l = [3,8, 12,5,7,14,10]

li = [ x**2 if x==3 else(x**3 if x==5 else x) for x in l]

print(li)

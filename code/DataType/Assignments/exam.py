# # 1. Python program to print duplicate elements in the given array?
# #Arr = [1,2,3,3,4,4,5]

arr = [1, 2, 3, 3, 4, 4, 5, 5, 5, 8, 8, 8]
duplicates = set()

for i in arr:
    if arr.count(i) > 1:
        duplicates.add(i)

print("Duplicate elements:", list(duplicates))

# # 2. Find the largest element in the given Array?
# # Arr= [500,200,100,50,1000]

arr = [500, 200, 100, 50, 1000, 5000, 1001]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)

# # 3. Write a program to check a string is palindrome or not ?(without using slicing method)
# # Input : malayalam
# # Output : yes, malayalam is a palindrome word

s = input("Enter the string: ")
r = ""

for i in s:
    r = i + r

if s == r:
    print(f"Yes, {s} is a palindrome word")
else:
    print(f"No, {s} is not a palindrome word")

# # 4. Write a program  to reverse the given list ?(without using reverse function)
# Li = [ 1,2,3,4,5]
Li = [1, 2, 3, 4, 5]
revLi = Li[::-1]

print("Reversed list:", revLi)

# # 5. Without using a sorted() function sort the given dictionary?
# # dict={‘b’:2,’a’:1,’c’:3}
dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = {}
sorted_keys = []

keys = list(dict.keys())
while keys:
    smallest = keys[0]
    for key in keys:
        if key < smallest:
            smallest = key
    sorted_keys.append(smallest)
    keys.remove(smallest)

for key in sorted_keys:
    sorted_dict[key] = dict[key]

print("Sorted dictionary:", sorted_dict)


# # 6. Generate a dictionary where each key is an integer from 101 to 110, and each corresponding value is the reverse of that integer?
# # Example : {101:101 ,102 : 201 , ……}

revdict = {}

for i in range(101, 111):
    revstr = str(i)[::-1]
    revnum = int(revstr)
    revdict[i] = revnum

print("Generated dictionary:", revdict)


# # 7. Generate the given list by taking input from the user?

# # Li=[‘a’ , 1 , ‘b’ , 2 ,’c’, 3]
n = int(input("Enter number of character: "))
Li = []

for i in range(n):
    al = input("Enter a character: ")
    num = int(input("Enter a number: "))
    Li.append(al)
    Li.append(num)
print("Generated list:", Li)

# # 8. Input a string from user and print the even position of the string as UPPER case and odd position as  Lower case?

# # Input : hello

# # Output : HeLlO

s = input("Input : ")
result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i].upper()
    else:
        result += s[i].lower()

print("Output :", result)

# # 9. Write a Python program to create a dictionary with each character of a string as a key and its count as the corresponding value.
# # Example:
# #             Input: hello
# #             Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

s = input("Enter a string: ")
mydict = {}

for i in s:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1

print("Character count dictionary:", mydict)

# # 10. Input a string from the user and remove duplicate elements ?

# # Input : hello

# # Output : helo
s = input("Enter a string: ")
result = ""

for i in s:
    if i not in result:
        result += i

print("String without duplicates:", result)

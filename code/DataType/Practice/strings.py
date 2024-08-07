# String Operations
# # String Reversal
# # # Write a function that takes a string and returns the string reversed.
# mystring = input("Enter the String: ")
# reversed = ""
# for i in mystring:
#     reversed = i + reversed
# print(reversed)

# mystring = input("Enter the String: ")
# mylist = list(mystring)

# mylist.reverse()
# print("".join(mylist))

# mystring = input("Enter the String: ")

# print(mystring[::-1])

# # Palindrome Check

# # Write a function that checks whether a given string is a palindrome (reads the same forward and backward).

# mystring = input("Enter the String: ")
# x = mystring[::-1]

# if mystring == x :
#     print(f"{mystring} is palindrome")
# else:
#     print(f"{mystring} is not palindrome")
# # Character Frequency

# # Write a function that takes a string and returns a dictionary with the frequency of each character in the string.
# mystring = input("Enter the String: ")
# mymap = {}
# for i in mystring:
#     mymap[i] = mystring.count(i)
# print(mymap)

# mystring = input("Enter the String: ")
# mymap = {}

# for i in mystring:
#     if i in mymap:
#         mymap[i] += 1
#     else:
#         mymap[i] = 1
# print(mymap)


# mystring = input("Enter the String: ")
# mymap = {}
# for i in mystring:
#    mymap.update({i: mystring.count(i)})
# print(mymap)


# # Vowel Count

# # Write a function that counts the number of vowels in a given string.
# mystring = input("Enter the String: ")
# vowels = set("aeiouAEIOU")
# count = 0

# for i in mystring:
#     if i in vowels:
#         count += 1
# print(count)


# # Substring Check


# # Write a function that checks whether a given substring exists within a string.


# # Anagram Check

# # Write a function that checks whether two strings are anagrams of each other (contain the same characters in a different order).
# # Remove Whitespace

# # Write a function that removes all whitespace characters (spaces, tabs, newlines) from a string.
# # Capitalize Words

# # Write a function that capitalizes the first letter of each word in a string.
# # Count Words

# # Write a function that counts the number of words in a string.
# # Find Longest Word

# # Write a function that finds and returns the longest word in a string.

n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in arr:
        sum += i
result = sum / (len(arr))
print(f"{result:.3f}")





# Initialize a list with a mix of strings and integers
mylist = ["Manu", "Aswin", "Ajal", "Niyas", 1, 2, 3, 4]

# Print the type of the list
print(type(mylist))  # Output: <class 'list'>

# Access and print the first element in the list
print(mylist[0])  # Output: Manu

# Access and print elements from index 0 to 6
print(mylist[0:7])  # Output: ['Manu', 'Aswin', 'Ajal', 'Niyas', 1, 2, 3]

# Access and print the last element in the list
print(mylist[-1])  # Output: 4

# Update list: Insert an element at the beginning
mylist.insert(0, "Mithra")
print(mylist)  # Output: ['Mithra', 'Manu', 'Aswin', 'Ajal', 'Niyas', 1, 2, 3, 4]

# Update list: Append an element to the end
mylist.append("Anjana")
print(mylist)  # Output: ['Mithra', 'Manu', 'Aswin', 'Ajal', 'Niyas', 1, 2, 3, 4, 'Anjana']

# Update list: Extend the list by appending elements from another list
mylist.extend(["Allen", "Parthan"])
print(mylist)  # Output: ['Mithra', 'Manu', 'Aswin', 'Ajal', 'Niyas', 1, 2, 3, 4, 'Anjana', 'Allen', 'Parthan']

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [3, 4, 5, 6]
print(list1 + list2)  # Output: [1, 2, 3, 3, 4, 5, 6]

# Remove operations

# Reinitialize the list
mylist = ["Manu", "Aswin", "Ajal", "Niyas", 1, 2, 3, 4]

# Delete the first element
del mylist[0]
print(mylist)  # Output: ['Aswin', 'Ajal', 'Niyas', 1, 2, 3, 4]

# Remove an element by value
mylist.remove("Ajal")
print(mylist)  # Output: ['Aswin', 'Niyas', 1, 2, 3, 4]

# Remove an element by index using pop
mylist.pop(0)
print(mylist)  # Output: ['Niyas', 1, 2, 3, 4]

# Clear the entire list
mylist.clear()
print(mylist)  # Output: []

# Sum of elements in a list
x = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for i in x:
    sum += i
print(sum)  # Output: 28

# Product of elements in a list
x = [1, 2, 3, 4, 5, 6, 7]
prod = 1
for i in x:
    prod *= i
print(prod)  # Output: 5040

# Print elements in odd and even positions

# Initialize the list
x = [11, 12, 13, 14, 15, 16, 17, 18, 19]

# Print elements in odd positions (1-based index)
print("Elements in odd positions: ", end="")
for i in range(1, len(x), 2):
    print(x[i], end=",")
print()

# Print elements in even positions (1-based index)
print("Elements in even positions: ", end="")
for i in range(0, len(x), 2):
    print(x[i], end=",")
print()

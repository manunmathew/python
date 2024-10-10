# Set Operations in Python

# Creating a set
set1 = {"Aswin", "Abhijith", "Ajal", "Anupam", "Fathima"}
print(type(set1))  # <class 'set'>

# Adding an element to the set
set1.add("Anjana")
print(set1)  # Output will include "Anjana"

# Adding multiple elements to the set
set1.update(["Akash", "Hitha"])
print(set1)  # Output will include "Akash" and "Hitha"

# Removing an element from the set
set1.remove("Ajal")
print(set1)  # Output will not include "Ajal"

# Discarding an element (no error if element does not exist)
set1.discard("Luminar")  # No error, even though "Luminar" is not in the set

# Creating another set for set operations
set1 = {"Aswin", "Abhijith", "Ajal", "Anupam", "Fathima", "Abhijith"}  # Note: "Abhijith" is duplicate
set2 = {"Aswin", "Abhijith", "Nivedh", "Goutham", "Anu", "Vipin"}

# Union Operation
print(set1 | set2)  # Combines all unique elements from both sets
print(set1.union(set2))  # Equivalent to the above operation

# Intersection Operation
print(set1 & set2)  # Gets elements present in both sets
print(set1.intersection(set2))  # Equivalent to the above operation

# Difference Operation
print(set1 - set2)  # Gets elements present in set1 but not in set2
print(set1.difference(set2))  # Equivalent to the above operation

# Symmetric Difference Operation
print(set1 ^ set2)  # Gets elements present in either set, but not in both
print(set1.symmetric_difference(set2))  # Equivalent to the above operation

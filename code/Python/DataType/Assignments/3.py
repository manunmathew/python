# 3. Python program to print the duplicate elements of an array

list1 = list(input("Enter the elements of the array (elements separated by commas): ").split(','))
elements = []
for i in list1:
    if list1.count(i) > 1:
        if i not in elements:
            elements.append(i)
if len(elements) != 0:
    print(f"Duplicate elements: {elements}")
else:
    print("No duplicate elements found.")

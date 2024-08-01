# 2. Write a program to count Write the program to find the lists consist of at least one common element.

list1 = list(input("Enter the first list of elements separated by spaces: ").split())
list2 = list(input("Enter the second list of elements separated by spaces: ").split())
count = 0
elements = []
for i in list1:
    if i in list2:
        elements.append(i)
        count += 1
if elements:
    print(f"Common elements are: {elements}")
else:
    print("No common elements found.")
print(f"Number of common element is: {count}")


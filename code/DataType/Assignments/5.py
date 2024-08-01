# 5. Python program to print the smallest element in an array

list1 = list(input("Enter the elements of the array (elements separated by commas): ").split(','))

smallest = int(list1[0])

for i in list1:
    i = int(i)
    if i < smallest:
        smallest = i

print(f"The smallest element is: {smallest}")

 # find the largest element in the given array
list1 = list(input("Enter the elements of the array (elements separated by commas): ").split(','))

largest = int(list1[0])

for i in list1:
    i = int(i)
    if i > largest:
        largest = i

print(f"The largest element is: {largest}")

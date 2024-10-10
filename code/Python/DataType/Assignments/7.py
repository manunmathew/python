 # Write a program to reverse a list without using reverse()

list1 = list(input("Enter the elements of the array (elements separated by commas): ").split(','))
rev_list = []

while list1:
    last_element = list1.pop()
    rev_list.append(last_element)
print("Reversed list:", rev_list)







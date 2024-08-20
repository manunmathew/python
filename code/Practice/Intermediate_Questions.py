# Question 1: Dictionary Manipulation
# You have a dictionary grades where the keys are student names and the values are their grades in a course.
# Write a Python function to return the name of the student with the highest grade.
# How would you handle the case where two students have the same highest grade?



# Question 2: Nested Data Structures
# Consider a dictionary that contains student information in the following format:
#
# students = {
#     "Alice": {"age": 24, "courses": ["Math", "Science"]},
#     "Bob": {"age": 22, "courses": ["English", "History"]},
#     "Charlie": {"age": 23, "courses": ["Math", "History", "Science"]},
# }
#
# def courses (students, subject ):
#     for i,j in students.items():
#         if subject in j["courses"]:
#             print(i, end = ",")
#     print()
# students = {
#      "Alice": {"age": 24, "courses": ["Math", "Science"]},
#      "Bob": {"age": 22, "courses": ["English", "History"]},
#      "Charlie": {"age": 23, "courses": ["Math", "History", "Science"]},
#  }
# courses(students, "Math")
# Write a Python function to find all students who are enrolled in the "Math" course.

# Question 3: Combining Data Structures
# You are given a list of dictionaries where each dictionary contains information about a product in a store.
# Write a Python function to find the most expensive product.
#
# Example:
#
# products = [
#     {"name": "Laptop", "price": 800},
#     {"name": "Smartphone", "price": 600},
#     {"name": "Tablet", "price": 300}
# ]

# def expensive(products):
#     highest_price = 0
#     expensive_product = ""
#     for product in products:
#         if product["price"] > highest_price:
#             highest_price = product["price"]
#             expensive_product = product["name"]
#     print("Expensive product : ", expensive_product)
# products = [
#     {"name": "Laptop", "price": 800},
#     {"name": "Smartphone", "price": 600},
#     {"name": "Tablet", "price": 300},
#     {"name": "Desktop", "price": 1200},
#     {"name": "Smartwatch", "price": 250},
#     {"name": "Camera", "price": 700},
#     {"name": "Headphones", "price": 150},
#     {"name": "Monitor", "price": 500},
#     {"name": "Printer", "price": 400},
#     {"name": "Keyboard", "price": 100},
#     {"name": "Mouse", "price": 50}
# ]
# expensive(products)

# Question 4: Complex Loops with Dictionaries
# Given a dictionary that maps employee names to their list of projects:
#
# employees = {
#     "John": ["Project1", "Project2"],
#     "Jane": ["Project2", "Project3", "Project4"],
#     "Doe": ["Project1", "Project4"]
# }
#
# Write a Python function that returns a dictionary mapping each project to the list of employees working on it.

# def project_map(employees):
#     project_list = {}
#     for name, projects in employees.items():
#         for project in projects:
#             if project not in project_list:
#                 project_list[project] = []

#             project_list[project].append(name)

#     print(project_list)

# employees = {
#     "John": ["Project1", "Project2"],
#     "Jane": ["Project2", "Project3", "Project4"],
#     "Doe": ["Project1", "Project4"]
# }
# project_map(employees)

# Question 5: Dictionary and Set Operations
# You have two dictionaries dict1 and dict2 where keys are strings and values are sets of integers.
# Write a Python function to find the intersection of values for keys that exist in both dictionaries.


# dict1 = {
#     "keyA": {1, 2, 3},
#     "key2": {4, 5, 6},
#     "keyB": {7, 8, 9}
# }


# dict2 = {
#     "keyA": {10, 11, 12},
#     "keyB": {13, 14, 15},
#     "keyC": {16, 17, 18}
# }


# def commonset (a,b):
#     common ={}
#     for key in a:
#         if key in b:
#             common[key] = []
#             common[key].extend(a[key])
#             common[key].extend(b[key])


#     print(common)

# commonset(dict1,dict2)



dict1 = {
    "keyA": {1, 2, 3},
    "key2": {4, 5, 6},
    "keyB": {7, 8, 9}
}


dict2 = {
    "keyA": {10, 11, 12},
    "keyB": {13, 14, 15},
    "keyC": {16, 17, 18}
}


def commonset (*a):
    common ={}
    print(a)



    print(common)

commonset(dict1,dict2)

# Question 6: String and Dictionary Manipulation
# Given a string containing a sentence, write a Python function that returns a dictionary where the keys are the words in the sentence,
# and the values are the number of times each word appears. Ignore case and punctuation.

# Question 7: Nested Loops with Conditions
# Write a Python function that takes a list of tuples where each tuple contains a student's name and their test score.
# The function should return a list of names of students who scored above the average score.


# Question 8: Loop and Dictionary Construction
# Write a Python function that takes a list of words and returns a dictionary where the keys are the lengths of the words,
# and the values are lists of words of that length.

# Question 9: Data Filtering with Dictionaries
# You have a dictionary where the keys are product names and the values are their prices.
# Write a Python function that returns a list of products that cost more than a given amount.

# Question 10: Combining Multiple Concepts
# Given a list of dictionaries, each representing an order with a product name and quantity,
# write a Python function to generate a summary dictionary where each key is a product name
# and each value is the total quantity ordered.
#
# Example:
#
# orders = [
#     {"product": "Apple", "quantity": 5},
#     {"product": "Banana", "quantity": 2},
#     {"product": "Apple", "quantity": 3},
# ]

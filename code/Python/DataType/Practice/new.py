# # Write a function to find the common elements between two lists.

# l1 = list(input("Enter the list space separated: ").split())
# l2 = list(input("Enter the list space separated: ").split())

# s1 = set(l1)
# s2 = set(l2)

# s3 = s1 & s2
# print(list(s3))

# Given a list of scores, write a function to find the runner-up (second highest) score.

# n = int(input("Enter Number of students: "))
# record = {}
# for i in range(n):
#     name = input("Enter the Name: ")
#     score = int(input("Enter the Score: "))
#     record[name] = score
# print(record)



# n = int(input("Enter Number of students: "))
# record = {}
# for i in range(1,n+1):
#     name = input("Enter the Name: ")
#     score = int(input("Enter the Score: "))
#     record["Student" +str(i) ] = {"Name": name, "Score": score}
# print(record)
# sum = 0
# for student in record:
#     sum += record[student]["Score"]
# avarage = sum/len(record)
# print(avarage)

n = int(input())
arr = map(int, input().split())

print(arr)
scores = list(arr)
print(scores)

# # Write code to print below patterns

# # *
# # * *
# # * * *
# # * * * *
# # * * * * *


# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print ("*", end=" ")
#     print()

# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5

# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows+1):
#     for j in range(i):
#         print (i, end=" ")
#     print()

# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows+1):
#     for j in range(1,i+1):
#          print (j, end=" ")
#     print()

# # * * * * *
# # * * * *
# # * * *
# # * *
# # *

# rows = int(input("Enter the number of rows: "))
# for i in range(rows, 0, -1):
#     for j in range(i):
#          print ("*", end=" ")
#     print()

# #                   *
# #                 *   *
# #               *   *   *
# #             *   *   *   *
# #           *   *   *   *   *
# #         *   *   *   *   *   *
# #       *   *   *   *   *   *   *
# #     *   *   *   *   *   *   *   *
# #   *   *   *   *   *   *   *   *   *
# # *   *   *   *   *   *   *   *   *   *

# rows = int(input("Enter the number of rows: "))

# for i in range(rows):
#     for j in range(rows -i -1):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("*", end="   ")
#     print()


# n = int(input("Enter the Number od rows: "))


# for i in range(n):
#     for s in range(n,  i ,- 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("* ", end="")
#     print()

s = input("Enter the String: ")


for i in range(n):
    for j in range(i + 1):
        print("* ", end="")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("* ", end="")
    print()


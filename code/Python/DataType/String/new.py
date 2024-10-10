# without using len function find length of a string
# mystring = input("Enter the String: ")

# count = 0
# for i in mystring:
#     count += 1
# print(count)

# Reverse a string
# s = input("Enter a string: ")
# revstr = ""
# for i in range(len(s) - 1, -1, -1):
#     revstr += s[i]
# print(revstr)


# s = input("Enter a string: ")
# revstr = ""
# for i in s:
#     revstr = i + revstr
# print(revstr)





#     H
#    HHH
#   HHHHH
#  HHHHHHH
# HHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#                     HHHHHHHHH
#                      HHHHHHH
#                       HHHHH
#                        HHH
#                         H


# s = int(input())
# a = "H"
# b = " "
# c = 1
# for i in range(s):
#     print((a * c).center(s*2, " "))
#     c += 2
# for i in range(s + 1):
#     left = (a * s).center(s*2, " ")
#     right = (a * s).rjust(s + (s * 2))
#     print(left + right)
# for i in range((s // 2)+1):
#     print((a * (s * 5)).center(s * 6, b))
# for i in range(s + 1):
#     left = (a * s).center(s*2, " ")
#     right = (a * s).rjust(s + (s * 2))
#     print(left + right)
# for i in range(s+1, -1, -1):
#      c -= 2
#      print((a * c).center(s * 6, b))

# ## need to correct last loop



# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


# size = 5

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# width = 4 * size - 3

# # Initialize an empty list to store the pattern
# pattern = []

# # Generate the top half including the middle row
# for i in range(size):
#     print(i)
#     row = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
#     print(row)
#     pattern.append(row.center(width, '-'))
#     print(pattern)

# # Print the top half and middle row
# for line in reversed(pattern[:-1]):
#     print(line)
# Print the bottom half by reversing the pattern list excluding the middle row
# for line in pattern:
#     print(line)



# even position
# b = "Hello, World!"
# print(b[:: 2])
# print(b[2 :: 2])




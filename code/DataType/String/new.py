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


s = int(input())
a = "H"
b = " "
c = 1
for i in range(s):
    print((a * c).center(s*2, " "))
    c += 2
for i in range(s + 1):
    left = (a * s).center(s*2, " ")
    right = (a * s).rjust(s + (s * 2))
    print(left + right)
for i in range((s // 2)+1):
    print((a * (s * 5)).center(s * 6, b))
for i in range(s + 1):
    left = (a * s).center(s*2, " ")
    right = (a * s).rjust(s + (s * 2))
    print(left + right)
for i in range(s+1, -1, -1):
     c -= 2
     print((a * c).center(s * 6, b))

## need to correct last loop

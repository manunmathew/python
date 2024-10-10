import re

txt = "varun and arjun are students"

a = re.split(r'\s', txt)
b = re.split(r'\s', txt, 1)
c = re.split(r'\s', txt, 2)
d = re.split(r'\s', txt, 3)


print(a)
print(b)
print(c)
print(d)

import re

txt = "varun and arjun are students"

a = re.sub(r'\s', '#', txt)

print(a)




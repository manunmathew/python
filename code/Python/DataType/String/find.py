x = "find string in a paragraph in in"
print(x.find("in"))  # if its there it will give index number
print(x.find("hello")) # if not there it will give -1

print(x.index("in")) # if its there it will give index number
#print(x.index("hello")) #if not there it will give value error

print(x.rfind("in")) #if its there it will give index number.. if multiple .. last index
print(x.rfind("hello")) #if not there it will give -1

print(x.count("in")) # will give number of ..

# 1. Using function with return Reverse an array of integers. Without using slicing and inbuild
# functions ?
# Example
# Input : [1,2,3]
# Output :[2,3,1]

# def rev(li):
#     il = []
#     for i in li:
#         il.insert(0,i)
#     return il
# a = [1,2,3]
# Output = rev(a)
# print(Output)

# 2. Pass a list into a function and return both minimum and maximum elements without using
# Inbuild functions ?
# Example :
# Input :[1,2,3,4]
# Minimum element = 1
# Maximum element =4



# li = [1,2,3,4]
# def min_max(a):
#     min = a[0]
#     max = a[0]
#     l = len(a)
#     for i in range(l):
#         for j in a:
#             if j < min :
#                 min = j
#             if j > max :
#                 max = j
#     return min, max
# output = min_max(li)
# print('Minimum element =', output[0])
# print('Maximum element =', output[1])





# 3. Input any number of strings into a function and finally return a dictionary that contains
# key value pairs , where value is the reverse of each strings ?

# def key_value(*a):
#     mydict = {}
#     for i in a:
#         print(i)
#         mydict.update({str(i):str(i[::-1])})
#     return mydict
# o = key_value("manu","hello","world")
# print(o)


# 4. Pass a string into a function and return a dictionary that contains each character and its
# index position without using any inbuild methods ?

# Example : ‘hello’
# Return : {‘h’:0 , ‘e’:1 , ‘l’:2, ’l’:3, ’o’:4}

# def string_index(a):
#     mydict = {}
#     index = 0
#     for i in a:
#         mydict[i] = index
#         index += 1
#     return mydict

# o = string_index("hello")
# print(o)

# 5. Pass a list into a function and return a dictionary that contains each elements and its
# factorial?
# Example : [1,2,3,4,5]
# Return : {1:1 , 2:2 , 3:6 , 4:24, 5:125}

# 6. Write a function that passes string as an argument and return a string by remove all the
# duplicates?
# Example :’hello’
# Return :’helo’

# 7. Capitalize the alternative characters of a string passing into a function?

# Example:’world’
# Output: WoRlD
# 8. Pass any number of elements into a function and return a set ?
def create_set(*args):
    return set(args)
# 9. Pass a string into a function and return a string with all the vowels removed?

# 10. Pass a list into a function a return a list with all the elements squared?
li = [1,2,3,4]
x = list(map(lambda i : i**2, li))
print(x)

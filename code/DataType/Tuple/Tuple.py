x = (1, 2, 3, 4, "python", "Django",1,3)

# Access tuple elements
print(type(x))  # Output: <class 'tuple'>
print(x[0])     # Output: 1
print(x[-1])    # Output: Django
print(x[2:5])
print(len(x))
print(x.count(3))
print(x.index(3))

# Delete tuple
del x


# # iterate a given tuple
t1 = ("a","b","c")
for i in t1:
    print(i)
# # find the min value of the given tuple
t1 = (5,2,1,6,4)

min = t1[0]
for i in t1:
        if i < min :
            min = i
print("Min value is ", min)
# # find the max value
t1 = (5,2,1,6,4)
max = t1[0]
for i in t1:
        if i < max :
            min = i
print("Max value is ", max)
# # find the sum of elements in tuple
t1 = (100,200,300,400,500)
sum = 0
for i in t1:
        sum += i
print("Sum is ", sum)


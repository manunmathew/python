# String Concatenation

# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

#String join() Method
#The join() method takes all items in an iterable and joins them into one string.

# A string must be specified as the separator.
myDict = {"Manu",  "Norway"}
mySeparator = " "

x = mySeparator.join(myDict)

print(x)


a = "Hello"
b = "World"
print("%s%s" % (a,b) )
print("%s %s" % (a,b) )
print("%s_%s" % (a,b) )
print("{}{}".format(a,b))
print("{} {}".format(a,b))
print("{}_{}".format(a,b))

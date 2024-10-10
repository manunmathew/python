import time

# localtime()


# t = time.localtime()
# print(t)

# print("Year: ", t.tm_year)
# print("Month: ", t.tm_mon)
# print("Day: ",t.tm_mday)
# a = time.asctime()
# print(a)

# sleep .. to add delay in execution
# time.sleep()
# print("Hello")
# time.sleep(3)
# print("Hello after 3 second")

# strftime()
# %A: day , %B: month %d: date ,%D: complete date, %Y: year
# %M: min,%S: sec ,%H: hour , %m:month,
t = time.strftime("%A")
print(t)

t = time.strftime("%a")
print(t)

t = time.strftime("%B")
print(t)


t = time.strftime("%b")
print(t)
t = time.strftime("%Y")
print(t)
t = time.strftime("%H:%M:%S")
print(t)
t = time.strftime("%a %b %d-%m-%y %H:%M:%S")
print(t)

# Random module generate random numbers or data

import random


l = [1,2,3,4]
print(random.choice(l))


#randint() : it is used to select random integers between the given range
# random.randint(start,end)

r1 = random.randint(100,200)
print(r1)

# random.uniform(start, end)

r1 = random.uniform(10,20)
print(r1)

# shuffle() shuffle a list of elements

li = [1,2,3]
random.shuffle(li)
print(li)



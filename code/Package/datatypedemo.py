from datatype import string
from datatype import lists
from datatype import sets
from datatype import tuples
from datatype import dicts

email = "user123@website.com"
a = string.validate_email(email)
print(a)

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
b = lists.remove_duplicates_and_sort(my_list)
print(b)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
c = sets.union_and_difference(set_a, set_b)
print(c)

dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}
d = dicts.merge_and_update(dict_a, dict_b)
print(d)

my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5)
e = tuples.find_max_and_min(my_tuple)
print(e)

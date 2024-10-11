# Tuple Operations in Python

A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

### Creating a Tuple

You can create a tuple by placing comma-separated values inside round brackets `()`.

```python
x = (1, 2, 3, 4, "python", "Django")
```

### Accessing Tuple Elements

You can access tuple items by referring to the index number, inside square brackets `[]`.

```python
print(type(x))  # <class 'tuple'>
print(x[0])     # Output: 1
print(x[-1])    # Output: Django
```

### Deleting a Tuple

Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. However, you can delete the tuple completely.

```python
del x
```
### Using `.count()`

count()	Returns the number of times a specified value occurs in a tuple

### Using `.index()`
index()	Searches the tuple for a specified value and returns the position of where it was found
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

###  slicing
print(thistuple[2:5])

## Reference Code



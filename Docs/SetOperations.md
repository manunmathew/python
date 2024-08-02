# Set Operations in Python

A set is a collection which is unordered, unindexed, and has no duplicate elements.

### Creating a Set

You can create a set by placing comma-separated values inside curly brackets `{}`.

```python
x = {1, 2, 3, 4, "python", "Django"}
```

### Adding Elements to a Set

- `add()`: Adds a single element to the set.
- `update()`: Adds multiple elements to the set; needs to be passed as a list.

```python
x.add("element")
x.update(["element1", "element2"])
```

### Removing Elements from a Set

- `remove()`: Removes the specified element; raises an error if the element does not exist.
- `discard()`: Removes the specified element; does not raise an error if the element does not exist.

```python
x.remove("element1")
x.discard("element2")
```

### Set Operations

#### Union

Combines all unique elements from both sets.

- Using the pipe `|` operator:
  ```python
  set1 | set2
  ```
- Using `union()` method:
  ```python
  set1.union(set2)
  ```

#### Intersection

Gets only the elements that are present in both sets.

- Using the `&` operator:
  ```python
  set1 & set2
  ```
- Using `intersection()` method:
  ```python
  set1.intersection(set2)
  ```

#### Difference

Gets elements that are present in the first set but not in the second set.

- Using the `-` operator:
  ```python
  set1 - set2
  ```
- Using `difference()` method:
  ```python
  set1.difference(set2)
  ```

#### Symmetric Difference

Gets elements that are present in either of the sets, but not in both.

- Using the `^` operator:
  ```python
  set1 ^ set2
  ```
- Using `symmetric_difference()` method:
  ```python
  set1.symmetric_difference(set2)
  ```

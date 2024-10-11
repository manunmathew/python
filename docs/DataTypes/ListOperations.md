# Python List Operations

## Introduction to Lists

- **Ordered Structure**: Lists maintain the order of elements as they are inserted.
- **Indexing**: Elements in a list can be accessed using indices starting from 0.
- **Mutability**: Lists are mutable, meaning their elements can be changed.
- **Variety**: Lists can store elements of various data types.

## Creating a List

    mylist = ["Manu", "Aswin", "Ajal", "Niyas"]

## Accessing Elements

Elements in a list can be accessed by their index, which starts from 0. Negative indices can also be used to access elements from the end of the list.

- **Print the type of the list**:

    ```python
    print(type(mylist))  # Output: <class 'list'>
    ```

- **Access and print the first element in the list**:

    ```python
    print(mylist[0])  # Output: Manu
    ```

- **Access and print elements from index 0 to 6**:

    ```python
    print(mylist[0:7])  # Output: ['Manu', 'Aswin', 'Ajal', 'Niyas', 1, 2, 3]
    ```

- **Access and print the last element in the list**:

    ```python
    print(mylist[-1])  # Output: 4
    ```

## Updating a List

### Inserting Elements

The `insert()` method inserts an element at the specified index. This shifts the element currently at that position (if any) and any subsequent elements to the right.

    mylist.insert(0, "Mithra")
    <!-- Result: ["Mithra", "Manu", "Aswin", "Ajal", "Niyas"] -->

### Adding Elements

- **Append to the End**:

  The `append()` method adds an element at the end of the list.

    mylist.append("Anjana")
    <!-- Result: ["Manu", "Aswin", "Ajal", "Niyas", "Anjana"] -->

- **Extend the List**:

  The `extend()` method extends the list by appending all the items from the iterable (another list in this case).

    mylist.extend(["Allen", "Parthan"])
    <!-- Result: ["Manu", "Aswin", "Ajal", "Niyas", "Allen", "Parthan"] -->

- **Concatenate Two Lists**:

  You can concatenate two lists using the `+` operator, which creates a new list containing elements from both lists.

    list1 = [1, 2, 3]
    list2 = [4, 5]
    combined_list = list1 + list2
    <!-- Result: [1, 2, 3, 4, 5] -->

## Removing Elements

### Using `del`

The `del` statement removes an element at a specified index or a slice of elements. It can also delete the entire list.

    del mylist[0]
    <!-- If mylist was ["Manu", "Aswin", "Ajal", "Niyas"] -->
    <!-- Result: ["Aswin", "Ajal", "Niyas"] -->

### Using `.remove()`

The `remove()` method removes the first occurrence of a specified value from the list.

    mylist.remove("Ajal")
    <!-- Result: ["Manu", "Aswin", "Niyas"] -->

### Using `.pop()`

The `pop()` method removes the element at the specified position and returns it. If no index is specified, it removes and returns the last element.

    last_element = mylist.pop()
    <!-- Result: ["Manu", "Aswin", "Ajal"] -->
    <!-- last_element: "Niyas" -->

    first_element = mylist.pop(0)
    <!-- Result: ["Aswin", "Ajal", "Niyas"] -->
    <!-- first_element: "Manu" -->

### Using `.clear()`

The `clear()` method removes all elements from the list, leaving it empty.

    mylist.clear()
    <!-- Result: [] -->

### Using `.sort()`

The `sort()` method sorts the list in ascending order by default.

Usage:

    list.sort(reverse=True|False, key=myFunc)

- **reverse**: Optional. `reverse=True` will sort the list in descending order. Default is `reverse=False`.
- **key**: Optional. A function to specify the sorting criteria(s).

Example:

    my_list = [3, 1, 4, 1, 5, 9]
    my_list.sort(reverse=True)
    print(my_list)  # Output: [9, 5, 4, 3, 1, 1]

### Using `.reverse()`

The `reverse()` method reverses the sorting order of the elements.

Usage:

    list.reverse()

Example:

    my_list = [3, 1, 4, 1, 5, 9]
    my_list.reverse()
    print(my_list)  # Output: [9, 5, 1, 4, 1, 3]


## Differences Between Arrays and Lists

- **Lists**:
    - Can store elements of different data types.
    - Part of Python's built-in data structures.
    - More flexible but might be slower for certain operations compared to arrays.

- **Arrays**:
    - Provided by the `array` module.
    - Store elements of the same data type.
    - More efficient for numerical computations.
    - Preferred in performance-critical applications or for numerical operations.

        import array
        myarray = array.array('i', [1, 2, 3, 4])


## Reference Code


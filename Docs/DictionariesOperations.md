# Dictionary Guide

## Introduction to Dictionaries

Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable, and does not allow duplicates.

Example:

    person = {
      "Name": "Manu",
      "Age": "42",
      "Phone": 90540977
    }
    print(person)

## Methods for Dictionaries

### `keys()`
The `keys()` method will return a list of all the keys in the dictionary.

Example:

    print(person.keys())

### `values()`
The `values()` method returns a view object. The view object contains the values of the dictionary, as a list.

Example:

    print(person.values())

### `get()`
The `get()` method returns the value of the item with the specified key.

- **keyname**: Required. The keyname of the item you want to return the value from.
- **value**: Optional. A value to return if the specified key does not exist. Default value is `None`.

Example:

    print(person.get("Name"))
    print(person.get("Address", "Not Available"))

### `pop()`
The `pop()` method removes the specified item from the dictionary. The value of the removed item is the return value of the `pop()` method.

Example:

    removed_value = person.pop("Age")
    print(removed_value)
    print(person)

### `popitem()`
The `popitem()` method removes the item that was last inserted into the dictionary. In versions before 3.7, the `popitem()` method removes a random item.

Example:

    last_item = person.popitem()
    print(last_item)
    print(person)

### `update()`
The `update()` method inserts the specified items to the dictionary.

Example:

    person.update({"Address": "123 Street Name"})
    print(person)

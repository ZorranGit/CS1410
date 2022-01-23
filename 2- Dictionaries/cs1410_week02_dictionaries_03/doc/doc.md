Exercise: lists_to_dict
----------------------

### Description

In this exercise your function will receive two parameters.
The first is a list of strings to use as keys in
a dictionary.  The second is a list of values to use
with the keys.  The function will create a dictionary
with every key/value pair from the lists.  It
will then return the dictionary

### Function Name

lists_to_dict

### Parameters

* `keys`   : a list of strings
* `values` : a list of strings (len(keys) == len(values))

### Return Value

A dictionary with the key/value pairs.

### Examples

    list_to_dict(["a", "b"], ["13", "7" ]) -> { "a": "13", "b": "7" }

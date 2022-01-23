Exercise: values_to_dict
----------------------

### Description

In this exercise your function will receive four parameters.
These parameters correspond to statistics for a baseball
player's trading card.  The function will use these
parameters for values in a dictionary.  The keys for
each value are specified below.  Finally, the function
will return the dictionary constructed with these values.
### Function Name

values_to_dict

### Parameters

*  `at_bats` : an integer value (key is `AB`)
*  `hits` : an integer value (key is `H`)
*  `runs_batted_in` : an integer value (key is `RBI`)
*  `batting_average` : a float value  (key is `AVG`)

### Return Value

A dictionary with the keys `AB`, `H`, `RBI`, and `AVG`.
The values for each of these should come from the input
parameters.

### Examples

    values_to_dict(10, 4, 2, 0.400) -> { "AB": 10, "H": 4, "RBI": 2, "AVG": .4 }

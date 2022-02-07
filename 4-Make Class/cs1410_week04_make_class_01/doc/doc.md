Exercise: Accelerate Method
-------------------------

### Description

In this exercise, you will add to your `Car` class
a method to accelerate the speed of an instance.

### Class Name

`Car`

### Method

`accelerate()`

### Parameters

* `self` : the `Car` object to use
* `delta_speed` : a number, the desired value to add to the speed data member.

### Action

Adds `delta_speed` to the speed of the object.  If the
new speed is too fast, then set the speed to the
maximum allowed speed.

Only do this action of `delta_speed` is positive, and
the `Car` isn't already at maximum speed.

### Return Value

`True` if a change occurred, `False` otherwise.

### Examples

    c = Car()
    c.setSpeed(40.) -> True
    c.accelerate(85.) -> True
    c.accelerate(1.) -> False
    c.accelerate(-1.) -> False

### Hints

- Remember, you're adding to the code from the previous step.
- You may want to use the global constant at the top of your file
  regarding the maximum allowed speed.

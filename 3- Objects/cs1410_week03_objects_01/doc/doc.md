Exercise: create01
----------------------

### Description

Write a function that receives no parameters and returns a `Pencil` object
constructed with 3 leads.

Refer to the `Pencil` documentation below.

### Function Name

`create01`

### Parameters

None

### Return Value

A `Pencil` object with 3 leads.

### Example

This is one example of how we might use your function:

    p = create01()
    print(p.get_num_leads()) # -> 3
    print(p.get_current_lead_length()) # -> 10

## Documentation

### constant `MAX_LEAD_LENGTH`

The maximum length of any lead stick. Set to 10.

<p></p>

### constant `MAX_NUM_LEADS`

The maximum amount of sticks that will fit inside of a Pencil object. Set to 5.

<p></p>

### type `Pencil`

**Contructor:**

`Pencil(num_leads)`

Creates a pencil object. The parameter `num_leads` determines the amount of lead
with which to initialize the Pencil object.

**Methods:**

`get_num_leads()`

Returns the number of leads in the Pencil object. This does not count the lead
that is extending from the pencil.

`get_current_lead_length()`

Returns the length of the lead extending from the pencil.

`click()`

"Clicks" the pencil, reducing the current lead length by one. If the current
lead is used up, reduce the number of leads in the pencil by one and set the
current lead length to the max lead length.

`add_leads(num_additional_leads)`

Adds lead sticks to the pencil. Only adds a positive number of sticks, up to the
maximum number of lead.

**Data members:**

`_num_leads`: the number of lead sticks in the barrel of the pencil.

`_current_lead_length`: the length of the lead stick extending from the pencil.

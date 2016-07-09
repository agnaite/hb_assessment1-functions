def get_item_cost(state, cost, tax=1.05):
    """Calculates total item cost based on state tax rate

    Args:
        state: state abbreviation
        cost: cost of item without tax
        tax: tax rate, with default value of 5%

    Returns:
        item cost with tax included

    """

    if state.lower() == 'ca':
        tax = 1.07

    return cost * tax


def is_berry(fruit):
    """Checks if argument matches certain values

    Args:
        fruit: a string

    Returns:
        True if argument matches "strawberry", "cherry", or "blackberry".
        False otherwise.

    """

    if (fruit.lower() == "strawberry" or
        fruit.lower() == "cherry" or
        fruit.lower() == "blackberry"):
        return True
    else:
        return False


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit):
    """Checks shipping cost based on type of fruit

    Args:
        fruit: a string

    Returns:
        0 if fruit is a strawberry, cherry, or blackberry and 5 otherwise.

    """

    if is_berry(fruit):
        return 0
    else:
        return 5


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################
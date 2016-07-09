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


def is_hometown(town):
    """Checks if a town passed in is a specific town

    Args:
        town: a string

    Returns:
        True if town is Kaunas; False otherwise.

    """

    if town.lower() == 'kaunas':
        return True
    else:
        return False


def full_name(first, last):
    """Returns a full name

    Args:
        first: first name as a string
        last: last name as a string

    Returns:
        full name as a string

    """

    return first + " " + last


def hometown_greeting(town, first, last):
    """Prints a greeting based on full_name and is_hometown function results

    Args:
        town: hometown as a string
        first: first name as a string
        last: last name as a string

    Return:
        prints a greeting

    """

    if is_hometown(town):
        greeting = "we're from the same place!"
    else:
        greeting = "where are you from?"

    print "Hi, {}, {}".format(full_name(first, last), greeting)


def increment(x=1):
    """Sums up x and add(y)

    Args:
        x: number with default value of 1

    Returns:
        sum of two numbers, the latter from nested function add()

    """

    def add(y):
        return y + x
    return add

addfive = increment(5)
addone = increment()
addone(5)
addone(20)


def append_number(num, num_list):
    """Appends a number to a list of numbers

    Args:
        num: a number
        num_list: a list of numbers

    Returns:
        list of numbers with new number added to the end

    """
    num_list.append(num)
    return num_list

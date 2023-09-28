# Variables

What They Are:

- Variables are containers for storing data values. In Python, they're dynamically typed, which means you don't have to declare what type a variable is. You got integers, floats, and strings here.

# Example Code:

- x = 15  # This is an integer
- price = 9.99  # This is a float
- discount = 0.2  # This is also a float
- result = price * (1 - discount)  # This performs an operation
- name = "Rolf"  # This is a string

# In Plain English:
- x = 15: Think of x like a box that you put the number 15 into.
- price = 9.99: Another box, but you put 9.99 in it.
- discount = 0.2: Yet another box, this one's got 0.2.
- result = price * (1 - discount): Here, you're taking the stuff in - the price and discount boxes, doing some math, and putting the result into a new box called result.
- name = "Rolf": You got a box labeled name and you stuffed the word "Rolf" into it.

### De-structuring Variables

#### What it is:
De-structuring allows you to unpack values from data structures like lists, tuples, or dictionaries directly into variables. Think of it like unpacking a care package—you get multiple items out all at once.

#### Why you'd use it:
It's a quick and readable way to assign values to multiple variables in one shot. Super handy to keep your code clean.

#### Syntax & Examples:

1. **Lists and Tuples**
    ```python
    coords = [40.7128, -74.0060]  # New York City coordinates
    lat, lon = coords
    print(lat)  # Output: 40.7128
    print(lon)  # Output: -74.0060
    ```

2. **Dictionaries**
    ```python
    dog = {'name': 'Gunner', 'age': 3}
    name, age = dog.values()
    print(name)  # Output: 'Gunner'
    print(age)   # Output: 3
    ```

3. **Ignoring Values**
    ```python
    # Say you only want latitude
    lat, _ = coords
    print(lat)  # Output: 40.7128
    ```

4. **Nested Structures**
    ```python
    data = ["John", (40.7128, -74.0060)]
    name, (lat, lon) = data
    print(name, lat, lon)  # Output: "John" 40.7128 -74.0060
    ```

#### Common Use Cases:
- Swapping variables
- Iterating through dictionaries/lists with index and value
- Returning multiple values from a function

In simple words, it's like opening a multi-item gift and knowing exactly which item to use for what purpose
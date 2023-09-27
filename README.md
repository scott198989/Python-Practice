# Python-Practice

# Content

This README is for note taking and to help understanding concepts in Python.

# Version 
- Python 3.11.5

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

For sure, Scott. Let's dive into the next topic: String Formatting.

### String Formatting

#### What it is:
String formatting is the process of inserting variables into a string to create a customized output. It's like having placeholders where your variables go, so you can change the variables without changing the string itself.

#### Why you'd use it:
String formatting is useful when you want to display messages that include variables. Like if you want to say "Hello, [Name]" and have it work for any name you provide.

#### How to use it:
Here are the main ways to format strings in Python:

1. **Concatenation**: Just stick strings together with `+`.
   ```python
   name = "Scott"
   print("Hello, " + name)
   ```

2. **% Formatting**: Old-school way but still valid.
   ```python
   name = "Scott"
   print("Hello, %s" % name)
   ```

3. **`.format()` Method**: More modern and flexible.
   ```python
   name = "Scott"
   print("Hello, {}".format(name))
   ```

4. **f-strings**: Latest and easiest way, only available in Python 3.6+.
   ```python
   name = "Scott"
   print(f"Hello, {name}")
   ```

#### Examples:
```python
age = 28
name = "Scott"

# Using .format() method
print("Hello, {}. You are {} years old.".format(name, age))

# Using f-string
print(f"Hello, {name}. You are {age} years old.")
```
### Getting User Input

#### What it is:
The `input()` function allows you to get data from the user through the terminal. The function reads a line from the input and returns it as a string.

#### Why you'd use it:
Whenever you want to gather some kind of information from the user, like their name, age, or any other data, `input()` is the go-to method.

#### How to use it:
Here's the basic syntax:
```python
user_input = input("Prompt message here: ")
```

The string inside the parentheses will be displayed as a prompt, and whatever the user types will be stored in `user_input`.

#### Examples:
1. Asking for a name:
    ```python
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    ```

2. Getting an integer (notice the `int()` conversion):
    ```python
    age = int(input("How old are you? "))
    print(f"Ah, you're {age} years old.")
    ```

3. Getting multiple inputs:
    ```python
    first_name = input("First name: ")
    last_name = input("Last name: ")
    print(f"Your full name is {first_name} {last_name}.")
    ```

#### Important Note:
The `input()` function returns a string. So if you want to use it as a number, you'll have to convert it using `int()` or `float()` like in the age example.
### Lists

#### What it is:
A list in Python is an ordered, mutable (changeable) collection of elements. Each element can be of any data type, including other lists.

#### Why you'd use it:
Lists are one of the most commonly used data structures in Python. You'd use them whenever you need to group a bunch of related data together.

#### How to use it:
Here's the basic syntax to create a list:
```python
my_list = [item1, item2, item3, ...]
```

#### Examples:
1. Basic list of integers:
    ```python
    numbers = [1, 2, 3, 4, 5]
    ```

2. List with mixed types:
    ```python
    mixed = [1, "two", 3.0, [4, 5]]
    ```

3. Access elements by index:
    ```python
    print(numbers[0])  # Output: 1
    ```

4. Change an item:
    ```python
    numbers[1] = 20
    ```

5. Append to the list:
    ```python
    numbers.append(6)
    ```

6. Remove an item:
    ```python
    numbers.remove(3)
    ```

7. Pop an item (remove and return):
    ```python
    last_item = numbers.pop()
    ```

8. Loop through items:
    ```python
    for num in numbers:
        print(num)
    ```

9. List slicing (getting sub-lists):
    ```python
    first_two = numbers[0:2]
    ```

#### Common Methods:
- `append()`: Add an item to the end.
- `remove()`: Remove an item by value.
- `pop()`: Remove and return the item at a given index (or the last item if the index is not provided).
- `index()`: Return the index of a specific item.
- `sort()`: Sort the list in place.

#### Important Note:
Lists are mutable, meaning their content can be changed after creation. If you need an immutable version, that's what tuples are for (we'll get to that).

### Tuples

#### What it is:
A tuple is similar to a list, but it's immutable, meaning you can't change it once it's created.

#### Why you'd use it:
Tuples are generally used for grouping data that belongs together but shouldn't be changed. For example, you could use a tuple to represent a set of coordinates (latitude, longitude) that you wouldn't want to accidentally change later in your code.

#### How to use it:
Here's the basic syntax for creating a tuple:
```python
my_tuple = (item1, item2, item3, ...)
```

#### Examples:
1. Basic tuple:
    ```python
    coordinates = (40.7128, -74.0060)
    ```

2. Accessing elements:
    ```python
    print(coordinates[0])  # Output: 40.7128
    ```

3. Attempt to modify (will cause an error):
    ```python
    # coordinates[1] = -75.0000  # TypeError: 'tuple' object does not support item assignment
    ```

4. Tuple unpacking:
    ```python
    lat, long = coordinates
    ```

5. Nested tuple:
    ```python
    nested_tuple = (1, 2, (3, 4))
    ```

#### Common Methods:
- `index()`: Returns the index of a specific item.
- `count()`: Returns the number of occurrences of a specific item.

#### Important Note:
Since tuples are immutable, they don't have methods for adding or removing elements like lists do. This makes them safer for things you want to set and not accidentally modify, but less flexible if you need to change the data later.

### Sets

#### What it is:
A set is a collection of unique elements, without any order.

#### Why you'd use it:
You'll typically use sets when you're dealing with a collection where you don't want any duplicates and you don't care about the order. Sets can also perform mathematical set operations like union, intersection, and difference.

#### How to use it:
Here's the basic syntax for creating a set:
```python
my_set = {item1, item2, item3, ...}
```

#### Examples:
1. Creating a set:
    ```python
    my_set = {1, 2, 3, 4, 5}
    ```

2. Adding elements:
    ```python
    my_set.add(6)  # my_set becomes {1, 2, 3, 4, 5, 6}
    ```

3. Removing elements:
    ```python
    my_set.remove(1)  # my_set becomes {2, 3, 4, 5, 6}
    ```

4. Checking if an element is in the set:
    ```python
    print(1 in my_set)  # Output: False
    ```

5. Mathematical operations:
    ```python
    another_set = {4, 5, 6, 7, 8}
    print(my_set.union(another_set))  # Output: {2, 3, 4, 5, 6, 7, 8}
    print(my_set.intersection(another_set))  # Output: {4, 5, 6}
    ```

#### Common Methods:
- `add()`: Adds a new element.
- `remove()`: Removes a specific element.
- `union()`: Returns a new set containing all elements from both sets.
- `intersection()`: Returns a new set containing elements found in both sets.
- `difference()`: Returns a new set containing elements in the first set but not in the second set.

#### Important Note:
Since sets don't have any order, they don't support indexing, slicing, or other sequence-like behavior.


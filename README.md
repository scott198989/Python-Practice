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

### Advanced Set Operations

#### What it is:
These are a bit more specialized operations you can do with sets, beyond the basics like adding or removing elements.

#### Why you'd use it:
For handling more complex set manipulation tasks, like getting the symmetric difference between sets or checking if one set is a subset of another.

#### How to use it:
Here are some advanced methods you can use with sets.

#### Examples:
1. `symmetric_difference()`:
    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}
    ```
    This gives you a set containing elements that are only in one of the sets, but not both.

2. `issubset()` and `issuperset()`:
    ```python
    set1 = {1, 2}
    set2 = {1, 2, 3, 4, 5}
    print(set1.issubset(set2))  # Output: True
    print(set2.issuperset(set1))  # Output: True
    ```
    You can check if one set is a subset or superset of another.

3. `update()`:
    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set1.update(set2)
    print(set1)  # Output: {1, 2, 3, 4, 5}
    ```
    This updates a set, adding elements from another set (or any other iterable).

4. `intersection_update()`:
    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set1.intersection_update(set2)
    print(set1)  # Output: {3}
    ```
    Updates the set, keeping only elements found in both sets.

#### Common Methods:
- `symmetric_difference()`
- `issubset()`
- `issuperset()`
- `update()`
- `intersection_update()`

### Booleans

#### What it is:
Booleans in Python represent one of two values: `True` or `False`.

#### Why you'd use it:
You'd use booleans to evaluate conditions, such as in if-else statements or loops. They help in making decisions in your code.

#### How to use it:
It's pretty straightforward, actually. You'll most often see them as the result of a comparison.

#### Examples:
1. Simple boolean values
    ```python
    is_active = True
    is_inactive = False
    ```

2. As a result of comparison
    ```python
    print(5 > 3)  # Output: True
    print(5 == 3)  # Output: False
    ```

3. In an `if` statement
    ```python
    is_hungry = True
    if is_hungry:
        print("Let's eat!")  # Output: Let's eat!
    ```

4. Result of functions that return a boolean
    ```python
    def is_even(number):
        return number % 2 == 0

    print(is_even(4))  # Output: True
    ```

#### Common Use Cases:
- Decision-making (`if`, `elif`, `else`)
- Loop conditions (`while`, `for`)
- To filter or check data

### If Statements

#### What it is:
The `if` statement is used to test a condition and execute code if the condition is true. You can also add `elif` and `else` blocks to test multiple conditions and execute different code accordingly.

#### Why you'd use it:
Use `if` statements for decision-making in your code. They help you perform different actions based on different conditions.

#### How to use it:
The syntax usually goes like this: `if condition: execute_this_code`

#### Examples:
1. Simple `if` statement
    ```python
    age = 25
    if age >= 21:
        print("You can drink!")
    ```

2. `if-else` statement
    ```python
    age = 17
    if age >= 21:
        print("You can drink!")
    else:
        print("Sorry, no drinks for you.")
    ```

3. `if-elif-else` statement
    ```python
    age = 18
    if age >= 21:
        print("You can drink and vote!")
    elif age >= 18:
        print("You can vote!")
    else:
        print("Sorry, you can't do much.")
    ```

4. Nested `if` statements
    ```python
    age = 22
    if age >= 18:
        print("You're an adult.")
        if age >= 21:
            print("You can also drink!")
    ```

#### Common Use Cases:
- Validating user input
- Checking data before processing it
- Making game logic decisions, like whether a player wins or loses

### The "In" Keyword

#### What it is:
The `in` keyword in Python is used to check if a value exists in a sequence (like a list, tuple, or string) or a collection (like a dictionary or set).

#### Why you'd use it:
You can use it to simplify code that checks for membership, making your code easier to read and maintain.

#### How to use it:
Simply use it between the item you're checking for and the collection you're checking within. It returns `True` if the item exists, otherwise `False`.

#### Examples:

1. Checking if an element is in a list:
    ```python
    fruits = ["apple", "banana", "cherry"]
    if "apple" in fruits:
        print("Apple exists!")
    ```

2. Checking if a key exists in a dictionary:
    ```python
    my_dict = {"name": "Scott", "age": 30}
    if "name" in my_dict:
        print("Name key exists!")
    ```

3. Checking if a substring exists in a string:
    ```python
    text = "Hello, World!"
    if "World" in text:
        print("World is in the text!")
    ```

4. Using `not in` to check if an item doesn't exist:
    ```python
    numbers = [1, 2, 3]
    if 4 not in numbers:
        print("4 is not in the list.")
    ```

#### Common Use Cases:
- Looking for specific values before processing data
- Triggering events when certain items are present in collections
- Conditional filtering of items

### Loops

#### What they are:
Loops are a way to repeatedly execute a block of code as long as a condition is met. This helps you avoid having to write the same code multiple times.

#### Why you'd use them:
Loops are great for tasks that are repetitive in nature. For instance, iterating through lists to find specific elements, or running a block of code until a user decides to stop.

#### Types of loops:

1. **For Loops**: Used to iterate over sequences (lists, tuples, dictionaries, sets, strings).
    ```python
    for item in [1, 2, 3]:
        print(item)  # Will print 1, then 2, then 3
    ```

2. **While Loops**: Run as long as a condition is true.
    ```python
    count = 0
    while count < 5:
        print(count)  # Will print 0, 1, 2, 3, 4
        count += 1
    ```

#### Examples:

1. **Iterating through a list**
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    ```

2. **Using `break` to exit a loop**
    ```python
    for num in [1, 2, 3, 4, 5]:
        if num == 3:
            break
        print(num)  # Will print 1, 2
    ```

3. **Using `continue` to skip an iteration**
    ```python
    for num in [1, 2, 3, 4, 5]:
        if num == 3:
            continue
        print(num)  # Will print 1, 2, 4, 5
    ```

4. **Using `enumerate` to get index and value**
    ```python
    for index, value in enumerate(["apple", "banana", "cherry"]):
        print(f"Index: {index}, Value: {value}")
    ```

5. **Nested Loops**
    ```python
    for x in [1, 2]:
        for y in ["a", "b"]:
            print(f"x: {x}, y: {y}")
    ```

#### Common Use Cases:
- Parsing and analyzing data
- Implementing algorithms
- Automating repetitive tasks

### List Comprehensions

#### What they are:
List comprehensions are a concise way to create lists in Python. Think of them as a one-liner that replaces a whole for-loop for list creation.

#### Why you'd use them:
List comprehensions make your code shorter and often more readable. They're handy when you want to generate a new list by performing some operation on each item in an existing list (or other iterable).

#### Syntax:
```python
[expression for item in iterable if condition]
```

1. **expression**: The value you want in the new list.
2. **item**: A variable that takes the value of each element in the iterable.
3. **iterable**: The original list, tuple, string, etc.
4. **condition**: A filtering condition (optional).

#### Examples:

1. **Create a list of squares**
    ```python
    squares = [x*x for x in range(1, 6)]  # Output: [1, 4, 9, 16, 25]
    ```

2. **Find even numbers in a list**
    ```python
    evens = [n for n in range(1, 11) if n % 2 == 0]  # Output: [2, 4, 6, 8, 10]
    ```

3. **Manipulate strings in a list**
    ```python
    upper_fruits = [fruit.upper() for fruit in ["apple", "banana", "cherry"]]  # Output: ['APPLE', 'BANANA', 'CHERRY']
    ```

4. **Nested List Comprehensions**
    ```python
    matrix = [[j for j in range(5)] for i in range(3)]
    # Output: [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
    ```

#### Common Use Cases:
- Quickly manipulating lists
- Data transformation
- Filtering data

### Dictionaries

#### What they are:
A dictionary in Python is a collection of key-value pairs. It's like a real-life dictionary where you look up a word (the key) to find its definition (the value).

#### Why you'd use them:
Dictionaries are great for organizing and managing data that can be mapped out with unique keys. They provide fast lookups and are super flexible.

#### Syntax:
```python
my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    ...
}
```

1. **key**: A unique identifier where you want to store some data.
2. **value**: The data you want to store.

#### Examples:

1. **Basic Dictionary**
    ```python
    dog = {'name': 'Gunner', 'breed': 'Tennessee treeing mountain curr', 'age': 3}
    ```

2. **Accessing Values**
    ```python
    print(dog['name'])  # Output: 'Gunner'
    ```

3. **Adding/Updating Key-Value Pairs**
    ```python
    dog['color'] = 'brown'
    ```

4. **Deleting a Key-Value Pair**
    ```python
    del dog['age']
    ```

5. **Iterating Through a Dictionary**
    ```python
    for key, value in dog.items():
        print(f"{key}: {value}")
    ```

#### Common Use Cases:
- Storing configurations
- Caching data
- Counting occurrences of words in a text file
- Representing real-world objects

Dictionaries are kinda like your toolbelt, keeping all your key-value "tools" organized and easy to grab

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
### Functions

#### What it is:
A function is like a mini-program within a program. It groups a set of statements so they can run more than once, and can also let us specify parameters that can serve as inputs.

#### Why you'd use it:
Functions help you to avoid writing the same code multiple times. Plus, if you need to make a change, you only have to update one spot instead of hunting down every occurrence in your code.

#### Syntax & Examples:

1. **Basic Function**
    ```python
    def greet():
        print("Hello, World!")
        
    greet()  # Output: "Hello, World!"
    ```

2. **Function with Parameters**
    ```python
    def greet(name):
        print(f"Hello, {name}!")
        
    greet("Scott")  # Output: "Hello, Scott!"
    ```

3. **Function with Return Values**
    ```python
    def add(a, b):
        return a + b
        
    result = add(3, 4)  # result = 7
    print(result)  # Output: 7
    ```

4. **Default Parameters**
    ```python
    def greet(name="World"):
        print(f"Hello, {name}!")
        
    greet()  # Output: "Hello, World!"
    greet("Scott")  # Output: "Hello, Scott!"
    ```

#### Common Use Cases:
- Code reuse and organization
- Input validation
- Calculations and data manipulation
- Grouping logic that belongs together

Think of a function like a recipe. You put in some ingredients (parameters), follow the steps (code inside the function), and get something delicious out (return value). It's a neat way to pack a bunch of instructions into a single, reusable line or block of code.
---

### Function Arguments and Parameters

#### What it is:
In Python, when you define a function, you can specify parameters that the function will take as input when called. Arguments are the actual values you pass in when you call a function that has parameters.

#### Why you'd use it:
Parameters allow your functions to be more flexible and reusable. You can write a single function that performs the same action on different data by using parameters. Arguments let you pass that varying data into your functions.

#### Syntax & Examples:

1. **Basic Function with Parameter**
    ```python
    def greet(name):  
        print(f"Hello, {name}!")
        
    greet("Scott")  # Output: "Hello, Scott!"
    ```

    In this example, `name` is a parameter and "Scott" is the argument you pass when you call the function.

2. **Multiple Parameters**
    ```python
    def add(a, b):
        print(a + b)

    add(3, 4)  # Output: 7
    ```

    Here, `a` and `b` are parameters, and 3 and 4 are the arguments.

3. **Default Parameter Values**
    ```python
    def greet(name="World"):
        print(f"Hello, {name}!")
        
    greet()  # Output: "Hello, World!"
    greet("Scott")  # Output: "Hello, Scott!"
    ```

    Default values let your function work even if some arguments are not provided.

#### Common Use Cases:
- To make your functions reusable for different inputs.
- To write cleaner, DRY (Don't Repeat Yourself) code.
- To make your code easier to understand and maintain.

---

### Default Parameter Values

#### What it is:
Default parameter values in Python functions allow you to set a default value for one or more parameters. This means if you don't provide a value for those parameters when calling the function, the default value will be used.

#### Why you'd use it:
Using default parameter values can make your functions more user-friendly and reduce the chance of errors. They allow optional customization while maintaining sensible default behavior.

#### Syntax & Examples:

1. **Basic Default Parameter**
    ```python
    def greet(name="World"):
        print(f"Hello, {name}!")
        
    greet()  # Output: "Hello, World!"
    greet("Scott")  # Output: "Hello, Scott!"
    ```
    If you don't pass an argument for `name`, it defaults to "World".

2. **Multiple Default Parameters**
    ```python
    def greet(name="World", punctuation="!"):
        print(f"Hello, {name}{punctuation}")
        
    greet()  # Output: "Hello, World!"
    greet("Scott", "?")  # Output: "Hello, Scott?"
    ```
    Here, both `name` and `punctuation` have default values.

3. **Mixing Default and Non-default Parameters**
    ```python
    def greet(greeting, name="World"):
        print(f"{greeting}, {name}!")
        
    greet("Hi")  # Output: "Hi, World!"
    greet("Hi", "Scott")  # Output: "Hi, Scott!"
    ```
    Note that default parameters should come after non-default parameters in the function definition.

#### Common Use Cases:
- Making your functions more flexible and easier to use.
- Reducing the chance of errors by having sensible defaults.
- Allowing optional functionality without requiring extra code.

---

### Returning Function Values

#### What it is:
The `return` keyword in Python allows a function to return a value back to the caller. This enables you to use the result of a function in other parts of your program.

#### Why you'd use it:
Returning values from a function lets you encapsulate some behavior and calculations, and then get the result for further operations or for displaying it to the user.

#### Syntax & Examples:

1. **Basic Return**
    ```python
    def add(a, b):
        return a + b
        
    result = add(3, 4)  # result = 7
    print(result)  # Output: 7
    ```
    The `add` function takes two parameters, adds them, and returns the sum.

2. **Returning Multiple Values**
    ```python
    def get_data():
        return "Scott", 25, "Developer"
        
    name, age, job = get_data()
    print(name, age, job)  # Output: Scott 25 Developer
    ```
    You can return multiple values as a tuple, and then unpack them.

3. **Conditional Return**
    ```python
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
            
    print(is_even(4))  # Output: True
    print(is_even(3))  # Output: False
    ```
    The function returns a boolean value based on a condition.

#### Common Use Cases:
- Getting the result of a calculation or data manipulation.
- Returning values for further use in your program, like conditionally executing code.
- Returning multiple related values as a single result (e.g., a tuple).

---

### Lambda Functions

#### What it is:
Lambda functions are small, anonymous (unnamed) functions defined using the `lambda` keyword. They're often used for quick, simple operations that can be defined in a single line of code.

#### Why you'd use it:
They are quick to write and can be used directly as an argument in functions like `sorted()`, `map()`, or `filter()` without formally defining a function using `def`.

#### Syntax & Examples:

1. **Basic Lambda**
    ```python
    add = lambda a, b: a + b
    print(add(3, 4))  # Output: 7
    ```
    This lambda function does the same as the `add` function in previous examples but in a more condensed form.

2. **Lambda in Built-in Functions**
    ```python
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16]
    ```
    The lambda function is used within the `map()` function to square each element in the list.

3. **Lambda with Multiple Arguments**
    ```python
    multiply = lambda a, b, c: a * b * c
    print(multiply(1, 2, 3))  # Output: 6
    ```
    You can have multiple arguments, but the expression must be a single one.

#### Common Use Cases:
- Simple data transformations in a quick and readable way.
- Passing a small piece of functionality as an argument to another function.
- Short, throwaway usage where a full function definition would be overly verbose.

---

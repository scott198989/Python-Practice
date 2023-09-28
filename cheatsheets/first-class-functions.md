### First-Class Functions

#### What it is:
In Python, functions are first-class citizens. This means you can assign them to variables, pass them as arguments to other functions, and return them from functions.

#### Why you'd use it:
Using first-class functions can make your code more flexible and modular. It allows for higher-order functions and can simplify complex operations.

#### Syntax & Examples:

1. **Assigning a Function to a Variable**
    ```python
    def greet():
        return "Hello, World!"

    my_greeting = greet
    print(my_greeting())  # Output: "Hello, World!"
    ```

2. **Passing Function as an Argument**
    ```python
    def shout(text):
        return text.upper()

    def whisper(text):
        return text.lower()

    def greet(func):
        greeting = func("Hello, World!")
        print(greeting)

    greet(shout)  # Output: "HELLO, WORLD!"
    greet(whisper)  # Output: "hello, world!"
    ```

3. **Returning a Function**
    ```python
    def get_greet_func(style):
        if style == 'loud':
            return shout
        else:
            return whisper

    my_func = get_greet_func('loud')
    print(my_func("hello"))  # Output: "HELLO"
    ```

#### Common Use Cases:
- Implementing decorators.
- Creating higher-order functions.
- Code that requires functional programming techniques, like map, filter, etc.

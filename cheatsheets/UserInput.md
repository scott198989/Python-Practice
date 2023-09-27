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
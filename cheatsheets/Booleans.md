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

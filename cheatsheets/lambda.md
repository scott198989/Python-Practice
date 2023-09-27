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
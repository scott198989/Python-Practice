### Multiple Default Parameters and Why It's a Bad Idea

#### What it is:
You can have multiple default parameters in a Python function. However, it can make your code harder to read and maintain, leading to potential bugs.

#### Why you'd use it:
While having multiple default parameters can provide flexibility, it also risks making the function too complex and harder to debug or understand.

#### Syntax & Examples:

1. **Multiple Default Parameters**
    ```python
    def complex_function(a=1, b=2, c=3, d=4):
        return a + b + c + d
        
    result = complex_function(5)  # Output: 5 + 2 + 3 + 4 = 14
    ```

2. **Hard to Trace**
    ```python
    def another_complex_function(a=1, b=2, c=3):
        # Imagine a lot of logic here
        return a * b + c

    result = another_complex_function(b=4)  # What will this return? Not so clear!
    ```

#### Common Use Cases:
- Not recommended for most cases due to readability and maintainability issues
- Could be used carefully when you are absolutely sure about the function's scope and usage

### Simple Decorators in Python

#### What it is:
A decorator is a function that takes another function as input and extends or alters its behavior without modifying its code.

#### Why you'd use it:
Decorators help you follow the DRY (Don't Repeat Yourself) principle. They allow you to add functionality to multiple functions without altering their source code.

#### Syntax & Examples:

1. **Basic Decorator**
    ```python
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()
    ```
    Output:
    ```
    Something is happening before the function is called.
    Hello!
    Something is happening after the function is called.
    ```

2. **Decorator as a Function**
    ```python
    def say_hello():
        print("Hello!")

    decorated_say_hello = my_decorator(say_hello)
    decorated_say_hello()
    ```
    This is functionally equivalent to using `@my_decorator` before `def say_hello()`.

#### Common Use Cases:
- Logging
- Authorization
- Memoization/caching
- Monitoring
- Enriching function behaviors (e.g., pre-processing, post-processing)

---

### The '@' Syntax for Decorators

#### What it is:
The '@' symbol, also known as the "pie" syntax, is a shorthand for applying decorators to a function.

#### Why you'd use it:
Using the '@' symbol makes your code cleaner and more readable, especially when you are using multiple decorators.

#### Syntax & Examples:

1. **Single Decorator**
    ```python
    @my_decorator
    def say_hello():
        print("Hello!")
    ```
    This is equivalent to:
    ```python
    def say_hello():
        print("Hello!")
        
    say_hello = my_decorator(say_hello)
    ```

2. **Multiple Decorators**
    ```python
    @another_decorator
    @my_decorator
    def say_hello():
        print("Hello!")
    ```
    This is equivalent to:
    ```python
    def say_hello():
        print("Hello!")
        
    say_hello = my_decorator(say_hello)
    say_hello = another_decorator(say_hello)
    ```

#### Common Use Cases:
- Code readability
- Simplifying the application of decorators
  
---

### Decorators with Parameters

#### What it is:
Sometimes you'll want to pass additional arguments to your decorator itself, rather than to the function it's decorating. This adds another layer of nesting to your decorator function.

#### Why you'd use it:
If you want your decorator to be more versatile and configurable, you'd use a decorator with parameters.

#### Syntax & Examples:

1. **Decorator with Parameters**
    ```python
    def repeat(n):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    func(*args, **kwargs)
            return wrapper
        return decorator
    
    @repeat(3)
    def say_hello(name):
        print(f"Hello, {name}!")
    ```

    Usage:
    ```python
    say_hello("Scott")  
    # Output:
    # Hello, Scott!
    # Hello, Scott!
    # Hello, Scott!
    ```

#### Common Use Cases:
- Retry logic
- Custom logging levels


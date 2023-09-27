### Magic Methods: `__str__` and `__repr__`

#### What it is:
Magic methods in Python are special methods that start and end with double underscores (`__`). They allow you to customize built-in behaviors for objects. `__str__` and `__repr__` are used for string representation of an object.

#### Why you'd use it:
- `__str__` is for the "informal" or "pretty" string representation of an object. Useful for end-users.
- `__repr__` is for the "formal" string representation of an object. Useful for debugging and development.

#### Syntax & Examples:

1. **Basic `__str__` Method**
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"This dog's name is {self.name}"

    my_dog = Dog("Gunner")
    print(str(my_dog))  # Output: "This dog's name is Gunner"
    ```

2. **Basic `__repr__` Method**
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"Dog(name='{self.name}')"

    my_dog = Dog("Gunner")
    print(repr(my_dog))  # Output: "Dog(name='Gunner')"
    ```

3. **Both Methods Together**
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"This dog's name is {self.name}"

        def __repr__(self):
            return f"Dog(name='{self.name}')"

    my_dog = Dog("Gunner")
    print(str(my_dog))  # Output: "This dog's name is Gunner"
    print(repr(my_dog))  # Output: "Dog(name='Gunner')"
    ```

#### Common Use Cases:
- Customizing how your object appears when converted to a string for user-friendly messages (`__str__`).
- Customizing the string output for debugging and logs (`__repr__`).


### Mutability

#### What it is:
In Python, some objects like lists and dictionaries are mutable, meaning they can be altered after creation. Others like strings and tuples are immutable, meaning once they're created, they can't be changed.

#### Why you'd use it:
Understanding mutability is crucial for avoiding bugs and effectively working with data structures.

#### Syntax & Examples:

1. **Mutable List**
    ```python
    my_list = [1, 2, 3]
    my_list[0] = 99
    print(my_list)  # Output: [99, 2, 3]
    ```

2. **Immutable String**
    ```python
    my_str = "hello"
    # my_str[0] = "H"  # This will throw an error
    my_str = "H" + my_str[1:]  # This is okay
    print(my_str)  # Output: "Hello"
    ```

#### Common Use Cases:
- Modifying lists or dictionaries in-place for performance gains
- Using immutable types for data integrity and safer programming

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
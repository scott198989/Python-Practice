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

### String Formatting

#### What it is:
String formatting is the process of inserting variables into a string to create a customized output. It's like having placeholders where your variables go, so you can change the variables without changing the string itself.

#### Why you'd use it:
String formatting is useful when you want to display messages that include variables. Like if you want to say "Hello, [Name]" and have it work for any name you provide.

#### How to use it:
Here are the main ways to format strings in Python:

1. **Concatenation**: Just stick strings together with `+`.
   ```python
   name = "Scott"
   print("Hello, " + name)
   ```

2. **% Formatting**: Old-school way but still valid.
   ```python
   name = "Scott"
   print("Hello, %s" % name)
   ```

3. **`.format()` Method**: More modern and flexible.
   ```python
   name = "Scott"
   print("Hello, {}".format(name))
   ```

4. **f-strings**: Latest and easiest way, only available in Python 3.6+.
   ```python
   name = "Scott"
   print(f"Hello, {name}")
   ```

#### Examples:
```python
age = 28
name = "Scott"

# Using .format() method
print("Hello, {}. You are {} years old.".format(name, age))

# Using f-string
print(f"Hello, {name}. You are {age} years old.")
```
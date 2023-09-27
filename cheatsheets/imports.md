### Imports in Python

#### What it is:
Importing allows you to bring in code from other Python files (modules) or libraries so you can use their functions, classes, or variables in your own code.

#### Why you'd use it:
Using imports, you can break up your code into multiple files for better organization, or utilize pre-built Python libraries to avoid re-inventing the wheel.

#### Syntax & Examples:

1. **Basic Import**
    ```python
    import math
    print(math.sqrt(25))  # Output: 5.0
    ```

2. **Import Specific Function or Class**
    ```python
    from math import sqrt
    print(sqrt(25))  # Output: 5.0
    ```

3. **Import and Rename**
    ```python
    import math as m
    print(m.sqrt(25))  # Output: 5.0
    ```

4. **Import Multiple Items**
    ```python
    from math import sqrt, pow
    print(pow(5, 2))  # Output: 25.0
    ```

#### Common Use Cases:
- To use built-in Python libraries or third-party libraries.
- To break your code into smaller, more manageable modules.
- To reuse code across multiple projects.

---

### Relative Imports in Python

#### What it is:
Relative imports allow you to import Python modules that are relative to the module you're working in. This is especially useful in bigger projects organized into packages (folders with an `__init__.py` file).

#### Why you'd use it:
Relative imports help you keep your project's internal dependencies clean, making it easier to manage the codebase.

#### Syntax & Examples:

1. **Same-Level Import**
    ```python
    # In a folder structure like:
    # my_package/
    # ├── module_a.py
    # └── module_b.py
    
    # Inside module_a.py
    from . import module_b  # . means the same folder level
    ```

2. **One-Level Up Import**
    ```python
    # In a folder structure like:
    # my_package/
    # ├── sub_package/
    # │   └── module_c.py
    # └── module_a.py
    
    # Inside module_c.py
    from .. import module_a  # .. means one folder up
    ```

3. **Specific Function or Class**
    ```python
    # Inside module_a.py
    from .module_b import some_function  # Import a specific function
    ```

#### Common Use Cases:
- In large projects, to maintain a clear internal dependency tree.
- When you want to rename or restructure modules without affecting the rest of the project.

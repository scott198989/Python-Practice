### Type Hinting in Python 3.5+

#### What it is:
Type hinting is the practice of annotating variables, class attributes, and function arguments and return values with their expected types. 

#### Why you'd use it:
Type hinting improves code readability and allows for better editor support with auto-completion and type checking. It's not enforced at runtime but can be checked using tools like `mypy`.

#### Syntax & Examples:

1. **Variable Type Hint**
    ```python
    name: str = "Scott"
    age: int = 32
    ```
  
2. **Function Argument and Return Type Hints**
    ```python
    def greet(name: str) -> str:
        return f"Hello, {name}"
    ```

3. **List and Dictionary Types**
    ```python
    from typing import List, Dict

    def process_scores(scores: List[int]) -> Dict[str, int]:
        return {"max": max(scores), "min": min(scores)}
    ```

4. **Optional Types**
    ```python
    from typing import Optional

    def get_employee(id: int) -> Optional[str]:
        # Code to fetch employee by id
        return None if not found
    ```

#### Common Use Cases:
- In large codebases to improve readability and maintainability.
- For better documentation.
- When you want to take advantage of type checking tools like `mypy`.

---
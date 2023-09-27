### `@classmethod` and `@staticmethod`

#### What it is:
In Python classes, you'll find three types of methods: instance methods, class methods, and static methods. `@classmethod` and `@staticmethod` are decorators that change the way methods behave in a class.

#### Why you'd use it:
- `@classmethod`: Useful when a method needs to interact with the class itself rather than instances of the class.
- `@staticmethod`: Useful for utility methods that don't need to access any class or instance-specific data.

#### Syntax & Examples:

1. **Class Method (`@classmethod`)**
    ```python
    class Dog:
        species = "Canine"
        
        @classmethod
        def get_species(cls):
            return cls.species

    print(Dog.get_species())  # Output: "Canine"
    ```

2. **Static Method (`@staticmethod`)**
    ```python
    class Dog:
        @staticmethod
        def bark(n):
            return "Woof! " * n

    print(Dog.bark(3))  # Output: "Woof! Woof! Woof! "
    ```

3. **Both Together**
    ```python
    class Dog:
        species = "Canine"
        
        @classmethod
        def get_species(cls):
            return cls.species
            
        @staticmethod
        def bark(n):
            return "Woof! " * n

    print(Dog.get_species())  # Output: "Canine"
    print(Dog.bark(2))  # Output: "Woof! Woof! "
    ```

#### Common Use Cases:
- You'd use `@classmethod` when you need to have methods that aren't concerned with instances but still need to know about the class itself.
- You'd use `@staticmethod` when you need a method that neither uses the class nor instance-specific data.

---

### Class Inheritance

#### What it is:
Inheritance is a way to form new classes using classes that have already been defined. The new class inherits attributes and behaviors (methods) from the parent class.

#### Why you'd use it:
To reuse code, reduce complexity, and build relationships between classes. It also helps in creating a logical structure for your code.

#### Syntax & Examples:

1. **Basic Inheritance**
    ```python
    class Animal:
        def make_sound(self):
            return "Some generic sound"

    class Dog(Animal):
        def make_sound(self):
            return "Woof"

    dog = Dog()
    print(dog.make_sound())  # Output: "Woof"
    ```

2. **Inheritance with `super()`**
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name

    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name)
            self.breed = breed

    dog = Dog("Gunner", "Tennessee Treeing Mountain Cur")
    print(dog.name, dog.breed)  # Output: "Gunner Tennessee Treeing Mountain Cur"
    ```

3. **Multiple Methods**
    ```python
    class Animal:
        def eat(self):
            return "This animal eats food."

    class Dog(Animal):
        def bark(self):
            return "Woof!"

    dog = Dog()
    print(dog.eat())  # Output: "This animal eats food."
    print(dog.bark())  # Output: "Woof!"
    ```

#### Common Use Cases:
- Reusing common logic between classes.
- Extending the functionality of existing classes without modifying them.
- Organizing code into a hierarchy to model real-world relationships.

---

### Class Composition

#### What it is:
Class Composition is a way to combine simple classes to build more complex ones. Instead of inheriting attributes and behaviors, a class is composed of references to other classes.

#### Why you'd use it:
Composition allows you to reuse code in a modular fashion. It's often favored over inheritance when you want to build classes that are more loosely coupled and easier to maintain.

#### Syntax & Examples:

1. **Basic Composition**
    ```python
    class Engine:
        def start(self):
            return "Engine started"

    class Car:
        def __init__(self):
            self.engine = Engine()
        
        def start(self):
            return self.engine.start()

    my_car = Car()
    print(my_car.start())  # Output: "Engine started"
    ```

2. **Composition with Multiple Objects**
    ```python
    class Wheel:
        def inflate(self):
            return "Wheel inflated"

    class Car:
        def __init__(self):
            self.engine = Engine()
            self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
        
        def inflate_wheels(self):
            for wheel in self.wheels:
                print(wheel.inflate())

    my_car = Car()
    my_car.inflate_wheels()  # Output: "Wheel inflated" four times
    ```

#### Common Use Cases:
- When you want to model "has-a" relationships as opposed to "is-a" relationships.
- When you need to combine functionalities of independent classes.
- To achieve greater flexibility and maintainability in code structure.

---

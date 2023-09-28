x = 15

price = 9.99

discount = 0.2

result = price * (1 - discount)

print(result)

name = "Rolf"

print(name)

print(name * 2)

a = 25
b = a
print(a)
print(b)
b = 17
print(b)

longer_phrase = "Hello, {}. Today is {}."

formated = longer_phrase.format("Rolf", "Monday")

print(formated)

name = input("what is your name?")

size_input = input("How big is your house(in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"This many {square_feet} equals this many {square_meters:.2}")

l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

l[0] = "Smith"
l.append("Smith2")
l.remove("Smith")
s.add("Smith")
print(s)

                
                
                        # SETS

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = abroad.difference(abroad)
print(local_friends)


local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art&science
print(both)



                        # Booleans 

age = input("What is your age?")
age = int(age)

if age >= 21:
    print("You are old enough to vote, drink, and drive.  Just dont do all at the same time, ok?")
elif age >= 18:
    print("You can vote and you can drive. SWEET!")
elif age >= 16:
    print("Well, you can drive, so not bad. Gas prices are horrible though.")
else:
    print("Sorry little buddy, you cant vote, drink or drive. Go watch cartoons or something")




                # Conditional Statements (if, elif, else)

day_of_the_week = input("What day of the week is it?").lower()

if day_of_the_week == "friday": 
    print ("Its the weekend!")
else:
    print("Gotta do more Udemy classes!")



                        # The "in" keyword

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you have watched recently.")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I havent seen that yet, NO SPOILERS!")
    
    
    

                    # Magic Number Challenge / While loop

number = 7

while True:
    user_input = input("Enter 'Y/n' if you would like to play")
    if user_input == "n":
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1:
        print("close, your off by one")
    else:
        print("Doh!")



                        # For Loops

friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade
print(total/amount)




                        # Lists comprehension 

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s", id(starts_s))



                # Dictionaries

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20
print(friend_ages["Adam"])


friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
    
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class")
    
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

                    
                    
                    
                    # Destructuring Variables
                    
t = 5, 11

x, y = t

print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession {person[2]}")

person = ("Bob", 42, "Mechanic")

name, _, profession = person

print (name, profession)

head, *tail = [ 1, 2, 3, 4, 5]

print(head)
print(tail)



                    # Functions
# Define the function   
def hello():
    print("Hello")
    
# Call the function

hello()

print("Welcome to the age in seconds program!")

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")
    
    
user_age_in_seconds()
    
print("See ya!")



                        # Function Parameters
                        
def add(x, y):
    result = x + y
    print(result)
add(5, 3)


                        # Adding Arguments  
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname = "Bob", name = "Smith")
    
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")
        
divide(dividend=0, divisor=15)


                        # Default parameter values
                        
def add (x=5, y=8):
    print(x+y)
    
add(5, 8)


                        #  Functions and returning values
                        
def add (x=5, y=8):
    print(x +y)
    return x + y
    
add(5, 8)
result = add(5, 8)
print(result)

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"
    
result = divide(15, 2) * 5
print(result)
    

                        #LAMBDA Functions
# 4 parts, lambda key word, arguments, semi colon, return value, and can store in a variable 

add = lambda x, y: x + y

print(add(5, 7)) 

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)


                        # Dictionary Comprehensions
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}

username_input = input("enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your detials are correct.")
else:
    print("Your details are incorrect.")


                            # Unpacking Arguements 

def multiply(*args):
    print(args)
    total = 1 
    for arg in args:
        total = total * args
    return total
    
print(multiply(-1))

def add(x, y):
    return x + y

nums = [3, 5]
add(nums)

def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}
print(add(**nums))

def multiply(*args):
    print(args)
    total = 1 
    for arg in args:
        total = total * args
    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply."
    
    
    print(apply(1, 3, 6, 7, operator="*"))

                        #Unpacking keyword arguements 
                        
def named(**kwargs):
    print(kwargs)
    
named(name="Bob", age=25)

def named(**kwargs):
    print(kwargs)
    
details = {"name": "Bob", "age": 25}

named(**details)
    
def named(**kwargs):
    print(kwargs)
    
def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
    
print_nicely(name="Bob", age=25)

def both(*args, **kwargs):
    print(args)
    print(kwargs)
    
both(1, 3, 5, name="Bob", age=25)

def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)


                # OOP (Object Oriented Programming)
                
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (100, 40, 83, 48, 90))
student3 = Student("Lana", (100, 90, 73, 88, 90))
student4 = Student("Ashley", (100, 100, 100, 100, 90))


print(student2.name)
print(student2.average())


                    # Magic Methods _str_ and _repr_
                    
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Person ({self.name}, {self.age}) years old"
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"
    
bob = Person("Bob", 35)
print(bob)

#                # @class method and @static method

class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static method.")

ClassTest.static_method
ClassTest.class_method()
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
print(book)
print(light)


                                   # Class Inheritance

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by 
        self.connected = True
        
    def __str__(self):
        return f"Device {self.name} ({self.connected_by})" 
        
    def disconnect(self):
        self.connected = False
        print("Disconnected")
  
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
        
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"  
    
    def print(self, pages):  
        if not self.connected:
            print("Your printer is not connected")
            return 
        print(f"Printing {pages} pages")  
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

printer.disconnect
        
        
                                   # Class Composition
                                    
class BookShelf:
    def __init__(self, *books):  
        self.books = books
        self.quantity = len(books)
        
    def __str__(self):
        return f"Bookshelf with {self.quantity} books."  

class Book:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)

    
                                           # TYPE Hinting
                                            
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)

                                          # Imports

def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py: ", __name__)

from mymodule import divide

mymodule.divide
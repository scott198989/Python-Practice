# x = 15

# price = 9.99

# discount = 0.2

# result = price * (1 - discount)

# print(result)

# name = "Rolf"

# print(name)

# print(name * 2)

# a = 25
# b = a
# print(a)
# print(b)
# b = 17
# print(b)

# longer_phrase = "Hello, {}. Today is {}."

# formated = longer_phrase.format("Rolf", "Monday")

# print(formated)

# name = input("what is your name?")

# size_input = input("How big is your house(in square feet): ")
# square_feet = int(size_input)
# square_meters = square_feet / 10.8
# print(f"This many {square_feet} equals this many {square_meters:.2}")

# l = ["Bob", "Rolf", "Anne"]
# t = ("Bob", "Rolf", "Anne")
# s = {"Bob", "Rolf", "Anne"}

# l[0] = "Smith"
# l.append("Smith2")
# # l.remove("Smith")
# s.add("Smith")
# print(s)

                
                
                # SETS

# friends = {"Bob", "Rolf", "Anne"}
# abroad = {"Bob", "Anne"}

# local_friends = abroad.difference(abroad)
# print(local_friends)


# local = {"Rolf"}
# abroad = {"Bob", "Anne"}

# friends = local.union(abroad)
# print(friends)

# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Jen", "Adam", "Anne"}
# both = art&science
# print(both)


#           
# 
#           Booleans 

# age = input("What is your age?")
# age = int(age)

# if age >= 21:
#     print("You are old enough to vote, drink, and drive.  Just dont do all at the same time, ok?")
# elif age >= 18:
#     print("You can vote and you can drive. SWEET!")
# elif age >= 16:
#     print("Well, you can drive, so not bad. Gas prices are horrible though.")
# else:
#     print("Sorry little buddy, you cant vote, drink or drive. Go watch cartoons or something")


# Conditional Statements (if, elif, else)

# day_of_the_week = input("What day of the week is it?").lower()

# if day_of_the_week == "friday": 
#     print ("Its the weekend!")
# else:
#     print("Gotta do more Udemy classes!")


#           
# 
#           The "in" keyword

# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you have watched recently.")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I havent seen that yet, NO SPOILERS!")

# Magic Number Challenge / While loop

# number = 7

# while True:
#     user_input = input("Enter 'Y/n' if you would like to play")
#     if user_input == "n":
#         break
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly")
#     elif abs(number - user_number) == 1:
#         print("close, your off by one")
#     else:
#         print("Doh!")



#                For Loops

# friends = ["Rolf", "Jen", "Bob", "Anne"]

# for friend in friends:
#     print(f"{friend} is my friend")

# grades = [35, 67, 98, 100, 100]
# total = 0
# amount = len(grades)

# for grade in grades:
#     total += grade
# print(total/amount)

# Lists comprehension 

# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = [friend for friend in friends if friend.startswith("S")]

# print(friends)
# print(starts_s)
# print(friends is starts_s)
# print("friends: ", id(friends), "starts_s", id(starts_s))



                # Dictionaries

# friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
# friend_ages["Bob"] = 20
# print(friend_ages["Adam"])


# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30},
#     {"name": "Anne", "age": 27}
# ]

# print(friends[1]["name"])

# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")
    
# if "Bob" in student_attendance:
#     print(f"Bob: {student_attendance['Bob']}")
# else:
#     print("Bob is not a student in this class")
    
# attendance_values = student_attendance.values()
# print(sum(attendance_values) / len(attendance_values))

                    # Destructuring Variables
                    
# t = 5, 11

# x, y = t

# print(x, y)

# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# print(list(student_attendance.items()))

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")

# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

# for person in people:
#     print(f"Name: {person[0]}, Age: {person[1]}, Profession {person[2]}")

# person = ("Bob", 42, "Mechanic")

# name, _, profession = person

# print (name, profession)

head, *tail = [ 1, 2, 3, 4, 5]

print(head)
print(tail)
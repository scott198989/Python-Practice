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


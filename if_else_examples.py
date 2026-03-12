# if_else_examples.py

# Basic if / else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")


# Using elif (else if)

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# Comparing two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is bigger")
else:
    print("Second number is bigger or equal")
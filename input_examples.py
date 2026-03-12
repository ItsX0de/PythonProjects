# input_examples.py

# input() lets the user type something into the program
# The vaue the user types gets sstored in a variable

name = input("Enter your name: ")
print("Hello", name)

# input() always returns a STRING (text)

age = input("Enter your age: ")
print("Your age is", age)
print(type(age)) #This shows the data type

#If we want to do math, we convert the input to an integer

number = int(input("Enter a number: "))
print("Your number doubled is:", number * 2)

# We can ask for multiple inputs

city = input("What city do you live in? ")
food = input("What is your favourite food? ")

print("You live in", city)
print("Your favourite food is", food)

# Small example program

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 + num2 

print("The result is:", result)
# logical_examples.py

# AND
# Both conditions must be true

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("You can enter")
else:
    print("You cannot enter")


# OR
# Only one condition needs to be true

day = input("Is it Saturday or Sunday? ")
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")
    

# NOT
# Reverses a condition

is_raining = input("Is it raining? (yes/no): ")
 
if not is_raining == "yes":
   print("You don't need an umbrella")
else:
   print("Take an umbrella")
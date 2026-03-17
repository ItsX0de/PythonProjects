number = 21

guess = int(input("Guess my number :"))

while guess != number:
  if guess > number:
    print("Too high!")
    guess = int(input("Guess my number :"))
  elif guess < number:
    print("Too low!")
    guess = int(input("Guess my number :"))

print("Congratulations!")
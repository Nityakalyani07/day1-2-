import random

target = random.randint(1, 20)
guess = 0
print("Guess the number between 1 and 20!")
while guess != target:
    guess = int(input("Your guess: "))
    if guess < target: print("Too low!")
    elif guess > target: print("Too high!")
print("Yay! You guessed it!")


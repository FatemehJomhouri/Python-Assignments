import random

number = random.randint(1, 20)
guess = 0
attempts = 0
name = input("Welcome to the Game, may I know your name?")
print("Well,", name, "I chose a number between 1-20 and you should make guesses")
while True:
    guess = int(input("Guess a number"))
    attempts += 1
    if guess == number:
        print("Yay! Great", name)
        print("You guessed for", attempts, "times")
        break
    else:
        if guess < number:
            print("Oops! try a higher number.")
        else:
            print("Oops! try a lower number.")
        continue



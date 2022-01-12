import random

number = random.randint(1, 9)

print("Number Guessing Game! \n Guess a number between 1 and 9")
chances = 0
guess = None

while guess != number:
    guess = input("Enter your guess:")
    guess = int(guess)

    if guess > number:
        print("Nope, your guesss was too high: Guess a number lower than ", guess)
        chances = chances + 1 
        #break  
    elif guess < number:
        print("Nope, your guesss was too low: Guess a number higher than ", guess)
        chances = chances + 1   
        #break
    else:
        print("good job you won the game!")
        break

    if not chances < 5:
        print("YOU LOSE!!! the number is ", number)



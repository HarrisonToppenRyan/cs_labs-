# Author: Harrison Toppen-Ryan
# Description : Lab 4, CSCI 141
# Date: October 24th, 2020

# Ensuring a random number and use for the random.radint between the lower and upper bound
import random 

# First Text and asking player for thier bounds 
print("Let's play a guessing game")
print("First seect a range from which I'll select a random number")
lowerBound = int(input("What is the lower bound? "))
upperBound = int(input("What is the upper bound? "))

# If the bound is more then 10 numbers apart 
if upperBound - 10 >= lowerBound:
    guessesAsk = int(input("How many guesses would you like? "))
    guessesLeft = guessesAsk
    tries = 1 
    # Random number choosen between the lower and upper bounds 
    guessNumber = int(random.randint(lowerBound, upperBound))

    # Definning what happens when a player runs out of guesses or guesses correctly
    def outOfGuesses():
        
        global guessesLeft
        # when the number of guesses run out 
        if guessesLeft == 0:
            print("You lose. The correct number was ", guessNumber)
            raise SystemExit

        # when the player still have guesses left 
        else:
            global tries 
            print("You guessed incorrectly. Try again. ")
            print("Guess number", tries)
            guess1 = int(input("What is your guess? "))

            if guess1 == guessNumber:
                #If player guesses correctly 
                print("You've guessed correctly. Win!")
                raise SystemExit
            else:
                #If the guess was incorrect 
                guessesLeft -= 1
                tries += 1
                #calls the function above 
                outOfGuesses()
                
                
    # Text telling the play info about the number guessed 
    print("I've guessed a random number between ", lowerBound, "and", upperBound)
    print("Let's begin. Good luck.")
    print("Guess number 1")

    # For loop that keeps track of how many guesses the player has left
    for i in range(0, guessesAsk):
        guess1 = int(input("What is your guess? "))
        guessNumber = int(random.randint(lowerBound, upperBound))
        
        if guess1 == guessNumber:
            print("You've guessed correctly. Win!")
            raise SystemExit
        else: 
            guessesLeft -= 1 
            tries += 1
            # calls the function above 
            outOfGuesses()


# If the bound is not more then 10 numbers apart 
else:
    print("The numbers are not at least 10 integers apart")
    print("Quitting")
    raise SystemExit

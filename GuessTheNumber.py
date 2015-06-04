# Create a program that generates a random number from 1 to 100(inclusive).
# Let a user make 7 guesses.
# Let the user know if they guess too high or too low and how many guesses
# they have left.

#import the required modules
import random

#function for getting a guess from user with error checking
def get_guess():
    a = True
    while a:
        try:
            guess = int(raw_input("Please enter your guess: "))
            a = False
        except ValueError:
            print "That is not an number."
    return guess

#function for friendly greeting
def greeting():
    print "Welcome to the number guessing game! \n\
    You will have 7 chances to guess my number! \n\
    Ready? I have picked a number between 1 and 100. \n\
    Let's begin!"

#function for the actual guessing game!
def guessgame():
    #run greeting function
    greeting()
    #get random number
    mynumber = random.randint(1, 100)
    #set counter variable
    num_of_guess = 1

    #while loop to check user guess
    while num_of_guess < 8:
        user_guess = get_guess()

        if user_guess == mynumber:
            print "You win! Congrats! It took you %s guesses." % num_of_guess
            num_of_guess = 8
        elif num_of_guess >= 7:
            print "You ran out of guesses! The number was %s" % mynumber
            num_of_guess = 8
        elif user_guess < mynumber:
            print "Your guess is too low. Try again!\nGuess number %s out of 7" % num_of_guess
            num_of_guess += 1
        elif user_guess > mynumber:
            print "Your guess is too high. Try again!\nGuess number %s out of 7" % num_of_guess
            num_of_guess += 1

guessgame()

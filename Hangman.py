# Goal
# Create a program that selects a random word and then allows the user to guess it in a game of hangman.
# Like the real game, there should be blank spots for each letter in the word, and a part of the body should
# be added each time the user guesses a letter than is not in the answer (you may choose how many wrong turns
# the user can make until the game ends).
# Subgoals
# If the user loses, print out the word at the end of the game.
# Create a "give up" option.
import urllib2
import random
import time

class Hangman(object):
    def __init__(self):
        self.word = ''
        self.counter = 10
        self.hidden_word_list = []
        self.word_list = []


    def set_random_word(self, length=6):
        """
        choose a random word from my local dictionary, defaults to 6 characters.
        """
        word_file = "/usr/share/dict/words"
        word_list = open(word_file).read().splitlines()
        narrow_word_choice = [x for x in word_list if len(x) <= length]
        self.word = random.choice(narrow_word_choice)



    def welcome_message(self):
        print "Welcome to the Hang man game!\n" \
              "You will have 10 chances to guess the word!\n" \
              "Ready?\n" \
        #TODO UI for word length choice
        self.menu_countdown()


    def menu_countdown(self):
        timer = 0.00
        a = "."
        while timer < 2.25:
            time.sleep(.25)
            print a
            timer += .25
            a += "."


    def set_hidden_word_list(self):
        self.hidden_word_list = list(self.word)

    def start_game(self):
        pass



new = Hangman()
word = new.set_random_word(8)
print new.word
# new.welcome_message()
new.set_hidden_word_list()
print new.hidden_word_list

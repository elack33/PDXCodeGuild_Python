# Goal
# Create a program that selects a random word and then allows the user to guess it in a game of hangman.
# Like the real game, there should be blank spots for each letter in the word, and a part of the body should
# be added each time the user guesses a letter than is not in the answer (you may choose how many wrong turns
# the user can make until the game ends).
# Subgoals
# If the user loses, print out the word at the end of the game.
# Create a "give up" option.
# import urllib2
import random
import time

class Hangman(object):
    def __init__(self):
        self.word = ''
        self.counter = 10
        self.hidden_word_list = []
        self.word_list = []
        self.guessed_letters = []
        self.start_game()

    def set_random_word(self, length=6):
        """
        choose a random word from my local dictionary, defaults to 6 characters and greater than 2
        """
        word_file = "/usr/share/dict/words"
        word_list = open(word_file).read().splitlines()
        narrow_word_choice = [x for x in word_list if len(x) <= length and len(x) > 2]
        self.word = random.choice(narrow_word_choice)
        self.word = self.word.lower()

    def welcome_message(self):
        welcome = "Welcome to the Hang man game!\n" \
                  "You will have 10 chances to guess the word!\n" \
                  "Each ^ is a letter to guess!\n" \
                  "Let's play!"
        # TODO UI for word length choice
        # self.menu_countdown()
        return welcome

    def menu_countdown(self):
        """
        little count down timer that looks neat.
        """
        timer = 0.00
        a = "."
        while timer < 1.51:
            time.sleep(.25)
            print a
            timer += .25
            a += "."

    def set_hidden_word_list(self):
        """
        hidden word holds the actual word in a list of characters to be compared against
        when the user guesses.
        loads the self.word_list with equal amount of blanks.
        """
        self.hidden_word_list = list(self.word)
        for x in self.hidden_word_list:
            self.word_list += '^'

    def guess(self, letter):
        for i, x in enumerate(self.hidden_word_list):
            if x == letter:
                self.word_list[i] = self.hidden_word_list[i]
            # else:
            #     self.guessed_letters.append(x)
            #     self.counter -= 1
                pass
        if letter not in self.word_list:
            self.counter -= 1
            self.guessed_letters.append(letter)

    def start_game(self):
        print self.welcome_message()
        self.set_random_word()
        self.set_hidden_word_list()
        self.play()

    def set_guess(self):
        letter = raw_input("Guess a letter: ")
        self.guess(letter)
        # TODO check self.guessed if the letter already used
        # TODO check self.word_list to see if the letter already used

    def show_word(self):
        guesses = ''.join(self.word_list)
        print guesses
        print self.word

    def play(self):
        while self.counter > 0:
            if self.hidden_word_list != self.word_list:
                self.show_word()
                self.set_guess()
                # self.counter -= 1
                print self.counter
                print "Guessed letters: ", ' '.join(self.guessed_letters)
                # TODO counter show function
            # elif self.counter == 0:
            #     print "You loose!"
            #     break
            #     # TODO Make a you loose function
            else:
                # TODO You win function
                print "You win!"
                break
        print "You loose."
        # TODO you loose function




new = Hangman()
# word = new.set_random_word(8)
# print new.word
# # new.welcome_message()
# new.set_hidden_word_list()
# print new.hidden_word_list
# print new.word_list



# Unit Tests
# from types import *
#
# def test_welcome_message():
#     game = Hangman()
#     message_test = game.welcome_message()
#
# def test_guess():
#     game = Hangman()
#     game.set_guess()
#     assert type(message_test) is StringType, "guess is not a string: %r" % message_test
#
# test_welcome_message()


# self.welcome_message()
# self.set_random_word()
# self.set_hidden_word_list()
# self.start_game()
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


    def set_random_word(self):
        # word_site = "http://www.freebsd.org/cgi/cvsweb.cgi/src/share/dict/web2?rev=1.12;content-type=text%2Fplain"
        # response = urllib2.urlopen(word_site)
        # txt = response.read()
        # word_list = txt.splitlines()
        word_file = "/usr/share/dict/words"
        word_list = open(word_file).read().splitlines()
        self.word = random.choice(word_list)


    def welcome_message(self):
        print "Welcome to the Hang man game!\n" \
              "You will have 10 chances to guess the word!\n" \
              "Ready?\n" \
              "Choosing random word!"
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
word = new.set_random_word()
print new.word
# new.welcome_message()
new.set_hidden_word_list()
print new.hidden_word_list

__author__ = 'darwright'
"""
made a little program to read ina  text file full of python challenges to and randomize them so i can
pick a new challenge to work on randomly.
QUatin list from:
https://github.com/zhiwehu/Python-programming-exercises
"""

class PickAProject(object):

    def __init__(self):
        self.level_1 = []
        self.level_2 = []
        self.level_3 = []


    def read_file(self):
        """
        read in the file
        """
        filename = 'challenge_import.txt'
        with open(filename) as load_import_data:
            for line in load_import_data:
                if line == '#----------------------------------------#':
                    if line in 'Question':



    def parse_data(self):
        """
        sort the data into beginning, intermediate and complex projects
        """
        pass

    def random_pick(self):
        """
        pick a random project to work and export it into a file for tracking.
        """
        #TODO someday make this a DB to keep track of what projects ive worked on already.
        pass








# Boggle


# H    J    M    A
# V    B    E    N
# T    W    P    E
# R    Q    A    I

import string
import random
import sys

boggle_game = raw_input("Welcome to Boggle! Please type 'start' when ready to play! When ready to quit, please type 'q' ")


# create board
board = []
for row in range(4):
    r = []
    for column in range(4):
        letter = random.choice(string.ascii_uppercase)
        r.append(letter)
    board.append(r)

# create vocabulary
fname = 'vocabulary.txt'
with open(fname) as f:
    vocabulary = f.read().splitlines()


def is_adjacent(coords1, coords2):
    """
    Checks if 2 pairs of coordinates are adjacent to each other in a 2-dimensional grid
    :param coords1: one set of coordinates
    :param coords2: other set of coordinates
    :return: True or False depending on if coords1 and coords2 are adjacent or not
    """
    delta_x = abs(coords1[0] - coords2[0])
    delta_y = abs(coords1[1] - coords2[1])
    return delta_x <= 1 and delta_y <= 1


def coordinates_for_letter(letter, board):
    """
    For a given board, find the coordinates (x, y) of a given letter
    :param letter: letter we're trying to find
    :param board: board in which we are trying to find letter (2 dimensional array)
    :return: list of tuples of coordinates in format (x, y)
    """
    letter = letter.upper()
    coordinates = []
    for y, row in enumerate(board):
        if letter in row:
            occurences = [x for x, row_letter in enumerate(row) if row_letter == letter]
            for x in occurences:
                coordinates.append((x, y))

    return coordinates


def word_on_board(word, board):
    """
    Checks if word is valid within board.
    :param word: word to check for
    :param board: game board to check within
    :return: True or False depending on if valid move or not
    """
    previous_coordinates = None

    for letter in word:
        current_coordinates = coordinates_for_letter(letter, board)

        if previous_coordinates:
            adjacent = []
            for p_coord in previous_coordinates:
                for c_coord in current_coordinates:
                    if is_adjacent(p_coord, c_coord):
                        adjacent.append(c_coord)
            previous_coordinates = adjacent
        else:
            previous_coordinates = current_coordinates

        if not previous_coordinates:
            return False

    return True


# game loop
score = 0

def print_board(board):
    for row in board:
        print row

def word_score(word):
    length = len(word)
    if length == 3 or length == 4:
        return 1
    if length == 5:
        return 2
    if length == 6:
        return 3
    if length == 7:
        return 5
    if length >= 8:
        return 11

while True:
    print_board(board)
    word = raw_input('Enter a word: ')
    # make sure word length is greater than 3
    if word == 'q':
        print "Thanks for playing!"
        sys.exit()

    if len(word) < 3:
        print 'Word must be 3 or more letters.'
        print
        continue

    # make sure word is in our vocabulary
    if word not in vocabulary:
        print 'Not a valid word!'
        print
        continue

    # make sure word is a valid move:
    if word_on_board(word, board):
        score += word_score(word)
        print "Good job! " + "Current Score: " + str(score)
        print
    else:
        print "Not a valid word on the Board"
        print

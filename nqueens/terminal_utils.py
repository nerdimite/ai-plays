'''
ANSI Codes Reference https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
'''

import sys


def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def move(n, direction):
    '''Move to a particular position in the terminal
    Args:
        n (int): Number of positions to move
        direction (str): Direction to move in the terminal
    '''
    if direction == 'up':
        write(f"\033[{n}A")
    elif direction == 'down':
        write(f"\033[{n}B")
    elif direction == 'right':
        write(f"\033[{n}C")
    elif direction == 'left':
        write(f"\033[{n}D")

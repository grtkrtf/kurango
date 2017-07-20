from lexicon import lexicon
import os
from pprint import pprint

os.system('cls' if os.name == 'nt' else 'clear')  # clears the terminal
print """
Interactive English-Kurango Dictionary
written by Garret Kurteff, Jul 1 2015 v0.1
Press RETURN to continue, or CTRL+C (^C) to quit.
"""
raw_input("> ")

os.system('cls' if os.name == 'nt' else 'clear')  # clears the terminal
print """
To use this dictionary, type in an English word.
The corresponding Kurango word will be displayed.
"""
# don't make it do this please.
pprint (lexicon, width=1)

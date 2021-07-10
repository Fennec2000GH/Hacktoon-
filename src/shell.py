
import emoji, os, sys
from pprint import pprint
from subprocess import Popen, PIPE
from termcolor import colored, cprint

# GLOBAL VARIABLES
colors = set([
    'grey',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white'
])

text_highlights = set([
    'on_grey',
    'on_red',
    'on_green',
    'on_yellow',
    'on_blue',
    'on_magenta',
    'on_cyan',
    'on_white'
])

attrs = set([
    'bold',
    'dark',
    'underline',
    'blink',
    'reverse',
    'concealed'
])

# pprint(sys.argv)

# while(True):

#     user_input = input(emoji.emojize(string=':thumbs_up:\t'))

#     print(colored(text=user_input, color='red', attrs=['reverse', 'blink']))
#     pipe = Popen(args=user_input.split(), stdout=PIPE)
#     output = pipe.communicate()[0].decode(encoding='UTF-8').split()
#     for line in output:
#         pprint(line)

print("\U0001f600")

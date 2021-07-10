
import emoji, os, sys, time
from pprint import pprint
from pynput.keyboard import Key, Controller, Listener
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

command_history = list()
output_history = list()

keyboard = Controller()

def on_press(key):
  print(key)

def on_release(key):
  pprint(key)

# with Listener(on_press=on_press) as listener:
#   listener.join()

while(True):

    user_input = input(emoji.emojize(string=':growing_heart:\t'))
    command_history.append(colored(text=user_input, color='red'))

    pipe = Popen(args=user_input.split(), stdout=PIPE)
    output = pipe.communicate()[0].decode(encoding='UTF-8').split()
    for line in output:
        formatted_line = colored(text=emoji.emojize(string=':bow_and_arrow:\t' + line), color='magenta')
        output_history.append(formatted_line)
        print(formatted_line)

  
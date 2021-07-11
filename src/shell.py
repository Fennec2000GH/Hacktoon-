
import emoji, os, sys, time
from pprint import pprint
from pynput.keyboard import Key, Controller, Listener
from subprocess import Popen, PIPE
from termcolor import colored, cprint

from nlp_map import emoji_commands, translate_emoji
# GLOBAL VARIABLES
# termcolor options
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

# stored collections
aliases = dict()
command_history = list()
output_history = list()

keyboard = Controller()

def on_press(key):
  print(key)

def on_release(key):
  pprint(key)

# with Listener(on_press=on_press) as listener:
#   listener.join()

# REPL loop
while(True):

  # collect user input
  user_input = input(emoji.emojize(string=':growing_heart:\t'))
  command_history.append(colored(text=user_input, color='red'))
  cprint(text=user_input, color='red')

  user_input_formatted = None

  # determine whther original user input is already a valid command
  try:
    pipe = Popen(args=user_input.split(), stdout=PIPE)
    output = pipe.communicate()[0].decode(encoding='UTF-8').split()
    for line in output:
      formatted_line = colored(text=emoji.emojize(string=':bow_and_arrow:\t' + line), color='magenta')
      output_history.append(formatted_line)
      print(formatted_line)
    continue

  except Exception as err:
    # convert emojis into valid commands
    user_input_formatted = ''.join(list([translate_emoji(emoji=char) if ord(char) > 127 else char for char in user_input]))
    pprint(user_input_formatted)


  # determine whether emoji-translated user input is a valid command
  try:
    pipe = Popen(args=user_input_formatted.split(), stdout=PIPE)
    output = pipe.communicate()[0].decode(encoding='UTF-8').split()
    for line in output:
      formatted_line = colored(text=emoji.emojize(string=':bow_and_arrow:\t' + line), color='magenta')
      output_history.append(formatted_line)
      print(formatted_line)
    continue

  except Exception as err:
    # convert natural language into nearest valid command
    pprint('NLP time!')

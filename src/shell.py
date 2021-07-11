
import emoji, os, random, sys
from pprint import pprint
from pynput.keyboard import Key, Controller, Listener
from subprocess import Popen, PIPE
from termcolor import colored, cprint

from nlp_map import emoji_commands, natural_language_commands, translate_emoji, predict_command

# GLOBAL VARIABLES
# stored collections
alias_dict = dict()  # key-value pair is {alias: valid command}
command_history = list()
output_history = list()

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

def alias(command: str, *args):
  """
  Link one or more strings from *args as aliases to a valid command.

  Parameters:
    command: Valid commands encompassed inside the same set of quotes.
    args: List of strings with quotes that are new aliases.

  Return:
    None
  """
  # if command not in emoji_commands and command not in natural_language_commands:
  #   raise ValueError(f'The command \'{command}\' is not yet registered.')

  for arg in set(args):
    alias_dict[arg] = command

def nlp_add_sent(command: str, sentence: str):
  """
  Add new sentence to set of training sentences for the pre-registered command

  Parameters:
    command: Registered and valid command.
    sentence: New training sentence for NLP interpretor.

  Return:
    None
  """
  if command not in emoji_commands and command not in natural_language_commands:
    raise ValueError(f'The command \'{command}\' is not yet registered.')

  natural_language_commands[command].insert(sentence)

magic_commands = dict({
  'alias': lambda parts: alias(parts[1], *parts[2:]),
  'nlp_add_sent': lambda parts: nlp_add_sent(command=parts[1], sentence=parts[2])
})

# keyboard = Controller()

def on_press(key):
  print(key)

def on_release(key):
  pprint(key)

# with Listener(on_press=on_press) as listener:
#   listener.join()

# REPL loop
while(True):

  # collect user input
  user_input = input(emoji.emojize(string=':man_superhero:\t'))
  command_history.append(colored(text=user_input, color='red'))
  cprint(text=user_input, color='red')

  user_input_formatted = user_input
  
  # catch potential magic commands
  if user_input.startswith('%'):
    parts = user_input.split()
    magic_cmd = parts[0][1:]
    pprint(magic_cmd)

    if magic_cmd not in magic_commands:
      raise ValueError(f'The magic command \'{magic_cmd}\' does not exist.')
      continue
  
    magic_func = magic_commands[magic_cmd]
    magic_func(parts)
    continue

  # execute aliases when possible
  if user_input in alias_dict:
    user_input_formatted = alias_dict[user_input]

  # determine whther original user input is already a valid command
  try:
    pipe = Popen(args=user_input_formatted.split(), stdout=PIPE)
    output = pipe.communicate()[0].decode(encoding='UTF-8').split()
    for line in output:
      formatted_line = colored(text=emoji.emojize(string=':man_supervillain:\t' + line), color=random.choice(list(colors)))
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
      formatted_line = colored(text=emoji.emojize(string=':man_supervillain:\t' + line), color=random.choice(list(colors)))
      output_history.append(formatted_line)
      print(formatted_line)
    continue

  except Exception as err:
    # convert natural language into nearest valid command
    predict_cmd = predict_command(sentence=user_input_formatted)
    pipe = Popen(args=predict_cmd.split(), stdout=PIPE)
    output = pipe.communicate()[0].decode(encoding='UTF-8').split()
    for line in output:
      formatted_line = colored(text=emoji.emojize(string=':man_supervillain:\t' + line), color=random.choice(list(colors)))
      output_history.append(formatted_line)
      print(formatted_line)

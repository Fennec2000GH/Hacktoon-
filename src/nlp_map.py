
import textblob as tb
from pprint import pprint

emoji_commands = dict({
  'cat': frozenset(['🐈', '🐱', '🙀', '😾', '😿', '😼', '😺', '😹', '😸', '😽', '😻']),
  'cd': frozenset(['🗄', '🗂']),
  'cp': frozenset(['📋']),
  'free': frozenset(['🆓']),
  'head': frozenset(['🔝', '🆙']),
  'ls': frozenset(['📝', '📜']),
  'mkdir': frozenset(['📁','📂', '🖿']),
  'mv': frozenset(['✂️', '🔪', '🗡️', ]),
  'nano': frozenset(['🖊️', '🖋️', '✒️', '✍️', ]),
  'rm': frozenset(['🧽', '🧹', '🧼', ]),
  'ssh': frozenset(['🐚', '🐌', '🐢', '🦪']),
  'tail': frozenset(['🔽', '⏬', '⬇️'])
})

def translate_emoji(emoji: str):
  """
  Get valid command from emoji.

  Parameters:
    emoji (str): Emoji to interpret.

  Returns:
    str: Valid Linux command from emoji. Invalid emoji will return None.
  """  
  for key, value in emoji_commands.items():
    if emoji in value:
      return key

  raise ValueError(f'The emoji \'{emoji}\' is not valid for any command.')

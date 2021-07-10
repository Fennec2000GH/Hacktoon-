
import textblob as tb
from pprint import pprint

emoji_commands = dict({
  'cat': set(['🐈', '🐱', '🙀', '😾', '😿', '😼', '😺', '😹', '😸', '😽', '😻']),
  'cp': set(['📋']),
  'free': set(['🆓']),
  'head': set(['🔝', '🆙']),
  'ls': set(['📝', '📜']),
  'mkdir': set(['📂']),
  'mv': set(['✂️', '🔪', '🗡️', ]),
  'nano': set(['🖊️', '🖋️', '✒️', '✍️', ]),
  'rm': set(['🧽', '🧹', '🧼', ]),
  'ssh': set(['🐚', '🐌', '🐢', '🦪']),
  'tail': set(['🔽', '⏬', '⬇️'])
})

pprint(emoji_commands)

# Natural Shell 🐚
------------------------------------------------------------------------------------------
![language](https://img.shields.io/badge/language-Python-gold?style=flat-square&logo=appveyor)
![dev environment](https://img.shields.io/badge/dev%20environment-Repl.it-magenta?style=for-the-badge&logo=appveyor)
![tested on](https://img.shields.io/badge/tested%20on-Docker-cyan?style=for-the-badge&logo=appveyor)
![tested on](https://img.shields.io/badge/tested%20on-Linode-darkgreen?style=for-the-badge&logo=appveyor)
------------------------------------------------------------------------------------------
## About ℹ️
This is a simple shell completely written in *Python* 🐍 that bridges the gap between new users and frequent users of **Linux** 🐧 commands. This will be helpful towards new CS students and people who grew up unaccustomed to the digital era. Two major features enable natural language to activate valid Linux commands. First, an emoji translator links a set of icons semantically close in meaning to eahc registered command. Second, an NLP interpretor ranks the set of registered commands based on document similarity scores between user input and training sentences, of courses choosing the command with the highest score. The natural language interpretation was mostly accomplished thanks to the *Spacy* 🌌 libary in Python, although *Jina AI* API 🤖 reached lesser progress earlier when running the shell in a `jinaai/jina` Docker container. Although this was tested in **Docker** 🐋 and **Linode** 🟩 in the terminal, it is guaranteed to work all the time only in **Repl.it** 🍥 shell environment.

## How to Use ❓
1) Clone this repository and `cd` into the root folder.
2) Run `pip3 install -r requirements.txt`.
3) `cd ./src/` and run `python3 shell.py`.

## Demo Video 📺
Click [here](https://youtu.be/uwHU1xP0jBM) to watch a basic demo.

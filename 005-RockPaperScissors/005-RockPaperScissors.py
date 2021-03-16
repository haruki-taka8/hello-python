# 005-RockPaperScissors.py
# Saw this on r/programminghumor and
# I had to reproduce it in Python

import random

while True:
    userInput = input('Rock, paper or scissors: ')

    if userInput.lower() in ['rock', 'paper', 'scissors']:
        break

print(random.choice(['You\'ve won!', 'You\'ve lost!', 'It\'s a tie!']))
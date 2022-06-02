# 005-RockPaperScissors.py
# Saw this on r/programminghumor and
# I had to reproduce it in Python

import random
userInput = ''

while not (userInput.lower() in ['rock', 'paper', 'scissors']):
    userInput = input('Rock, paper or scissors: ')

print(random.choice(['You\'ve won!', 'You\'ve lost!', 'It\'s a tie!']))

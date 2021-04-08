# 006-Hangman.py
# It's been forever since I last worked on this repo

# Variables
from random import randint
import os
wordPath = 'wordlist.txt'
word = []

# Read file
wordPath = os.path.join(os.path.dirname(__file__), wordPath)
lines = 0
with open(wordPath) as file1:
    wordlist = file1.readlines()

# Initialize
toGuess = wordlist[randint(0, len(wordlist)-1)].replace('\n','')
display = '_' * len(toGuess)

# Game loop
while '_' in display:
    # Display prompt
    os.system('cls' if os.name=='nt' else 'clear')
    print(display)
    print()
    try:
        guess = input('Guess: ')[0]
    except:
        guess = ''

    # Evaluate input
    for i in range(len(toGuess)):
        if guess.lower() == toGuess[i].lower():
            display = display[:i] + guess + display[i+1:]

# Game win screen
os.system('cls' if os.name=='nt' else 'clear')
print(toGuess)
print()
print('You\'ve won!')

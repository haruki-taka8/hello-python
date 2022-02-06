# 001-GuessTheNumber.py
# The program generates a random integer from 1 - 100,
# and the user have to guess this random number.

from random import randint
randomNumber = randint(1, 100)
guess = 0

while guess != randomNumber:
    guess = int(input('Please guess the number (1-100 inclusive): '))

    if guess > randomNumber:
        print('Your guess is too big.')
    elif guess < randomNumber:
        print('Your guess is too small.')
    else:
        print('Your guess is correct!')

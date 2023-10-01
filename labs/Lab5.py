'''
This is a simple number guessing game. 
The script will generate a number between 1 and 10.
Then you guess. It will tell if it's too high or too low.
'''

import random

num = random.randint(1,10)
guess = ''

print('I am thinking of a number.')
while guess != num:

    guess = int(input('Guess: '))

    if guess == num:
        print('You guessed it! The number was ' + str(num))
    elif guess < num:
        print('Too low. Try again!')
    elif guess > num:
        print('Too high. Try again!')

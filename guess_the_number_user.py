import random

number = random.randint(1, 100)
score = 100

while True:
    users_guess = int(input('Guess a number between 1 and 100 '))

    if users_guess < number:
        print('Bigger!')
        score -= 1
        continue
    elif users_guess > number:
        print('Smaller!')
        score -= 1
        continue
    elif users_guess == number:
        print()
        print('You guest the right number!')
        print('Your score was', score)
        break




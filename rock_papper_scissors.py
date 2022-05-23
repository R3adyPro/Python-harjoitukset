
import random
    
utilities = ['Rock', 'Papper', 'Scissors']


while True:
    enemys_choice = random.choice(utilities)
    player_choice = input('Pick between rock, papper and scissors! ')
    player_choice = player_choice.lower().capitalize()

    if player_choice == utilities[0]:
        if enemys_choice == 'Papper':
            print('You lost!')
        elif enemys_choice == 'Scissors':
            print('You won!')
        elif enemys_choice == 'Rock':
            print('Draw!')
            continue

    if player_choice == utilities[1]:
        if enemys_choice == 'Papper':
            print('Draw!')
        elif enemys_choice == 'Scissors':
            print('You lost!')
        elif enemys_choice == 'Rock':
            print('You won!')
            continue

    if player_choice == utilities[2]:
        if enemys_choice == 'Papper':
            print('You won!')
        elif enemys_choice == 'Scissors':
            print('Draw!')
        elif enemys_choice == 'Rock':
            print('You lost!')
            continue
        
    again = input("Do you want to play again? ")
    if again.lower() == 'yes':
        continue
    else:
        break
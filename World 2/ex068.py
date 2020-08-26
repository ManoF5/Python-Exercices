from random import randint
# COLORS
RESET = '\033[m'
RED   = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
# INTRO
print(f'{GREEN}Even or Odd{RESET}')
print(f'{GREEN}   Game    {RESET}')
# INPUT / OUTPUT
winning_streak = 0
while True:
    player_num = int(input('Type a number: '))
    while True:
        player_choice = str(input('Even or Odd? ')).upper().strip()
        machine_num = randint(0, 10)
        # SITUATION 1
        if player_choice == 'EVEN':
            total = player_num + machine_num
            if total % 2 == 0:
                print('=' * 18)
                print(f'Player number: {player_num}')
                print(f'Machine number: {machine_num}')
                print(f'Total: {total}')
                print(f'\n{GREEN}Player Wins{RESET}')
                print('=' * 18)
                winning_streak += 1
                play_again = True
            else:
                print('=' * 18)
                print(f'Player number: {player_num}')
                print(f'Machine number: {machine_num}')
                print(f'Total: {total}')
                print(f'\n{RED}Machine Wins{RESET}')
                print('=' * 18)
                play_again = False
            break
        # SITUATION 2
        elif player_choice == 'ODD':
            total = player_num + machine_num
            if total % 2 == 0:
                print('=' * 18)
                print(f'Player number: {player_num}')
                print(f'Machine number: {machine_num}')
                print(f'Total: {total}')
                print(f'\n{RED}Machine Wins{RESET}')
                print('=' * 18)
                play_again = False
            else:
                print('=' * 18)
                print(f'Player number: {player_num}')
                print(f'Machine number: {machine_num}')
                print(f'Total: {total}')
                print(f'\n{GREEN}Player Wins{RESET}') 
                print('=' * 18)
                winning_streak += 1
                play_again = True
            break
        # SITUATION 3
        else:
            print(f'{RED}Wrong choice{RESET},try again...')
    if play_again == True:
        print('Lets play again...\n')
    elif play_again == False:
        break   
print(f'{YELLOW}Winning streak{RESET}: {winning_streak} \n')    

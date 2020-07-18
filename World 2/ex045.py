from random import choice
opt = ['ROCK','PAPER','SCISSOR']
machine_opt = choice(opt)
# COLORS
colors = {
    'CLEAN':'\033[m',
    'GREEN':'\033[32m',
    'RED':'\033[31m'
}
# INTRO
print(' {}      JOKENPO {}'.format(colors['GREEN'], colors['CLEAN']))
print('   Rock-Paper-Scissor \n')
# INPUT
player_opt = str(input('Player  -> ')).strip().upper()
print('Machine -> {}'.format(machine_opt))
# OUTPUT
if player_opt == 'ROCK' and machine_opt == 'SCISSOR':                        # ROCK  <- SCISSOR
    print('\n{} Player Wins! {}\n'.format(colors['GREEN'], colors['CLEAN']))
elif player_opt == 'ROCK' and machine_opt == 'PAPER':                        # ROCK -> PAPER
    print('\n{} Machine Wins! {}\n'.format(colors['RED'], colors['CLEAN']))
elif player_opt == 'ROCK' and machine_opt == 'ROCK':                         # ROCK - ROCK
    print('\n Draw! \n')                 
elif player_opt == 'PAPER' and machine_opt == 'ROCK':                        # PAPER <- ROCK
    print('\n{} Player Wins! {}\n'.format(colors['GREEN'], colors['CLEAN']))
elif player_opt == 'PAPER' and machine_opt == 'SCISSOR':                     # PAPER -> SCISSOR         
    print('\n{} Machine Wins! {}\n'.format(colors['RED'], colors['CLEAN'])) 
elif player_opt == 'PAPER' and machine_opt == 'PAPER':                       # PAPER - PAPER         
    print('\n Draw! \n')     
elif player_opt == 'SCISSOR' and machine_opt == 'PAPER':                     # SCISSOR <- PAPER
    print('\n{} Player Wins! {}\n'.format(colors['GREEN'], colors['CLEAN']))
elif player_opt == 'SCISSOR' and machine_opt == 'ROCK':                      # SCISSOR -> ROCK
    print('\n{} Machine Wins! {}\n'.format(colors['RED'], colors['CLEAN'])) 
elif player_opt == 'SCISSOR' and machine_opt == 'SCISSOR':                   # SCISSOR - SCISSOR
    print('\n Draw! \n') 
else:
    print('\n INVALID INPUT \n')
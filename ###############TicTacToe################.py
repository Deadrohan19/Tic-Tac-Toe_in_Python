###############TicTacToe####################################
#Boolean
game_on = True

#variables
x = 0
y = 0

#############FUNCTIONS#######################################
#Display
def display_board():
    print(f' {indexes["7"]:1} | {indexes["8"]:1} | {indexes["9"]:1} ')
    print('-----------')
    print(f' {indexes["4"]:1} | {indexes["5"]:1} | {indexes["6"]:1} ')
    print('-----------')
    print(f' {indexes["1"]:1} | {indexes["2"]:1} | {indexes["3"]:1} ')
    
#XO
def XO_choice():
    choice = 'wrong'
    
    while choice not in ['X','O']:
        
        choice = input('Do you want to be X or O? \n')
        
        if choice not in ['X','O']:
            print('Choice is not valid! Please choose X or O.')
    if choice == 'X':
        print('Player 1 will go first.')
    else:
        print('Player 2 will go first.')
    return choice

#Confirmation
def confirmation():
    choice = 'wrong'
    global game
    
    while choice not in ['Yes', 'No']:
        choice = input('Are you ready to play? Enter Yes or No.\n')
        if choice not in ['Yes', 'No']:
            print('Enter valid choice!')
    if choice == 'No':
        game = False
        
#Position
def position_choice():
    choice = 'wrong'
    while choice not in position_index:
        choice = input('Choose your next position: (1-9)\n')
        
        if choice not in position_index:
            print('Please enter a valid position')
            
    position_index.remove(choice)        
    return choice

#Replace
def replacement_func(position):
    global choice
    indexes[position] = choice
    if choice == 'X':
        choice = 'O'
    else:
        choice = 'X'
        
#Won_check
def won_check():
    global game
    global x
    global y
    if indexes['1'] == indexes['2'] == indexes['3'] == 'X' or indexes['4'] == indexes['5'] == indexes['6'] == 'X' or indexes['7'] == indexes['8'] == indexes['9'] == 'X' or indexes['1'] == indexes['5'] == indexes['9'] == 'X' or indexes['7'] == indexes['5'] == indexes['3'] == 'X' or indexes['1'] == indexes['4'] == indexes['7'] == 'X' or indexes['2'] == indexes['5'] == indexes['8'] == 'X' or indexes['3'] == indexes['6'] == indexes['9'] == 'X':
        print('Player 1 has won')
        x += 1
        game = False
    elif indexes['1'] == indexes['2'] == indexes['3'] == 'O' or indexes['4'] == indexes['5'] == indexes['6'] == 'O' or indexes['7'] == indexes['8'] == indexes['9'] == 'O' or indexes['1'] == indexes['5'] == indexes['9'] == 'O' or indexes['7'] == indexes['5'] == indexes['3'] == 'O' or indexes['1'] == indexes['4'] == indexes['7'] == 'O' or indexes['2'] == indexes['5'] == indexes['8'] == 'O' or indexes['3'] == indexes['6'] == indexes['9'] == 'O':
        print('Player 2 has won')
        y += 1
        game = False
        
#play_again
def play_again():
    choice = 'wrong'
    global game_on
    
    while choice not in ['Yes', 'No']:
        choice = input('Do you want to play again? Enter Yes or No\n')
        
        if choice not in [ 'Yes', 'No']:
            print('Enter valid choice')
    if choice == 'No':
        game_on = False


#############LOGIC###########################################
print('Welcome to Tic-Tac-Toe!')

while game_on:
    game = True
    
    #array & dictionary
    position_index = ['1','2','3','4','5','6','7','8','9']
    indexes = {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':'', '9':''}
    
    #initial inputs
    choice = XO_choice()
    print('\n'*100)

    confirmation()
    print('\n'*100)

    while game:
        if len(position_index) == 0:
            print('Draw!')
            break
        #Displaying the board
        display_board()

        #position choosing
        position = position_choice()

        #Clearing output
        print('\n'*100)

        #replacing on that chosen position
        replacement_func(position)

        #Again displaying the board
        display_board

        #checking if someone won
        won_check()
    
    #Asking if u want to play again
    play_again()

    print('\n'*100)
#########STATISTICS#####################################

print(f'Player 1 has won {x} times')
print(f'Player 2 has won {y} times\n\n')

#Ending message
print('Thanks for playing')
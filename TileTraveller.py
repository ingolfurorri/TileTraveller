import random
list_of_coins = [(1,2), (2,2), (3,2), (2,3)]
SEED = int(input("Input seed: "))
random.seed(SEED)


def coin_check():
    print("Pull a lever (y/n):", end= ' ')
    user_input = random.choice(['y', 'n'])
    print(user_input)

    if user_input == 'y':
        return True
    else:
        return False



def move_al(move_user, move_allowed):
    '''Checks if the move is legal'''
    move_user = move_user.lower()
    for i in move_allowed:
        if move_user == i:
            return True

    return False



def movement_available(x, y):
    '''Checks the current position, and returns what moves are available'''
    movement = ''
    move_yes = ''
    if not (y == 3 or x == 2 and y == 2):

        if(movement == ''):
            movement += '(N)orth'
            move_yes += 'n'

    if (x < y):
        if(movement == ''):
            movement += '(E)ast'
            move_yes += 'e'

        else:
            movement += ' or (E)ast'
            move_yes += 'e'

    if not (y == 1 or x == 2 and y == 3):
        if(movement == ''):
            movement += '(S)outh'
            move_yes += 's'

        else:
            movement += ' or (S)outh'
            move_yes += 's'
            
    if (x == 2 and y == 3 or x == y and x != 1):
        if(movement == ''):
            movement += '(W)est'
            move_yes += 'w'

        else:
            movement += ' or (W)est'
            move_yes += 'w'

    return movement, move_yes



def move(x, y, move_user):
    '''Updates the position of the user according to input'''
    movement = move_user.lower()
    if(movement == 'n'):
        y += 1
    elif(movement == 's'):
        y -= 1
    elif(movement == 'e'):
        x += 1
    elif(movement == 'w'):
        x -= 1

    return x, y


def play():
    moves_computer = 0
    pos_current_x = 1
    pos_current_y = 1
    coins = 0

    while not (pos_current_x == 3 and pos_current_y == 1):

    #Checks what moves are allowed

        move_avail , move_allowed = movement_available(pos_current_x, pos_current_y)
        move_avail += '.'
        print("You can travel:", move_avail)
        print("Direction:", end=' ')
        move_user = random.choice(['n', 'e', 's', 'w'])
        print(move_user)

    #Checks if the move is allowed, if not prompts for a different direction
    
        move_bool = move_al(move_user, move_allowed)

        while not(move_bool):
            print("Not a valid direction!")
            print("You can travel:", move_avail)
            print("Direction:", end=' ')
            move_user = random.choice(['n', 'e', 's', 'w'])
            move_bool = move_al(move_user, move_allowed)
            print(move_user)
            moves_computer += 1

    #Updates the position

        pos_current_x, pos_current_y = move(pos_current_x, pos_current_y, move_user)
        user_pos_tuple = (pos_current_x, pos_current_y)

        if user_pos_tuple in list_of_coins:
            if(coin_check()):
                coins+=1
                print("You received 1 coin, your total is now {}.".format(coins))
        
        moves_computer += 1


    else:
        print("Victory! Total coins {}. Moves {}.".format(coins, moves_computer))



def main():
    play_no = 1
    play()
    user_input = input("Play again (y/n): ")

    while user_input == 'y':
        play()
        user_input = input("Play again (y/n): ")

main()
pos_x = 1
pos_y = 1



def get_coin():
    user_input = input("Pull a lever (y/n): ").lower()
    if user_input == 'y':
        return 1
    else:
        return 0



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



#Main program

pos_current_x = pos_x
pos_current_y = pos_y
coins = 0

while not (pos_current_x == 3 and pos_current_y == 1):

    #Checks what moves are allowed

    move_avail , move_allowed = movement_available(pos_current_x, pos_current_y)
    move_avail += '.'
    print("You can travel:", move_avail)
    move_user = input("Direction: ")

    #Checks if the move is allowed, if not prompts for a different direction
    
    move_bool = move_al(move_user, move_allowed)

    while not(move_bool):
        print("Not a valid direction!")
        move_user = input("Direction: ")
        move_bool = move_al(move_user, move_allowed)

    #Updates the position

    pos_current_x, pos_current_y = move(pos_current_x, pos_current_y, move_user)

    coins += coin_check(list_of_coins, pos_current_x, pos_current_y)

else:
    print("Victory! Total coins {}".format(coins))
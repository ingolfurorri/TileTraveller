pos_x = 1
pos_y = 1

def movement_available(x, y):
    movement = ''
    if not (y == 3 or x == 2 and y == 2):
        movement += '(N)orth'
    if (y == 3 or y != x and y != 1 and x != 2):
        movement += '(E)ast'
    if not (y == 1 or x == 2 and y == 3):
        movement += '(S)outh'
    if (x == 2 and y == 3 or x == y and x != 1):
        movement += '(W)est'

    return movement

def move(x, y, move_user):
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

pos_current_x = pos_x
pos_current_y = pos_y

while not (pos_current_x == 3 and pos_current_y == 1):
    print(movement_available(pos_current_x, pos_current_y))
    move_user = input('Input where to go: ')
    
    pos_current_x, pos_current_y = move(pos_current_x, pos_current_y, move_user) 
    print(pos_current_x, pos_current_y)
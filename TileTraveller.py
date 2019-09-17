pos_x = 1
pos_y = 1

def movement_available(x, y):
    movement = ''
    if not (y == 3 or x == 2 and y == 2):
        movement += '(N)orth'
    if (y == 3 and y != x):
        movement += '(E)ast'
    if not (y == 1 or x == 2 and y == 3):
        movement += '(S)outh'
    if (x == 2 and y == 3 or x == y and x != 1 or x == 1 and y == 2):
        movement += '(W)est'
    return movement

def move(pos_current_x, pos_current_y, movement):
    

pos_current_x = pos_x
pos_current_y = pos_y

while not (pos_current_x == 3 and pos_current_y == 1):
    print(movement_available(pos_current_x, pos_current_y))
    move_user = input('Input where to go: ')

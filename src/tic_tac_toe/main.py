board = '''                          |            |
                          |            |
                          |            |
                          |            |
                          |            |
                   7      |      8     |       9
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                          |            |
                          |            |
                   4      |      5     |       6
             _____________|____________|_______________
                          |            |
                          |            |
                          |            |
                          |            |
                          |            |
                   1      |      2     |        3

'''
moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


print(board)


def movement(icon):
    move = input("Where do you want to move?\n")
    if str(move) in moves:
        
        global board
        board = board.replace(str(move), icon)
        print(board)
        if icon == 'X':
            movement('O')
        else:
            movement('X')
    else:
        print('You can\'t make this move...')
        movement(icon)
movement('O')
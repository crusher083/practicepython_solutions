def print_board(height, width):
    for n in range(height):
        print(' ' + '--- '*width)
        print('|' + '   |'* width)
    print(' ' + '--- ' * width)


print_board(20, 20)

# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
def enter_names():
    player1 = input(f'Player1, please enter your name: ')
    player2 = input(f'Player2, please enter your name: ')
    return player1, player2


def make_a_move(player):
    while True:
        p_move = input(f'\n{player}, please choose:\
                                    \n1. Rock\
                                    \n2. Spock\
                                    \n3. Paper\
                                    \n4. Lizard\
                                    \n5. Scissors\n')
        if p_move.isdigit() and 0 < int(p_move) < 6:
            break
        else:
            print("Please enter number from 1 to 5")
    return int(p_move) - 1


def rpsls_game(p1_move, p2_move):
    playing = True
    while playing:
        if (p1_move - p2_move) % 5 < 3:
            win = (p1_move**2 + 10) // (p2_move - 0.5)
            print(f'{values[p1_move]} {win_options[win]} {values[p2_move]}!\
                  \n{player1} wins!')
            playing = False
        elif p1_move == p2_move:
            print('It is a tie!')
        else:
            win = ((p2_move**2 + 10) // (p1_move - 0.5))
            print(f'{values[p2_move]} {win_options[win]} {values[p1_move]}\
                  \n{player2} wins!')
            playing = False


def game():
    p1_move = make_a_move(player1)
    p2_move = make_a_move(player2)
    rpsls_game(p1_move, p2_move)


def replay():
    choice = input('Wanna play again? Y or N')
    while True:
        if choice[0].lower() == 'y':
            game()
            break
        elif choice[0].lower() == 'n':
            quit()
        else:
            print('Please enter Y or N')


values = {0: 'Rock', 1: 'Spock', 2: 'Paper', 3: 'Lizard', 4: 'Scissors'}
win_options = {-28.0: 'wraps', -22.0: 'evaporates', 2.0: 'crushes',
               3.0: 'smashes', 4.0: 'crush', 10.0: 'decapitate', 12.0: 'eats',
               17.0: 'cuts', 28.0: 'disproves', 38.0: 'poisons'}


if __name__ == '__main__':
    player1, player2 = enter_names()
    game()
    replay()

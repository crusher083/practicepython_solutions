winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


def rows_159(board):
    yield from board
    yield [board[i][i] for i in range(len(board))]


def all_lines(board):
    yield from rows_159(board)
    yield from rows_159(list(zip(*reversed(board))))


def win(board):
    for line in all_lines(board):
        if len(set(line)) == 1 and line[0] != 0:
            print(line[0])
            return line[0]
    return None




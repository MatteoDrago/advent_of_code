import numpy as np

def bingo(boards, numbers, last=False):
    num_boards = len(boards) // 5 
    board_bingo = []
    for el in numbers:
        num = 0
        while (num < len(boards)):
            bn = num // 5 # index of the current board
            for i in range(num, num+5):
                if bn in board_bingo:
                    break
                if el in boards[i]:
                    j, = np.where(boards[i] == el)
                    boards[i,j[0]] = np.nan
                    if np.isnan(boards[i]).all() or np.isnan(boards[bn*5:bn*5+5,j[0]]).all(): # check if this board won
                        if not last:
                            return bn, el, boards # find first board to win
                        board_bingo.append(bn)
                        if len(board_bingo) == num_boards:
                            return bn, el, boards # find last board to win 
            num += 5

def print_board(boards, board_num):
    for i in range(board_num*5, board_num*5+5):
        print(boards[i])

def score(final, board_num, boards):
    count = 0
    for i in range(board_num*5, board_num*5+5):
        for el in boards[i]:
            if not np.isnan(el):
                count += el
    return final*count

numbers = np.loadtxt('input_04.txt', dtype=float, delimiter=',', max_rows=1)
boards = np.loadtxt('input_04.txt', dtype=float, skiprows=1)

board_num, final, boards = bingo(boards, numbers)
print("Answer first part: ", score(final, board_num, boards))

board_num, final, boards = bingo(boards, numbers, True)
print("Answer second part: ", score(final, board_num, boards))
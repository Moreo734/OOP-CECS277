import check_input
import random
def create_board(rows, cols):

    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        board.append(row)
    return board
def place_mines(board, mines):
    """random places mines which are indicated as X on the board without overwriting existing mines, creates 2D list representing the board, # of mines to place"""
    rows = len(board)
    cols = len(board[0])
    placed = 0

    while placed < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        if board[r][c] == 0:
            board[r][c] = 'X'
            placed += 1


def display_board(board):
    """Displays board to console"""
    for row in board:
        for value in row:
            print(value, end=" ")
        print()


def count_mines(board):
    """Counts # of adjacent mines for each non mine cell, then updates the board"""
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] != 'X':
                count = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if board[nr][nc] == 'X':
                                count += 1
                board[r][c] = count


def main():
    print("Minesweeper Maker")
    row = int(input("Enter row number: "))
    col = int(input("Enter column number: "))
    mine = int(input("Enter number of mines: "))
    board = create_board(row, col)
    place_mines(board,mine)
    count_mines(board)
    display_board(board)



main()
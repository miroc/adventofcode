#!/usr/bin/env python

from itertools import product

# board include border lights, which are always off 0. and 102. row/column


def empty_board():
    return [['.' for j in range(102)] for i in range(102)]


def evaluate(board, row, col, corners_on=False):
    # count on neighbours
    if corners_on:
        if (row, col) in [(1,1), (1,100), (100,1),(100, 100)]:
            return "#"

    on_count = 0
    for dx,dy in list(product(range(-1,2), repeat=2)):
        if dx == dy == 0:
            continue
        if board[row + dx][col + dy] == '#':
            on_count += 1
    if board[row][col] == '#':
        if on_count in [2,3]:
            return '#'
    else:
        if on_count == 3:
            return '#'
    # all other cases, go off
    return '.'


def next_board(board, corners_on=False):
    future_board = empty_board()
    for row in range(1,101):
        for col in range(1,101):
            future_board[row][col] = evaluate(board, row, col, corners_on)
    return future_board


def count_on(board):
    on_count = 0
    for row in board:
        for c in row:
            if c == '#':
                on_count += 1
    return on_count


def main():
    board0 = empty_board()
    with open("day_18_input") as f:
        for row, line in enumerate(f.readlines()):
            for col,c in enumerate(line.strip()):
                board0[row+1][col+1] = c


    board = board0
    for i in range(100):
        board = next_board(board, True)
    print(count_on(board))


if __name__ == '__main__':
    main()

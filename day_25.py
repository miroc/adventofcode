#!/usr/bin/env python


def next_code(code):
    return (code * 252533) % 33554393


def get_code_count(row, column):
    return sum(range(row + column - 1)) + column


def main():
    first_code = 20151125
    code_coords = (2981, 3075)

    cur_code = first_code
    for i in range(get_code_count(*code_coords)):
        cur_code = next_code(cur_code)
    print("Code", cur_code)


if __name__ == '__main__':
    main()


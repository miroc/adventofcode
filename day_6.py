#!/usr/bin/env python

op_types = ['turn on', 'turn off', 'toggle']

class Operation:
    def __init__(self, op_type, frm, to):
        """
        :param op_type: type of operation, see op_types
        :param frm: tuple (x1, y1)
        :param to: tuple (x2, y2
        :return:
        """
        self.op_type = op_type
        self.x1 = frm[0]
        self.x2 = to[0]
        self.y1 = frm[1]
        self.y2 = to[1]


class Board:
    task1_mutations = {
        "turn on": lambda cell: 1,
        "turn off": lambda cell: 0,
        "toggle": lambda cell: 0 if cell == 1 else 1
    }
    task2_mutations = {
        "turn on": lambda cell: cell + 1,
        "turn off": lambda cell: max(cell - 1, 0),  # decrement by 1 until 0 is reached
        "toggle": lambda cell: cell + 2
    }

    def __init__(self):
        self.matrix = [[0 for x in range(1000)] for x in range(1000)]

    def task1_apply(self, op):
        self.__apply(op, self.task1_mutations)

    def task2_apply(self, op):
        self.__apply(op, self.task2_mutations)

    def reset_board(self):
        for x in range(1000):
            for y in range(1000):
                self.matrix[x][y] = 0

    def __apply(self, op, mutations):
        mutation_func = mutations[op.op_type]
        for x in range(op.x1, op.x2 + 1):
            for y in range(op.y1, op.y2 + 1):
                self.matrix[x][y] = mutation_func(self.matrix[x][y])

    def count_lights_sum(self):
        total = 0
        for row in self.matrix:
            for cell in row:
                total += cell
        return total

    def print_beginning(self, rows, cols):
        for row in range(rows):
            print(self.matrix[row][:cols])


def process_op_rest(op_type, rest):
    """
    Here parse coordinates from line string
    :param op_type:
    :param rest:
    :return:
    """
    delimiter = "through"

    delimiter_start = rest.find(delimiter)
    if delimiter_start != -1:
        frm = [int(c) for c in rest[:delimiter_start].strip().split(',')]
        to = [int(c) for c in rest[delimiter_start + len(delimiter):].strip().split(',')]
        operations.append(Operation(op_type, tuple(frm), tuple(to)))


operations = []


def process_lines(lines):
    for line in lines:
        for op_type in op_types:
            # Parse line into operation type + coordinates
            if line.startswith(op_type):
                rest = line[len(op_type):]
                process_op_rest(op_type, rest)
    print("number of operations: %d" % len(operations))

    # operations = [Operation("turn on", (0, 0), (2, 2)), Operation("toggle", (0, 0), (2, 2))]

    board = Board()
    for op in operations:
        board.task1_apply(op)
    print("Task1: number of lights on: %d" % board.count_lights_sum())
    board.reset_board()

    for op in operations:
        board.task2_apply(op)

    print("Task2: sum of lights: %d" % board.count_lights_sum())


def main():
    with open("day_6_input") as f:
        lines = f.readlines()
        process_lines(lines)


if __name__ == '__main__':
    main()

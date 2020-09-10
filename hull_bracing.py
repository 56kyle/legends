import pyautogui
from repair_mini_game import *
import time
import math
import random

Move = collections.namedtuple("Move", "p1 p2")


class HullBracing(RepairMiniGame):
    def __init__(self):
        super().__init__()
        self.button = Point(x=956, y=916)
        self.name = "hull_bracing"
        self.block_region = points_to_region(Point(x=810, y=380), Point(x=1116, y=686))
        base = "./images/markers/hull_bracing/"
        self.blockade = base + "blockade.png"
        self.green_line = base + "green_line.png"
        self.red_line = base + "red_line.png"
        self.red_and_green_line = base + "red_and_green_line.png"
        self.blue_line = base + "blue_line.png"
        self.blocks = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]
        ]

    @property
    def playfield(self):
        snap = pyscreeze.screenshot(region=self.block_region)
        location = "./images/markers/hull_bracing/playfield.png"
        snap.save(location)
        return location

    def play(self):
        starting_board = self.playfield
        if pyscreeze.locate(self.green_line, starting_board, confidence=.9):
            self.play_medium()
        elif pyscreeze.locate(self.blue_line, starting_board, confidence=.9):
            self.play_hard()
        elif pyscreeze.locate(self.red_line, starting_board, confidence=.9):
            self.play_easy()
        else:
            self.play()

    def play_easy(self):
        print("Easy")
        field = self.playfield

        self.assign_placements(self.blockade, 0, field)
        self.assign_placements(self.red_line, 1, field)
        print(self.blocks)

    def play_medium(self):
        print("Medium")
        field = self.playfield
        #field = "./images/markers/hull_bracing/playfield.png"
        complete = False

        self.assign_placements(self.blockade, 0, field)
        self.assign_placements(self.red_line, 1, field)
        self.assign_placements(self.green_line, 2, field)
        self.assign_placements(self.red_and_green_line, 4, field)
        possibilities = [Board(self.blocks)]
        final_board = None

        while not final_board:
            new_round = []
            for a_board in possibilities:
                board = a_board.board
                for y in range(4):
                    for x in range(4):
                        new_possibilities = []
                        if board[y][x] is False:
                            if x > 0:
                                new_board = board
                                move = [[y, x-1], [y, x]]
                                new_board[y][x-1] = False
                                new_board[y][x] = board[y][x-1]
                                new_possibilities.append([new_board, move])
                            if x < 3:
                                new_board = board
                                move = [[y, x+1], [y, x]]
                                new_board[y][x+1] = False
                                new_board[y][x] = board[y][x+1]
                                new_possibilities.append([new_board, move])
                            if y > 0:
                                new_board = board
                                move = [[y-1, x], [y, x]]
                                new_board[y-1][x] = False
                                new_board[y][x] = board[y-1][x]
                                new_possibilities.append([new_board, move])
                            if y < 3:
                                new_board = board
                                move = [[y+1, x], [y, x]]
                                new_board[y+1][x] = False
                                new_board[y][x] = board[y+1][x]
                                new_possibilities.append([new_board, move])
                        for possible in new_possibilities:
                            possible_board = Board(possible[0], a_board, possible[1])
                            new_round.append(possible_board)
            possibilities = new_round
            for plausible_board in possibilities:
                accept = True
                for y in range(4):
                    for x in range(4):
                        if (plausible_board.board[y][x] == 1) or (plausible_board.board[y][x] == 4):
                            for val in plausible_board.board[y]:
                                if not (val == 1 or val == 4):
                                    accept = False
                        if (plausible_board.board[y][x] == 2) or (plausible_board.board[y][x] == 4):
                            for row in plausible_board.board:
                                if not (row[x] == 2) or (row[x] == 4):
                                    accept = False
                if accept:
                    final_board = plausible_board

        all_steps = final_board.retrace_steps()
        for step in all_steps:
            dx = step[0][0] - step[1][0]
            dy = step[0][0] - step[1][0]
            dh = math.sqrt((dx**2) + (dy**2))
            duration = dh * .01

            pyautogui.moveTo(step[0][0], step[0][1])
            pyautogui.mouseDown(step[0][0], step[0][1], duration=duration)
            pyautogui.moveTo(step[1][0], step[1][1], duration=duration)
            pyautogui.mouseUp(step[1][0], step[1][1])

    def play_hard(self):
        print("Hard")
        field = self.playfield

        self.assign_placements(self.blockade, 0, field)
        self.assign_placements(self.red_line, 1, field)
        self.assign_placements(self.blue_line, 3, field)

        print(self.blocks)

    def assign_placements(self, line_type, value_to_assign, field=None):
        placements = self.locate_block_placements(line_type, field=field)
        for placement in placements:
            self.blocks[placement[0]][placement[1]] = value_to_assign

    def locate_block_placements(self, block, field=None):
        positions = []
        if field is None:
            field = self.playfield
        block_places = list(pyscreeze.locateAll(block, field, confidence=.96))
        for place in block_places:
            positions.append(self.find_placement(place))
        return positions

    def block_center(self, region):
        return Point(region[0]+int(region[2]/2), region[1]+int(region[3]/2))

    def find_placement(self, block):
        quarter_width = int(self.block_region[2] / 4)
        quarter_height = int(self.block_region[3] / 4)
        center = self.block_center(block)
        x = self.get_place([center.x, quarter_width])
        y = self.get_place([center.y, quarter_height])

        return [y, x]

    def get_place(self, pair):
        val = pair[0]
        quarter = pair[1]
        if 0 < pair[0] < quarter:
            return 0
        if quarter < val < (2 * quarter):
            return 1
        if (2 * quarter) < val < (3 * quarter):
            return 2
        if (3 * quarter) < val < (4 * quarter):
            return 3


class Board:
    def __init__(self, board, ancestor=None, move=None):
        self.ancestor = ancestor
        self.board = board
        self.move = move

    def in_history(self, searching_for):
        if self.board == searching_for:
            return True
        elif self.ancestor:
            return self.ancestor.in_history(searching_for)
        else:
            return False

    def count_steps(self, steps=0):
        steps += 1
        if self.ancestor:
            return self.ancestor.count_steps(steps)
        else:
            return steps

    def retrace_steps(self):
        if self.ancestor:
            current_progress = self.ancestor.retrace_steps()
            current_progress.append(self.move)
            return current_progress
        else:
            return [self.move]


if __name__ == "__main__":
    test = HullBracing()
    test.play()

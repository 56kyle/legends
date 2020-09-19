from brew.piece import *
import collections
from window_input import Window, Key
import mouse
import keyboard
import time

Point = collections.namedtuple("Point", "x y")
Color = collections.namedtuple("Color", "r g b")


class Board:
    up_next_checks = [
        Point(x=726, y=144),
        Point(x=796, y=115)
    ]

    column_checks = [
        Point(x=1002, y=72),
        Point(x=1082, y=114),
        Point(x=1154, y=74),
        Point(x=1224, y=114),
        Point(x=1294, y=72),
        Point(x=1366, y=114),
        Point(x=1436, y=72),
        Point(x=1504, y=114)
    ]

    background_results = [
        Color(r=43, g=21, b=3),
        Color(r=45, g=24, b=5),
        Color(r=59, g=36, b=17),
        Color(r=47, g=25, b=13),
        Color(r=38, g=17, b=0),
        Color(r=48, g=25, b=15),
        Color(r=38, g=19, b=5),
        Color(r=53, g=32, b=20)
    ]

    placements = [
        Point(x=1042, y=304),
        Point(x=1128, y=304),
        Point(x=1186, y=306),
        Point(x=1264, y=312),
        Point(x=1330, y=314),
        Point(x=1398, y=320),
        Point(x=1474, y=340)
    ]

    def __init__(self, win=Window(), pattern=(RED, RED, GREEN, GREEN, BLUE, BLUE, RED, None)):
        self.win = win
        self.pattern = pattern
        self.history = []
        self.start = None
        self.rep = 0
        self.times = []

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(*self.columns)

    @property
    def pair(self):
        pair = []
        columns = self.columns
        if columns:
            for val in columns:
                if val:
                    pair.append(val)
            return pair
        else:
            return False

    @property
    def complete(self):
        if not keyboard.is_pressed("`"):
            return self.win.pixel(1222, 683) == Color(255, 255, 255)
        else:
            time.sleep(999)

    @property
    def columns(self):
        while not self.complete:
            columns = [None, None, None, None, None, None, None, None]
            for i, point in enumerate(self.column_checks):
                px = self.win.pixel(point)
                if px != self.background_results[i]:
                    for color in COLOR_CLASSES:
                        if color.column_results[i] == px:
                            columns[i] = color().color
            else:
                passing = 0
                for val in columns:
                    if val:
                        passing += 1
                if passing == 2:
                    return columns
        else:
            return False

    def place(self, column_nums):
        self.maintain_spot_until_full(column_nums)
        mouse.click()
        time.sleep(.2)
        self.maintain_spot_until_full(column_nums)

    def maintain_spot_until_full(self, column_nums):
        columns = self.columns
        while columns and not(columns[column_nums[0]] and columns[column_nums[1]]):
            mouse.move(*self.placements[column_nums[0]])
            columns = self.columns

    def swap(self):
        keyboard.press("space")
        time.sleep(.1)
        keyboard.release("space")

    def solve(self):
        self.start = time.time()
        while not self.complete:
            placed = False
            pair = self.pair
            if pair:
                for i in range(7):
                    if self.pattern[i] == pair[0] and self.pattern[i+1] == pair[1]:
                        self.place((i, i+1))
                        placed = True
                if not placed:
                    self.swap()
        else:
            self.times.append(time.time()-self.start)
            self.rep += 580
            print("--------------------------------------------------")
            print("Round {} - {}".format(len(self.times), self.times[-1]))
            print("Running Average - {}".format(sum(self.times)/len(self.times)))
            print("Total Rep Gained - {}".format(self.rep))
            mouse.move(1236, 687)
            mouse.click()
            time.sleep(.1)
            mouse.release()
            time.sleep(.5)


def select_swift_three(win):
    for _ in range(2):
        mouse.move(1452, 834)
        mouse.click()
        time.sleep(.1)
        mouse.release()
        time.sleep(.1)
    time.sleep(.1)
    mouse.move(*Point(x=1157, y=840))
    mouse.click()
    time.sleep(.1)
    mouse.release()
    if win.pixel(1156, 493) == (255, 255, 255):
        time.sleep(.5)
        mouse.move(1208, 574)
        mouse.click()
        time.sleep(.1)
        mouse.release()


def select_cannon_three(win):
    for _ in range(2):
        mouse.move(1452, 834)
        mouse.click()
        time.sleep(.1)
        mouse.release()
        time.sleep(.1)
    time.sleep(.1)
    mouse.move(1159, 768)
    mouse.click()
    time.sleep(.1)
    mouse.release()
    if win.pixel(1156, 493) == (255, 255, 255):
        time.sleep(.5)
        mouse.move(1208, 574)
        mouse.click()
        time.sleep(.1)
        mouse.release()


def select_marksman_three(win):
    time.sleep(.2)
    mouse.move(*Point(x=1157, y=840))
    mouse.click()
    if win.pixel(1156, 493) == (255, 255, 255):
        time.sleep(.5)
        mouse.move(1208, 574)
        mouse.click()


if __name__ == "__main__":
    time.sleep(2)
    board = Board(Window())
    while True:
        select_swift_three(board.win)
        board.solve()

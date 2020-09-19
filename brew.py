import collections
import pyautogui
import mouse, keyboard
import pyscreeze
import win32api
import win32gui
import win32con
from window_input import Window, Key
import time
import keyboard

Point = collections.namedtuple("Point", "x y")


class Potion:
    def __init__(self, win):
        self.selection = []
        self.window = win
        self.stop_making = False
        self.placements = [
            Point(x=1042, y=304),
            Point(x=1128, y=304),
            Point(x=1186, y=306),
            Point(x=1264, y=312),
            Point(x=1330, y=314),
            Point(x=1398, y=320),
            Point(x=1474, y=340)
        ]

    def scroll(self):
        x = self
        for _ in range(2):
            mouse.move(1452, 834)
            mouse.click()

    def select(self):
        #self.scroll()  # Disable if t1
        #time.sleep(.2)  # Disable if t1
        mouse.move(*self.selection)
        mouse.click()
        time.sleep(.5)
        mouse.move(1208, 574)
        mouse.click()

    def create(self):
        pass


class SwiftFoot(Potion):
    def __init__(self, win):
        super().__init__(win)
        # 1 - Point(x=1134, y=296)
        # 3 - Point(x=1157, y=840)
        self.selection = Point(x=1134, y=296)

    def create(self):
        history = []
        strikes = 0
        while not self.complete:
            block_one, block_two = self.get_colors()
            if len(history) != 0:
                if history[len(history) - 1] == [block_one, block_two]:
                    strikes += 1
                else:
                    strikes = 0
                if strikes > 5:
                    self.window.click(666, 845)
                    time.sleep(.5)
                    self.window.click(1208, 573)
                    time.sleep(1)
                    return
            if block_one and block_two:
                history.append([block_one, block_two])

            if block_one == "r":
                if block_two == "r":
                    pyautogui.moveTo(self.placements[0])
                    time.sleep(.2)
                    pyautogui.click(self.placements[0])
                elif block_two == "g":
                    pyautogui.moveTo(self.placements[1])
                    time.sleep(.2)
                    pyautogui.click(self.placements[1])
                elif block_two == "b":
                    pyautogui.rightClick()
                    time.sleep(.5)
                    pyautogui.moveTo(self.placements[5])
                    time.sleep(.2)
                    pyautogui.click(self.placements[5])
            elif block_one == "g":
                if block_two == "r":
                    pyautogui.rightClick()
                    time.sleep(.5)
                    pyautogui.moveTo(self.placements[1])
                    time.sleep(.2)
                    pyautogui.click(self.placements[1])
                elif block_two == "g":
                    pyautogui.moveTo(self.placements[2])
                    time.sleep(.2)
                    pyautogui.click(self.placements[2])
                elif block_two == "b":
                    pyautogui.moveTo(self.placements[3])
                    time.sleep(.3)
                    pyautogui.click(self.placements[3])
            elif block_one == "b":
                if block_two == "r":
                    pyautogui.moveTo(self.placements[5])
                    time.sleep(.4)
                    pyautogui.click(self.placements[5])
                elif block_two == "g":
                    pyautogui.rightClick()
                    time.sleep(.2)
                    pyautogui.moveTo(self.placements[3])
                    time.sleep(.4)
                    pyautogui.click(self.placements[3])
                elif block_two == "b":
                    pyautogui.moveTo(self.placements[4])
                    time.sleep(.4)
                    pyautogui.click(self.placements[4])
        else:
            if strikes <= 5:
                pyautogui.click(1236, 687)
                time.sleep(2)

    def get_colors(self):
        mouse.move(1000, 520)
        time.sleep(.5)
        if self.window.pixel(1008, 109) == (111, 66, 37):
            return [False, False]
        colors = [
            self.window.pixel(1010, 144),
            self.window.pixel(1076, 186)
        ]
        blocks = []
        for color in colors:
            highest = max(iter(color))
            if highest == color[0]:
                blocks.append("r")
            elif highest == color[1]:
                blocks.append("g")
            elif highest == color[2]:
                blocks.append("b")
        return blocks

    @property
    def complete(self):
        return self.window.pixel(950, 487) == (254, 1, 0)

    @property
    def full(self):
        return self.window.pixel(1156, 493) == (255, 255, 255)


def stop_brewing(current_potion):
    current_potion.stop_making = True


def brew():
    potion = SwiftFoot(Window())
    while not potion.stop_making:
        if "irate" in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            potion.select()
            time.sleep(1)
            potion.create()


if __name__ == "__main__":
    time.sleep(3)
    brew()


import collections
import pyautogui
import pyscreeze
import win32api
import win32gui
import win32con
import time
import keyboard

Point = collections.namedtuple("Point", "x y")


def click(x, y=None):
    if y is None:
        y = x[1]
        x = x[0]
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


class Potion:
    def __init__(self):
        self.selection = None
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
            pyautogui.click(1452, 834)


    def select(self):
        #self.scroll()  # Disable if t1
        #time.sleep(.2)  # Disable if t1
        pyautogui.click(self.selection)
        time.sleep(.5)
        pyautogui.click(Point(x=1208, y=574))

    def create(self):
        pass


class SwiftFoot(Potion):
    def __init__(self):
        super().__init__()
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
                    pyautogui.click(666, 845)
                    time.sleep(.5)
                    pyautogui.click(1208, 573)
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
        pyautogui.moveTo(1000, 520)
        time.sleep(.5)
        if pyscreeze.pixelMatchesColor(x=1008, y=109, expectedRGBColor=(111, 66, 37), tolerance=2):
            return [False, False]
        colors = [
            pyscreeze.pixel(1010, 144),
            pyscreeze.pixel(1076, 186)
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
        return pyscreeze.pixelMatchesColor(x=950, y=487, expectedRGBColor=(254, 1, 0), tolerance=2)


def stop_brewing(current_potion):
    current_potion.stop_making = True


def brew():
    potion = SwiftFoot()
    keyboard.on_press_key("`", [potion])
    while not potion.stop_making:
        if "irate" in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            potion.select()
            time.sleep(1)
            potion.create()


if __name__ == "__main__":
    brew()

import pyautogui
from repair_mini_game import *
import time
import win32api
import win32con


class Hammering(RepairMiniGame):
    def __init__(self):
        super().__init__()
        self.name = "hammering"
        self.button = Point(x=1124, y=916),
        self.t1 = time.time()
        self.easy = [
            Point(x=756, y=482),
            Point(x=890, y=480),
            Point(x=1028, y=482),
            Point(x=1160, y=480)
        ]
        self.medium = [
            Point(x=704, y=484),
            Point(x=806, y=480),
            Point(x=906, y=482),
            Point(x=1010, y=484),
            Point(x=1116, y=484),
            Point(x=1214, y=482)
        ]
        self.hard = [
            Point(x=674, y=482),
            Point(x=756, y=482),
            Point(x=836, y=482),
            Point(x=918, y=482),
            Point(x=1008, y=482),
            Point(x=1090, y=482),
            Point(x=1162, y=482),
            Point(x=1246, y=482)
        ]

    def click_when_best(self, x, y):
        win32api.SetCursorPos((x, y))
        snap = pyscreeze.screenshot()
        if snap.getpixel((x, y + 20))[0] > 200:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            return True
        else:
            return False

    def find_nails(self):
        search_region = (560, 390, 1380 - 560, 730 - 390)
        if pyscreeze.locateOnScreen("./images/markers/hammering/easy.png", region=search_region):
            return self.easy
        elif pyscreeze.locateOnScreen("./images/markers/hammering/medium.png", region=search_region):
            return self.medium
        elif pyscreeze.locateOnScreen("./images/markers/hammering/hard.png", region=search_region):
            return self.hard
        else:
            return None

    def play(self):
        nails = None
        while not nails:
            nails = self.find_nails()
        else:
            for nail in nails:
                while not self.click_when_best(nail[0], nail[1]):
                    pass
                time.sleep(.05)


if __name__ == "__main__":
    test = Hammering()
    test.play()

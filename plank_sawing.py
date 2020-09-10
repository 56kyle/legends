import pyautogui
from repair_mini_game import *
import time
import math


class PlankSawing(RepairMiniGame):
    def __init__(self):
        super().__init__()
        self.button = Point(x=796, y=914)
        self.name = "plank_sawing"
        self.planks = {
            'forward_slash': [
                Point(x=1043, y=399),
                Point(x=832, y=826)
            ],
            'in_top_out_right': [
                Point(x=960, y=399),
                Point(x=960, y=579),
                Point(x=1274, y=579)
            ],
            'letter_n': [
                Point(x=785, y=765),
                Point(x=921, y=517),
                Point(x=999, y=647),
                Point(x=1121, y=439)
            ],
            'straight_horizontal': [
                Point(x=594, y=580),
                Point(x=1420, y=580)
            ],
            'straight_vertical': [
                Point(x=948, y=398),
                Point(x=952, y=780)
            ]
        }

    def play(self):
        plank_region = (600, 420, 730, 320)
        solved = 0
        while solved < 3:
            for plank in self.planks.keys():
                region = pyscreeze.locateOnScreen('./images/markers/plank_sawing/{}.png'.format(plank), region=plank_region)
                if region:
                    direction_list = self.planks[plank]
                    pyautogui.moveTo(direction_list[0])
                    for point in direction_list:
                        x1, y1 = pyautogui.position()
                        x2, y2 = point
                        dx = x2 - x1
                        dy = y2 - y1
                        dh = math.sqrt((dx ** 2) + (dy ** 2))
                        duration = dh * .0008
                        pyautogui.mouseDown(duration=duration)
                        pyautogui.moveTo(point, duration=duration)
                    pyautogui.mouseUp()


if __name__ == "__main__":
    test = PlankSawing()
    test.play()


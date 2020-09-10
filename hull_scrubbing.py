from repair_mini_game import *
from PIL import Image
import pyscreeze
import random
import math


class HullScrubbing(RepairMiniGame):
    def __init__(self):
        super().__init__()
        self.name = "hull_scrubbing"
        self.button = Point(x=634, y=914)

    def play(self):
        snap_region = (580, 318, 1216 - 580, 758 - 318)
        while not self.complete:
            xi, yi = pyautogui.position()

            xf = random.randint(snap_region[0], snap_region[0] + snap_region[2])
            yf = random.randint(snap_region[1], snap_region[1] + snap_region[3])

            dx = xf - xi
            dy = yf - yi
            dh = math.sqrt((dx**2)+(dy**2))
            duration = dh*.0005
            pyautogui.moveTo(xf, yf, duration=duration)


if __name__ == "__main__":
    test = HullScrubbing()
    time.sleep(2)
    test.play()

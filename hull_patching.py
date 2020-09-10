import pyautogui
from repair_mini_game import *
import time
from PIL import Image


class HullPatching(RepairMiniGame):
    def __init__(self):
        super().__init__()
        self.needed = 7
        self.button = Point(x=1285, y=918)
        self.patched_holes = 0
        self.holes = [
            Point(x=730, y=431),
            Point(x=870, y=431),
            Point(x=874, y=699),
            Point(x=1226, y=699),
            Point(x=874, y=559),
            Point(x=1188, y=489),
            Point(x=984, y=371),
            Point(x=1122, y=369),
            Point(x=872, y=691),
            Point(x=702, y=367),
            Point(x=1226, y=433),
            Point(x=1056, y=627),
            Point(x=1058, y=357),
            Point(x=1156, y=565),
            Point(x=724, y=431),
            Point(x=868, y=693),
            Point(x=1228, y=435),
            Point(x=1156, y=695),
            Point(x=736, y=557),
            Point(x=838, y=487),
            Point(x=732, y=697),
            Point(x=1022, y=703),
            Point(x=1046, y=491),
            Point(x=938, y=557)
        ]
        self.name = "hull_patching"

    def play(self):
        holes_patched = 0
        needed = 17
        hard_needed = 32
        background = Image.open("./images/markers/hull_patching/background.png")
        keep_going = True
        while keep_going:
            pyautogui.moveTo(100, 100)
            new_snap = pyscreeze.screenshot(region=(650, 322, 1272 - 650, 752 - 322))
            new_snap.save("./images/markers/hull_patching/temp.png")
            last_click = [0, 0]
            for x in range(new_snap.width):
                for y in range(new_snap.height):
                    new_px = new_snap.getpixel((x, y))
                    if new_px == (0, 0, 0):
                        if background.getpixel((x, y)) != new_px:
                            if abs((650+x)-last_click[0]) > 40 or abs((322+y)-last_click[1]) > 40:
                                last_click = [650 + x, 322 + y]
                                pyautogui.click(650 + x, 322 + y)
                                holes_patched += 1
                                break
            if pyscreeze.locate("./images/markers/hull_patching/choose_next_game.png",
                                "./images/markers/hull_patching/temp.png"):
                return
            elif pyscreeze.locateOnScreen("./images/markers/ship_repair.PNG", region=(766, 120, 1152-766, 190-120)):
                return


if __name__ == "__main__":
    test = HullPatching()
    test.repair()

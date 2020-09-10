import pyautogui
from repair_mini_game import *
import time


class BilgePumping(RepairMiniGame):
    def __init__(self):
        super().__init__()
        self.name = "bilge_pumping"
        self.desired = "top"
        self.iterations = 0
        self.completed = False
        self.button = Point(x=634, y=914)

    def play(self):
        top_strike_point = (682, 424)
        bot_strike_point = (680, 650)
        neutral_point = (982, 570)
        p1 = None
        p2 = None
        while self.iterations <= 15:
            if p1 is None:
                p1 = pixel(top_strike_point)
            if p2 is None:
                p2 = pixel(bot_strike_point)
            if p1[1] > p2[1]:
                while p1 == pixel(top_strike_point):
                    pass
                else:
                    pyautogui.click(neutral_point)
                    p1 = (0, 0, 0)
                    p2 = pixel(bot_strike_point)
                    self.iterations += 1
            else:
                while p2 == pixel(bot_strike_point):
                    pass
                else:
                    pyautogui.click(neutral_point)
                    p2 = (0, 0, 0)
                    p1 = pixel(top_strike_point)
                    self.iterations += 1
        self.completed = True


if __name__ == "__main__":
    test = BilgePumping()
    test.play()


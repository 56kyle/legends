import win32gui, win32ui, win32con
from window_input import Window, Key
import time
from PIL import Image
import collections

Region = collections.namedtuple("Region", "top_left bot_right")


class Tlopo:
    def __init__(self, win):
        if win is None:
            self.win = Window()
        else:
            self.win = win


class OnFoot(Tlopo):
    def __init__(self, win=None):
        super().__init__(win)
        self.orientation = 0

    def turn(self, desired):
        duration = 3*(desired/360)
        if duration < 0:
            duration = abs(duration)
            self.win.press(Key.VK_A, duration=duration)
        else:
            self.win.press(Key.VK_D, duration=duration)

    def keep_jumping(self):
        self.win.key_down(Key.VK_SPACE)

    def sword_combo(self):
        for _ in range(5):
            self.win.press(Key.VK_CONTROL)
            time.sleep(1)

    def record_loot(self):
        loot_area = Region((452, 338), (872, 516))
        return self.win.capture(loot_area)


class Sailing(Tlopo):
    def __init__(self, win=None):
        super().__init__(win)

    def circle(self, clockwise=True):
        if clockwise:
            button = Key.VK_D
        else:
            button = Key.VK_A
        self.win.press(button, duration=.1)
        time.sleep(.4)
        self.fire()

    @property
    def should_fire(self):
        for x in range(1790, 1850):
            for y in range(90, 140):
                if self.win.pixel(x, y).r > 200:
                    return True
        return False

    def fire(self, sides=None):
        if sides is None:
            sides = [True, True]
        if sides[0]:
            self.win.press(Key.VK_1, duration=.06)
        if sides[1]:
            self.win.press(Key.VK_2, duration=.06)




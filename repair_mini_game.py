import pyautogui
import collections
import win32gui
import win32api
import win32ui
import pyscreeze
import mouse
import time

Point = collections.namedtuple("Point", "x y")
Color = collections.namedtuple("Color", "r g b")


def rgbint2rgbtuple(rgb_int):
    blue = rgb_int & 255
    green = (rgb_int >> 8) & 255
    red = (rgb_int >> 16) & 255
    return red, green, blue


def pixel(x, y=None):
    if y is None:
        y = x[1]
        x = x[0]
    try:
        window = win32gui.FindWindow(None, "The Legend of Pirates Online [BETA]")
        dc = win32gui.GetWindowDC(window)
        colorref = win32gui.GetPixel(dc, x+8, y+8)
    except:
        print("woops")
        return 0, 0, 0
    win32gui.DeleteDC(dc)
    return rgbint2rgbtuple(colorref)


def points_to_region(p1, p2=None):
    if p2 is None:
        p2, p1 = p1
    xi = min(p1[0], p2[0])
    xf = max(p1[0], p2[0])
    yi = min(p1[1], p2[1])
    yf = max(p1[1], p2[1])
    return [xi, yi, xf-xi, yf-yi]


class RepairMiniGame:
    def __init__(self):
        self.name = None
        self.button = None
        self.completed = False
        self.snapshot = "./images/markers/temp.png"

    @property
    def active(self):
        activity = pyscreeze.locateOnScreen("./images/markers/{name}/{name}.png".format(name=self.name), region=(754, 112, 1162-754, 306-112))
        if activity:
            return True
        else:
            return False

    @property
    def complete(self):
        if pyscreeze.locateOnScreen("./images/markers/{name}/{name}_completion.png".format(name=self.name), region=(518, 856, 1406-518, 978-856)):
            return True
        else:
            return False

    @property
    def time_stopped(self):
        time_shot = pyscreeze.screenshot("./images/markers/timer_timestamp.png", region=(886, 760, 1034-886, 818-760))
        time.sleep(1)
        return True

    def play(self):
        pass

    def repair(self):
        if self.button:
            pyautogui.click(self.button)
            self.play()

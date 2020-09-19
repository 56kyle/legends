import pyscreeze
import pyautogui
import collections
import time
import mouse
import random
import win32api, win32con, win32gui
from repair_mini_game import *
import tracking
from chat import display
import random
from PIL import Image
import keyboard
from window_input import Window, Key
import tlopo_util
import os

Point = collections.namedtuple("Point", "x y")
FAMED = 1001
LEGENDARY = 1002

class Twin:
    def __init__(self, tlopo, target="forsaken"):
        self.window = tlopo
        self.target = target
        self.health_bar_height = 111
        self.boss_color = {
            "forsaken": (81, 86, 72),
            "cicatriz": (79, 15, 24),
            "darkheart": (14, 9, 3),
            "eitc": (177, 177, 168),
            "navy": (160, 106, 96)
        }
        self.boss_check_point = Point(x=834, y=93)
        self.looted = True

    @property
    def spawning(self):
        r, g, b = self.window.pixel(883, 47)
        return (r, g, b) == (251, 247, 231)

    @property
    def is_alive(self):
        x, y = self.boss_check_point
        px = self.window.pixel(x, y)
        px2 = self.boss_color[self.target]
        matches = True
        for i in range(2):
            if abs(px[i]-px2[i]) > 10:
                matches = False
        return matches

    @property
    def is_fighting(self):
        black_x = 1124
        black_y = 111
        px = pixel(black_x, black_y)
        return px[0] < 10 and px[1] < 10 and px[2] < 10


def once(tlopo):
    tlopo.press(Key.VK_CONTROL)


def farm(tlopo, attack, track_now=True, collect=False, delay=True, jump=True, post_kill_sequence=None, target="forsaken"):
    twin = Twin(tlopo, target)
    space = False

    while True:
        if twin.is_alive:
            twin.looted = False
            if twin.is_fighting or not delay:
                if not twin.spawning:
                    if not space and jump:
                        tlopo.key_down(Key.VK_SPACE)
                    attack(tlopo)
        else:
            if jump:
                tlopo.key_up(Key.VK_SPACE)
                time.sleep(1)
                space = False
            if not twin.looted:
                if post_kill_sequence:
                    post_kill_sequence(tlopo)
                else:
                    rating = check_loot_rating(tlopo)
                    if track_now:
                        with open("pali.txt", "a") as file:
                            file.write(str(rating))
                    if not collect:
                        if rating == 3 or rating == 2:
                            tlopo.bring_to_front()
                        elif rating != 0:
                            tlopo.click(464, 287)
                            time.sleep(1)
                            if check_loot_rating(tlopo) != 0:
                                tlopo.click(464, 287)
                    else:
                        tlopo.click(813, 527)
                twin.looted = True


def filter_loot(tlopo):
    tlopo_utility = tlopo_util.OnFoot(win=tlopo)
    rating = check_loot_rating(tlopo)

    if rating == 3 or rating == 2:
        bmpstr, bmpinfo = tlopo_utility.record_loot()
        img = tlopo_utility.win.bitmap_to_image(bmpstr, bmpinfo)
        bk = Image.open("./images/loot_background.png")
        bk_data = bk.getdata()
        new_data = []
        for i, px in enumerate(img.getdata()):
            if bk_data[i] != px:
                new_data.append(px)
            else:
                new_data.append((0, 0, 0))
        img.putdata(new_data)
        if rating == 2:
            img.save("./images/looted/chests/{}.png".format(len(os.listdir("./images/looted/chests"))))
        else:
            img.save("./images/looted/skulls/{}.png".format(len(os.listdir("./images/looted/skulls"))))
        rar = detect_rarity(img)
        tlopo.bring_to_front()
        if rar == LEGENDARY:
            pyautogui.click(800, 525)
            tlopo.click(800, 525)
        else:
            tlopo.click(464, 287)

    elif rating != 0:
        tlopo.click(464, 287)
        time.sleep(1)
        if check_loot_rating(tlopo) != 0:
            tlopo.click(464, 287)


def detect_rarity(img):
    for x in range(70, 200):
        for y in range(img.height):
            px = img.getpixel((x, y))
            if is_legendary_colored(px):
                return LEGENDARY
            elif is_famed_colored(px):
                return FAMED

    for x in range(270, img.width):
        for y in range(img.height):
            px = img.getpixel((x, y))
            if is_legendary_colored(px):
                return LEGENDARY
            elif is_famed_colored(px):
                return FAMED
    return False


def is_legendary_colored(px):
    return px[0] > 200 and px[1] < 30 and px[2] < 30


def is_famed_colored(px):
    return px[0] < 30 and px[1] > 200 and px[2] < 30


def channel_full(tlopo, color=(76, 153, 255), key=Key.VK_CONTROL):
    # Take Aim - (76, 153, 255)
    # Cast Spell - (255, 179, 179)
    tlopo.key_down(key)
    ti = time.time()
    r, g, b = (0, 0, 0)
    while not (r, g, b) == color or time.time() > ti + 6:
        r, g, b = pixel(Point(x=1182, y=643))
    else:
        tlopo.key_up(key)


def throw_4_daggers(tlopo):
    d = .1
    tlopo.press(Key.VK_CONTROL, duration=d)
    time.sleep(.5)
    tlopo.press(Key.VK_CONTROL, duration=d)
    time.sleep(.5)
    tlopo.press(Key.VK_CONTROL, duration=d)
    time.sleep(.6)
    tlopo.press(Key.VK_CONTROL, duration=d)
    time.sleep(2)


def swing_sword(tlopo):
    tlopo.press(Key.VK_CONTROL)
    time.sleep(1)


def run_and_filter(tlopo):
    tlopo.press(Key.VK_W, duration=3.7496514320373535)
    filter_loot(tlopo)
    time.sleep(1)
    tlopo.press(Key.VK_F1)
    time.sleep(3)
    tlopo.press(Key.VK_F1)
    util = tlopo_util.OnFoot(tlopo)
    util.turn(180)
    tlopo.press(Key.VK_W, duration=3.7496514320373535)
    util.turn(180)
    time.sleep(5)


def check_loot_rating(tlopo):
    for i in range(4):
        tlopo.press(Key.VK_SHIFT)
        time.sleep(.5)
    time.sleep(2)

    points = [
        Point(x=579, y=517),
        Point(x=603, y=517),
        Point(x=629, y=517)
    ]
    skulls = 0
    for p in points:
        px = tlopo.pixel(p)
        if px[0] > 200 and px[1] > 200 and px[2] > 200:
            skulls += 1
    return skulls

def view_loot():
    looted = 0
    famed = 0
    legendaries = 0
    for file in os.listdir("./images/looted"):
        img = Image.open("./images/looted/"+file)
        rar = detect_rarity(img)
        if rar != FAMED and rar != LEGENDARY:
            looted += 1
        elif rar == FAMED:
            looted += 1
            famed += 1
        elif rar == LEGENDARY:
            looted += 1
            legendaries += 1
    print(looted)
    print(famed)
    print(legendaries)


if __name__ == "__main__":
    time.sleep(3)
    tlopo = Window()
    kwargs = {"attack": swing_sword, "track_now": False, "collect": False, "delay": False, "jump": False, "post_kill_sequence": filter_loot, "target": "eitc"}
    farm(tlopo, **kwargs)


import pyautogui
import time
from repair_mini_game import *
import keyboard
import mouse
from window_input import Window, Key

top_strike_point = (787, 420)
bot_strike_point = (787, 648)


def show_pixels():
    win = Window()
    px = pyautogui.position()
    print(px)
    print(win.pixel(834, 93))


if __name__ == "__main__":
    x = mouse.on_click(show_pixels)
    while type(x) != int:
        pass


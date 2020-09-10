from hull_scrubbing import HullScrubbing
from bilge_pumping import BilgePumping
from plank_sawing import PlankSawing
from hull_bracing import HullBracing
from hammering import Hammering
from hull_patching import HullPatching
import keyboard
import pyscreeze
import time
import pyautogui


def repair_callback(*args):
    games = [
        #BilgePumping,
        PlankSawing,
        #HullBracing,
        Hammering,
        HullPatching
    ]
    for game in games:
        mini_game = game()
        mini_game.repair()


if __name__ == "__main__":
    keyboard.on_press_key(key="`", callback=repair_callback)
    while True:
        pass

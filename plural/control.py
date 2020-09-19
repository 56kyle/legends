
from window_input import Window, Key
import win32api, win32gui, win32con
import mouse
import keyboard
import time


class Controller:
    def __init__(self):
        self.pirates = []
        self.adding = True
        self.conversions = {"ctrl": Key.VK_CONTROL, "w": Key.VK_W, "a": Key.VK_A, "s": Key.VK_S, "d": Key.VK_D, "space": Key.VK_SPACE, "esc": Key.VK_ESCAPE}
        self.pressed = []

    def add_pirate(self):
        if self.adding:
            self.pirates.append(Window())

    def lock_pirates(self, *args):
        self.adding = False

    def key_down(self, event):
        print(event.name)
        if event.name in self.conversions.keys():
            for win in self.pirates:
                win.key_down(self.conversions[event.name])
                self.pressed.append(event.name)


if __name__ == "__main__":
    controller = Controller()
    mouse.on_right_click(controller.add_pirate)
    keyboard.on_press_key("`", controller.lock_pirates)

    keyboard.on_press(controller.key_down)
    while True:
        for name in controller.pressed:
            if not keyboard.is_pressed(name):
                for win in controller.pirates:
                    win.key_up(controller.conversions[name])
                controller.pressed.remove(name)


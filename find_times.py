
import win32api
import win32gui
import win32con
import mouse
import keyboard
import time
import re


class Timer:
    def __init__(self):
        self.t1 = time.time()
        self.times = []

    def mark_time(self):
        t2 = time.time()
        self.times.append(t2 - self.t1)
        self.t1 = t2
        print(self.times[-1])


class Mimic:
    def __init__(self):
        self.actions = []
        self.t1 = time.time()
        self.recording = True

    def record(self, button, val):
        self.recording = True
        if len(self.actions) == 0:
            self.actions.append(Action(button, val, time.time()))
        else:
            self.actions.append(Action(button, val, self.actions[-1].timestamp))

    def end_recording(self, *args):
        self.recording = False

    def save(self, name="test"):
        with open("./{}.py".format(name), "w") as file:
            file.write('ACTIONS = [\n')
            for i, action in enumerate(self.actions):
                file.write('    {\n')
                file.write('        "button":    "{}",\n'.format(action.button))
                file.write('        "action":    "{}",\n'.format(action.action))
                file.write('        "delay":    "{}"\n'.format(action.delay))
                file.write("    },\n")
            file.write("]\n")

    def play(self):
        for action in self.actions:
            try:
                action.delay
            except AttributeError:
                action = Action(action['button'], action['action'], None, delay=float(action['delay']))
            time.sleep(action.delay)
            if action.action == mouse.UP:
                mouse.release(action.button)
            elif action.action == mouse.DOWN:
                mouse.press(action.button)
            elif action.action == mouse.DOUBLE:
                mouse.double_click(action.button)


class Action:
    def __init__(self, button, val, ti=None, delay=None):
        self.timestamp = time.time()
        if ti:
            self.delay = self.timestamp - ti
        elif delay:
            self.delay = delay
        else:
            print("WTF")
        self.button = button
        self.action = val


def record_and_save(file):
    timer = Timer()
    mimic = Mimic()
    buttons = (mouse.LEFT, mouse.MIDDLE, mouse.RIGHT, mouse.X, mouse.X2)
    values = (mouse.UP, mouse.DOWN, mouse.DOUBLE)
    for button in buttons:
        for val in values:
            mouse.on_button(mimic.record, args=(button, val), buttons=(button,), types=(val,))

    keyboard.on_press_key("`", mimic.end_recording)

    while mimic.recording:
        pass
    else:
        mimic.save("throw_daggers")


if __name__ == "__main__":
    mimic = Mimic()

    time.sleep(2)
    mimic.play()

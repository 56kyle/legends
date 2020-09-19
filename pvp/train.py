from window_input import Window, Key
import time
import random


class Dummy:
    def __init__(self, win, **kwargs):
        self.win = win
        self.kwargs = kwargs
        print(kwargs)

    def run(self):
        if "movement_function" in self.kwargs.keys():
            self.kwargs["movement_function"](self.win)


def move_random(win):
    swap = 0
    while True:
        win.key_down(Key.VK_SPACE)
        win.key_down(Key.VK_W)
        if swap == 0:
            win.key_up(Key.VK_D)
            win.key_down(Key.VK_A)
        else:
            win.key_up(Key.VK_A)
            win.key_down(Key.VK_D)
        while roll_state_change():
            win.key_up(Key.VK_SPACE)
            win.key_up(Key.VK_W)
            win.key_down(Key.VK_SPACE)
            win.key_down(Key.VK_W)
            time.sleep(.5)
        else:
            if swap == 1:
                swap = 0
            else:
                swap = 1


def roll_state_change():
    val = random.randint(0, 10)
    if val != 1:
        return True
    else:
        return False


if __name__ == "__main__":
    time.sleep(4)
    target = Dummy(Window(), movement_function=move_random)
    target.run()





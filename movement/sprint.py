
from window_input import Window, Key
import time

if __name__ == "__main__":
    time.sleep(2)
    win = Window()
    win.key_down(Key.VK_W)
    t1 = time.time()
    d = .1
    while time.time() < t1 + 5:
        #win.press(Key.VK_A, duration=d)
        #win.press(Key.VK_D, duration=d)
        pass
    win.key_up(Key.VK_W)


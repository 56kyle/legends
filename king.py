from window_input import Window, Key
import time
from tlopo_util import *


def swing_jump(tlopo):
    ti = time.time()
    tlopo.key_down(Key.VK_CONTROL)
    tlopo.key_down(Key.VK_SPACE)
    time.sleep(.1)
    tlopo.key_up(Key.VK_CONTROL)
    while not ti + 1 < time.time():
        tlopo.key_up(Key.VK_SPACE)
        time.sleep(.1)
        tlopo.key_down(Key.VK_SPACE)
    else:
        tlopo.key_up(Key.VK_SPACE)


def test_swing():
    while True:
        tlopo.key_down(Key.VK_CONTROL)
        time.sleep(.1)
        tlopo.key_up(Key.VK_CONTROL)
        time.sleep(.1)


if __name__ == "__main__":
    time.sleep(2)
    tlopo = Window()
    test_swing()
    #while True:
        #swing_jump(tlopo)

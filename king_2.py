from window_input import Window, Key
import time
from king import swing_jump


if __name__ == "__main__":
    time.sleep(3)
    tlopo = Window()
    while True:
        swing_jump(tlopo)


import pyscreeze
import mouse
import time
import win32api
import win32con


def record_frames():
    x, y = win32api.GetCursorPos()
    print(x)
    print(y)
    print(pyscreeze.pixel(x, y))


if __name__ == "__main__":
    mouse.on_right_click(record_frames)
    while True:
        pass

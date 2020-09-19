
from window_input import Window, Key
import asyncio
import win32api, win32gui, win32con


class Session:
    def __init__(self):
        self.pirates = []

    def find_pirates(self, hwnd, *args):
        if win32gui.GetWindowText(hwnd) == "The Legend of Pirates Online [BETA]":
            self.pirates.append(Window(hwnd))


if __name__ == "__main__":
    session = Session()
    win32gui.EnumWindows(session.find_pirates, ())
    print(session.pirates)

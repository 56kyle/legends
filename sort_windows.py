
from window_input import Window, Key
import win32api, win32gui, win32con
import math


class WindowManager:
    def __init__(self):
        self.windows = []
        win32gui.EnumWindows(self.find_windows, ())

    def find_windows(self, hwnd, *args):
        if win32gui.GetWindowText(hwnd) == "The Legend of Pirates Online [BETA]":
            self.windows.append(Window(hwnd))

    def sort(self):
        width = win32api.GetSystemMetrics(0)
        height = win32api.GetSystemMetrics(1)
        length = len(self.windows)
        rows = math.floor(math.sqrt(length))
        print("Rows - {}".format(rows))
        columns = math.ceil(length/rows)
        print("Columns - {}".format(columns))
        for i, win in enumerate(self.windows):
            column = i % columns
            row = math.floor((i-column)/rows)
            print("Row - {}".format(row))
            print("Column - {}".format(column))

            xi = int(column*(width/columns))
            yi = int(row*(height/rows))
            w = int(width/columns)
            h = int(height/rows)
            self.make_box(win.hwnd, (xi, yi, w, h))

    def make_box(self, hwnd, region):
        print("Moving to {}".format(region))
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.MoveWindow(hwnd, *region, True)


if __name__ == "__main__":
    wm = WindowManager()
    wm.sort()

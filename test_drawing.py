import win32api
import win32gui
import win32con


def RGB(r, g, b):
    r = r & 0xFF
    g = g & 0xFF
    b = b & 0xFF
    return (b << 16) | (g << 8) | r


def draw(x, y):
    win = win32gui.GetForegroundWindow()
    dc = win32gui.GetWindowDC(win)
    win32gui.SetPixel(dc, x, y, RGB(255, 255, 255))
    win32gui.ReleaseDC(win, dc)


if __name__ == "__main__":
    while True:
        draw(500, 500)

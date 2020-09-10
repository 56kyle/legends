import win32gui, win32con


def RGB(r, g, b):
    r = r & 0xFF
    g = g & 0xFF
    b = b & 0xFF
    return (b << 16) | (g << 8) | r


def display():
    chat_region = (40, 753, 400, 200)

    foreground = win32gui.GetForegroundWindow()
    dc = win32gui.GetWindowDC(foreground)

    pirate_win = win32gui.FindWindow(None, "The Legend of Pirates Online [BETA]")
    pirate_dc = win32gui.GetWindowDC(pirate_win)

    win32gui.BitBlt(dc, chat_region[0], chat_region[1], chat_region[2], chat_region[3], pirate_dc, chat_region[0],
                    chat_region[1], win32con.SRCCOPY)

    win32gui.ReleaseDC(foreground, dc)
    win32gui.ReleaseDC(pirate_win, pirate_dc)


if __name__ == "__main__":
    while True:
        display()
from window_input import Window, Key
import pyautogui
import mouse
import time


def win_a():
    pyautogui.hotkey("winleft", "a")


def toggle_wifi():
    win_a()
    time.sleep(.6)
    mouse.move(1853, 863)
    time.sleep(.2)
    pyautogui.click(duration=.3)
    time.sleep(.6)
    win_a()


def accept_retrain():
    mouse.move(916, 659)
    pyautogui.click(duration=.1)
    pyautogui.press("escape")


def learn_flourish():
    pyautogui.press("k")
    pyautogui.click(1668, 419, duration=.1)
    pyautogui.click(1668, 419, duration=.1)
    pyautogui.click(1668, 419, duration=.1)
    pyautogui.click(1668, 419, duration=.1)
    pyautogui.click(1668, 419, duration=.1)
    pyautogui.click(1668, 419, duration=.1)
    pyautogui.click(1668, 419, duration=.1)
    pyautogui.click(1668, 419, duration=.1)


if __name__ == "__main__":
    time.sleep(3)
    toggle_wifi()
    time.sleep(.2)
    accept_retrain()
    time.sleep(.2)
    learn_flourish()
    time.sleep(.1)
    toggle_wifi()


import mouse
import keyboard
import time
import win32gui


PIRATES = 4


def click():
    mouse.click()
    time.sleep(.1)
    mouse.release()


def open_launcher():
    mouse.move(1054, 1061)
    click()
    while win32gui.GetWindowText(win32gui.GetForegroundWindow()) != "The Legend of Pirates Online":
        pass


def select_username():
    mouse.move(1128, 468)
    click()


def enter_info(num, pwd):
    keyboard.write("56kyle"+num)
    keyboard.press_and_release("tab")
    keyboard.write(pwd+num)
    keyboard.press_and_release("enter")


def login(num, pwd):
    open_launcher()
    select_username()
    enter_info(num, pwd)


if __name__ == "__main__":
    password = input("Please enter your password: ")
    for _ in range(50):
        print("\n")

    for i in range(2, 6):
        login(str(i), password)


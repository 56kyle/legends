
import keyboard
import time
import re
import sqlite3


class Tracker:
    def track(self, arg):
        val = arg
        conn = sqlite3.connect("./palifico.db")
        c = conn.cursor()
        c.execute("INSERT INTO Round (loot) VALUES ('{}')".format(val))
        conn.commit()
        conn.close()
        self.view()

    def view(self):
        conn = sqlite3.connect("./palifico.db")
        c = conn.cursor()
        values = ["None", "Pouch", "Chest", "Skull"]
        totals = {'Rounds': len(c.execute("SELECT loot FROM Round").fetchall())}
        for value in values:
            totals[value] = len(c.execute("SELECT loot FROM Round WHERE loot=?", (value,)).fetchall())
        print(totals)

    def input_none(self, *args):
        self.track("None")

    def input_pouch(self, *args):
        self.track("Pouch")

    def input_chest(self, *args):
        self.track("Chest")

    def input_skull(self, *args):
        self.track("Skull")


if __name__ == "__main__":
    tracker = Tracker()

    keyboard.on_press_key("7", tracker.input_none)
    keyboard.on_press_key("8", tracker.input_pouch)
    keyboard.on_press_key("9", tracker.input_chest)
    keyboard.on_press_key("0", tracker.input_skull)
    while True:
        pass


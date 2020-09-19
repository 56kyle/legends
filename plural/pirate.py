
from window_input import Window, Key
import asyncio
import time
import pyautogui

LEGENDARY = 1001
FAMED = 1002
RARE = 1003
COMMON = 1002

class Target:
    def __init__(self, window):
        self.window = window
        self.looted = True

    @property
    def alive(self):
        possible = [(81, 86, 72), (79, 15, 24), (14, 9, 3), (177, 177, 168), (160, 106, 96)]
        px = self.window.pixel(834, 93)
        return px in possible

    @property
    def spawning(self):
        r, g, b = self.window.pixel(883, 47)
        return (r, g, b) == (251, 247, 231)

class Pirate:
    def __init__(self, window):
        self.window = window

    async def farm(self):
        target = Target()
        if target.alive:
            if not target.spawning:
                await self.fight()
        else:
            if not target.looted:
                await self.loot()

    async def loot(self):
        rating = await self.rate_loot()
        await self.filter_loot(rating)

    async def rate_loot(self):
        for i in range(4):
            self.window.key_down(Key.VK_SHIFT)
            await asyncio.sleep(.1)
            self.window.key_up(Key.VK_SHIFT)
            await asyncio.sleep(.5)
        await asyncio.sleep(2)
        points = [
            (579, 517),
            (603, 517),
            (629, 517)
        ]
        skulls = 0
        for p in points:
            px = self.window.pixel(p)
            if px[0] > 200 and px[1] > 200 and px[2] > 200:
                skulls += 1
        return skulls

    async def filter_loot(self, rating):
        if rating == LEGENDARY:
            self.window.click(800, 525)
        elif rating == FAMED:
            await self.trash()
        elif rating == RARE:
            await self.trash()
        elif rating == COMMON:
            await self.trash()
        else:
            await self.trash()

    async def trash(self):
        self.window.click(464, 287)

    async def fight(self):
        pass




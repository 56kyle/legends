import collections

Point = collections.namedtuple("Point", "x y")
Color = collections.namedtuple("Color", "r g b")

RED = "Red"
GREEN = "Green"
BLUE = "Blue"
PURPLE = "Purple"
GOLD = "Gold"
ORANGE = "Orange"
COLORS = [RED, GREEN, BLUE, PURPLE, GOLD, ORANGE]


class Piece:
    up_next = [None, None]
    column_results = [None, None, None, None, None, None, None, None]

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

    def __eq__(self, other):
        if isinstance(other, Piece):
            return self.color == other.color
        else:
            return self.color == other


class Red(Piece):
    up_next = [
        Color(r=131, g=38, b=35),
        Color(r=150, g=22, b=19)
    ]
    column_results = [
        Color(r=142, g=32, b=27),
        Color(r=149, g=26, b=11),
        Color(r=157, g=25, b=19),
        Color(r=152, g=25, b=9),
        Color(r=151, g=26, b=8),
        Color(r=156, g=24, b=8),
        Color(r=155, g=24, b=1),
        Color(r=141, g=30, b=34)
    ]

    def __init__(self):
        super().__init__(RED)


class Green(Piece):
    up_next = [
        Color(r=79, g=115, b=39),
        Color(r=105, g=149, b=64)
    ]
    column_results = [
        Color(r=86, g=118, b=47),
        Color(r=100, g=141, b=58),
        Color(r=112, g=153, b=78),
        Color(r=100, g=141, b=58),
        Color(r=88, g=124, b=40),
        Color(r=100, g=141, b=58),
        Color(r=86, g=123, b=40),
        Color(r=102, g=142, b=51)
    ]

    def __init__(self):
        super().__init__(GREEN)


class Blue(Piece):
    up_next = [
        Color(r=70, g=113, b=184),
        Color(r=57, g=74, b=115)
    ]
    column_results = [
        Color(r=82, g=121, b=198),
        Color(r=78, g=106, b=169),
        Color(r=55, g=78, b=119),
        Color(r=77, g=105, b=170),
        Color(r=88, g=119, b=190),
        Color(r=77, g=105, b=170),
        Color(r=86, g=116, b=188),
        Color(r=83, g=111, b=166)
    ]

    def __init__(self):
        super().__init__(BLUE)


class Purple(Piece):
    def __init__(self):
        super().__init__(PURPLE)


class Gold(Piece):
    def __init__(self):
        super().__init__(GOLD)


class Orange(Piece):
    def __init__(self):
        super().__init__(ORANGE)


COLOR_CLASSES = [Red, Green, Blue, Purple, Gold, Orange]

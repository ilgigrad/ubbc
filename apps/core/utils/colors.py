import random

ORANGE = "#df5f25"
GREEN = "#b5b42a"
LEAVE = "#643c12"
ROSE = "#c9b5C1"
OLIVE = "#769157"
STRAWBERRY = "#b13f4f"
GREY = "#808290"
PRUNE = "#150927"
NAVY = "#16537e"
SADSEA = "#72b2c5"
GOLD = "#f2b502"
PEACH = "#e5625c"
APRICOT = "#f9bf76"

COLORS = (
    ORANGE,
    GREEN,
    LEAVE,
    ROSE,
    OLIVE,
    STRAWBERRY,
    GREY,
    PRUNE,
    NAVY,
    SADSEA,
    GOLD,
    PEACH,
    APRICOT,
)


def random_color():
    return random.choice(COLORS)


def get_luminance(hex_color):
    color = hex_color[1:]
    hex_red = int(color[0:2], base=16)
    hex_green = int(color[2:4], base=16)
    hex_blue = int(color[4:6], base=16)
    return hex_red * 0.2126 + hex_green * 0.7152 + hex_blue * 0.0722


def get_text_color(hex_color):
    if get_luminance(hex_color) < 140:
        return "#ffffff"
    return "#333333"

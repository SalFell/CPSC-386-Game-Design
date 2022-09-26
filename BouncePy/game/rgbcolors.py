# Salvador Felipe
# CPSC 386-01
# 2022-04-25
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 05-00
#
# File containing a list of RGB colors.
#


"""A list of RGB colors produced by X11's showrgb command. The color database
    is probably from an IRIX system circa 2005"""

from pygame import Color


def _clamp(val: int, min_value=0, max_value=255) -> int:
    """Clamp a value between min and max."""
    return max(min_value, min(val, max_value))


def mult_color(scalar, color):
    """Multiply a color by a scalar"""
    return tuple(map(lambda n: _clamp(n * scalar), color))


def mult_colr(color_a, color_b):
    """Multiply a color by another color."""
    return (
        _clamp(color_a[0] * color_b[0]),
        _clamp(color_a[1] * color_b[1]),
        _clamp(color_a[2] * color_b[2]),
    )


def sum_color(color_a, color_b):
    """Sum two colors together."""
    return (
        _clamp(color_a[0] + color_b[0]),
        _clamp(color_a[1] + color_b[1]),
        _clamp(color_a[2] + color_b[2]),
    )


def diff_color(color_a, color_b):
    """Take the difference of two colors."""
    return (
        _clamp(color_a[0] - color_b[0]),
        _clamp(color_a[1] - color_b[1]),
        _clamp(color_a[2] - color_b[2]),
    )


def tuple_to_color(color_tuple):
    "Given a tuple representing a color, return a Pygame color contructed from that tuple."
    return Color(*color_tuple)


SNOW = (255, 250, 250)
GHOST_WHITE = (248, 248, 255)
GHOSTWHITE = (248, 248, 255)
WHITE_SMOKE = (245, 245, 245)
WHITESMOKE = (245, 245, 245)
GAINSBORO = (220, 220, 220)
FLORAL_WHITE = (255, 250, 240)
FLORALWHITE = (255, 250, 240)
OLD_LACE = (253, 245, 230)
OLDLACE = (253, 245, 230)
LINEN = (250, 240, 230)
ANTIQUE_WHITE = (250, 235, 215)
ANTIQUEWHITE = (250, 235, 215)
PAPAYA_WHIP = (255, 239, 213)
PAPAYAWHIP = (255, 239, 213)
BLANCHED_ALMOND = (255, 235, 205)
BLANCHEDALMOND = (255, 235, 205)
BISQUE = (255, 228, 196)
PEACH_PUFF = (255, 218, 185)
PEACHPUFF = (255, 218, 185)
NAVAJO_WHITE = (255, 222, 173)
NAVAJOWHITE = (255, 222, 173)
MOCCASIN = (255, 228, 181)
CORNSILK = (255, 248, 220)
IVORY = (255, 255, 240)
LEMON_CHIFFON = (255, 250, 205)
LEMONCHIFFON = (255, 250, 205)
SEASHELL = (255, 245, 238)
HONEYDEW = (240, 255, 240)
MINT_CREAM = (245, 255, 250)
MINTCREAM = (245, 255, 250)
AZURE = (240, 255, 255)
ALICE_BLUE = (240, 248, 255)
ALICEBLUE = (240, 248, 255)
LAVENDER = (230, 230, 250)
LAVENDER_BLUSH = (255, 240, 245)
LAVENDERBLUSH = (255, 240, 245)
MISTY_ROSE = (255, 228, 225)
MISTYROSE = (255, 228, 225)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_SLATE_GRAY = (47, 79, 79)
DARKSLATEGRAY = (47, 79, 79)
DARK_SLATE_GREY = (47, 79, 79)
DARKSLATEGREY = (47, 79, 79)
DIM_GRAY = (105, 105, 105)
DIMGRAY = (105, 105, 105)
DIM_GREY = (105, 105, 105)
DIMGREY = (105, 105, 105)
SLATE_GRAY = (112, 128, 144)
SLATEGRAY = (112, 128, 144)
SLATE_GREY = (112, 128, 144)
SLATEGREY = (112, 128, 144)
LIGHT_SLATE_GRAY = (119, 136, 153)
LIGHTSLATEGRAY = (119, 136, 153)
LIGHT_SLATE_GREY = (119, 136, 153)
LIGHTSLATEGREY = (119, 136, 153)
GRAY = (190, 190, 190)
GREY = (190, 190, 190)
LIGHT_GREY = (211, 211, 211)
LIGHTGREY = (211, 211, 211)
LIGHT_GRAY = (211, 211, 211)
LIGHTGRAY = (211, 211, 211)
MIDNIGHT_BLUE = (25, 25, 112)
MIDNIGHTBLUE = (25, 25, 112)
NAVY = (0, 0, 128)
NAVY_BLUE = (0, 0, 128)
NAVYBLUE = (0, 0, 128)
CORNFLOWER_BLUE = (100, 149, 237)
CORNFLOWERBLUE = (100, 149, 237)
DARK_SLATE_BLUE = (72, 61, 139)
DARKSLATEBLUE = (72, 61, 139)
SLATE_BLUE = (106, 90, 205)
SLATEBLUE = (106, 90, 205)
MEDIUM_SLATE_BLUE = (123, 104, 238)
MEDIUMSLATEBLUE = (123, 104, 238)
LIGHT_SLATE_BLUE = (132, 112, 255)
LIGHTSLATEBLUE = (132, 112, 255)
MEDIUM_BLUE = (0, 0, 205)
MEDIUMBLUE = (0, 0, 205)
ROYAL_BLUE = (65, 105, 225)
ROYALBLUE = (65, 105, 225)
BLUE = (0, 0, 255)
DODGER_BLUE = (30, 144, 255)
DODGERBLUE = (30, 144, 255)
DEEP_SKY_BLUE = (0, 191, 255)
DEEPSKYBLUE = (0, 191, 255)
SKY_BLUE = (135, 206, 235)
SKYBLUE = (135, 206, 235)
LIGHT_SKY_BLUE = (135, 206, 250)
LIGHTSKYBLUE = (135, 206, 250)
STEEL_BLUE = (70, 130, 180)
STEELBLUE = (70, 130, 180)
LIGHT_STEEL_BLUE = (176, 196, 222)
LIGHTSTELLBLUE = (176, 196, 222)
LIGHT_BLUE = (173, 216, 230)
LIGHTBLUE = (173, 216, 230)
POWDER_BLUE = (176, 224, 230)
POWDERBLUE = (176, 224, 230)
PALE_TURQUOISE = (175, 238, 238)
PALETURQUOISE = (175, 238, 238)
DARK_TURQUOISE = (0, 206, 209)
DARKTURQUOISE = (0, 206, 209)
MEDIUM_TURQUOISE = (72, 209, 204)
MEDIUMTURQUOISE = (72, 209, 204)
TURQUOISE = (64, 224, 208)
CYAN = (0, 255, 255)
LIGHT_CYAN = (224, 255, 255)
LIGHTCYAN = (224, 255, 255)
CADET_BLUE = (95, 158, 160)
CADETBLUE = (95, 158, 160)
MEDIUM_AQUAMARINE = (102, 205, 170)
MEDIUMAQUAMARINE = (102, 205, 170)
AQUAMARINE = (127, 255, 212)
DARK_GREEN = (0, 100, 0)
DARKGREEN = (0, 100, 0)
DARK_OLIVE_GREEN = (85, 107, 47)
DARKOLIVEGREEN = (85, 107, 47)
DARK_SEA_GREEN = (143, 188, 143)
DARKSEAGREEN = (143, 188, 143)
SEA_GREEN = (46, 139, 87)
SEAGREEN = (46, 139, 87)
MEDIUM_SEA_GREEN = (60, 179, 113)
MEDIUMSEAGREEN = (60, 179, 113)
LIGHT_SEA_GREEN = (32, 178, 170)
LIGHTSEAGREEN = (32, 178, 170)
PALE_GREEN = (152, 251, 152)
PALEGREEN = (152, 251, 152)
SPRING_GREEN = (0, 255, 127)
SPRINGGREEN = (0, 255, 127)
LAWN_GREEN = (124, 252, 0)
LAWNGREEN = (124, 252, 0)
GREEN = (0, 255, 0)
CHARTREUSE = (127, 255, 0)
MEDIUM_SPRING_GREEN = (0, 250, 154)
MEDIUMSPRINGGREEN = (0, 250, 154)
GREEN_YELLOW = (173, 255, 47)
GREENYELLOW = (173, 255, 47)
LIME_GREEN = (50, 205, 50)
LIMEGREEN = (50, 205, 50)
YELLOW_GREEN = (154, 205, 50)
YELLOWGREEN = (154, 205, 50)
FOREST_GREEN = (34, 139, 34)
FORESTGREEN = (34, 139, 34)
OLIVE_DRAB = (107, 142, 35)
OLIVEDRAB = (107, 142, 35)
DARK_KHAKI = (189, 183, 107)
DARKKHAKI = (189, 183, 107)
KHAKI = (240, 230, 140)
PALE_GOLDENROD = (238, 232, 170)
PALEGOLDENROD = (238, 232, 170)
LIGHT_GOLDENROD_YELLOW = (250, 250, 210)
LIGHTGOLDENRODYELLOW = (250, 250, 210)
LIGHT_YELLOW = (255, 255, 224)
LIGHTYELLOW = (255, 255, 224)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
LIGHT_GOLDENROD = (238, 221, 130)
LIGHTGOLDENROD = (238, 221, 130)
GOLDENROD = (218, 165, 32)
DARK_GOLDENROD = (184, 134, 11)
DARKGOLDENROD = (184, 134, 11)
ROSY_BROWN = (188, 143, 143)
ROSYBROWN = (188, 143, 143)
INDIAN_RED = (205, 92, 92)
INDIANRED = (205, 92, 92)
SADDLE_BROWN = (139, 69, 19)
SADDLEBROWN = (139, 69, 19)
SIENNA = (160, 82, 45)
PERU = (205, 133, 63)
BURLYWOOD = (222, 184, 135)
BEIGE = (245, 245, 220)
WHEAT = (245, 222, 179)
SANDY_BROWN = (244, 164, 96)
SANDYBROWN = (244, 164, 96)
TAN = (210, 180, 140)
CHOCOLATE = (210, 105, 30)
FIREBRICK = (178, 34, 34)
BROWN = (165, 42, 42)
DARK_SALMON = (233, 150, 122)
DARKSALMON = (233, 150, 122)
SALMON = (250, 128, 114)
LIGHT_SALMON = (255, 160, 122)
LIGHTSALMON = (255, 160, 122)
ORANGE = (255, 165, 0)
DARK_ORANGE = (255, 140, 0)
DARKORANGE = (255, 140, 0)
CORAL = (255, 127, 80)
LIGHT_CORAL = (240, 128, 128)
LIGHTCORAL = (240, 128, 128)
TOMATO = (255, 99, 71)
ORANGE_RED = (255, 69, 0)
ORANGERED = (255, 69, 0)
RED = (255, 0, 0)
HOT_PINK = (255, 105, 180)
HOTPINK = (255, 105, 180)
DEEP_PINK = (255, 20, 147)
DEEPPINK = (255, 20, 147)
PINK = (255, 192, 203)
LIGHT_PINK = (255, 182, 193)
LIGHTPINK = (255, 182, 193)
PALE_VIOLET_RED = (219, 112, 147)
PALEVIOLETRED = (219, 112, 147)
MAROON = (176, 48, 96)
MEDIUM_VIOLET_RED = (199, 21, 133)
MEDIUMVIOLETRED = (199, 21, 133)
VIOLET_RED = (208, 32, 144)
VIOLETRED = (208, 32, 144)
MAGENTA = (255, 0, 255)
VIOLET = (238, 130, 238)
PLUM = (221, 160, 221)
ORCHID = (218, 112, 214)
MEDIUM_ORCHID = (186, 85, 211)
MEDIUMORCHID = (186, 85, 211)
DARK_ORCHID = (153, 50, 204)
DARKORCHID = (153, 50, 204)
DARK_VIOLET = (148, 0, 211)
DARKVIOLET = (148, 0, 211)
BLUE_VIOLET = (138, 43, 226)
BLUEVIOLET = (138, 43, 226)
PURPLE = (160, 32, 240)
MEDIUM_PURPLE = (147, 112, 219)
MEDIUMPURPLE = (147, 112, 219)
THISTLE = (216, 191, 216)
SNOW1 = (255, 250, 250)
SNOW2 = (238, 233, 233)
SNOW3 = (205, 201, 201)
SNOW4 = (139, 137, 137)
SEASHELL1 = (255, 245, 238)
SEASHELL2 = (238, 229, 222)
SEASHELL3 = (205, 197, 191)
SEASHELL4 = (139, 134, 130)
ANTIQUEWHITE1 = (255, 239, 219)
ANTIQUEWHITE2 = (238, 223, 204)
ANTIQUEWHITE3 = (205, 192, 176)
ANTIQUEWHITE4 = (139, 131, 120)
BISQUE1 = (255, 228, 196)
BISQUE2 = (238, 213, 183)
BISQUE3 = (205, 183, 158)
BISQUE4 = (139, 125, 107)
PEACHPUFF1 = (255, 218, 185)
PEACHPUFF2 = (238, 203, 173)
PEACHPUFF3 = (205, 175, 149)
PEACHPUFF4 = (139, 119, 101)
NAVAJOWHITE1 = (255, 222, 173)
NAVAJOWHITE2 = (238, 207, 161)
NAVAJOWHITE3 = (205, 179, 139)
NAVAJOWHITE4 = (139, 121, 94)
LEMONCHIFFON1 = (255, 250, 205)
LEMONCHIFFON2 = (238, 233, 191)
LEMONCHIFFON3 = (205, 201, 165)
LEMONCHIFFON4 = (139, 137, 112)
CORNSILK1 = (255, 248, 220)
CORNSILK2 = (238, 232, 205)
CORNSILK3 = (205, 200, 177)
CORNSILK4 = (139, 136, 120)
IVORY1 = (255, 255, 240)
IVORY2 = (238, 238, 224)
IVORY3 = (205, 205, 193)
IVORY4 = (139, 139, 131)
HONEYDEW1 = (240, 255, 240)
HONEYDEW2 = (224, 238, 224)
HONEYDEW3 = (193, 205, 193)
HONEYDEW4 = (131, 139, 131)
LAVENDERBLUSH1 = (255, 240, 245)
LAVENDERBLUSH2 = (238, 224, 229)
LAVENDERBLUSH3 = (205, 193, 197)
LAVENDERBLUSH4 = (139, 131, 134)
MISTYROSE1 = (255, 228, 225)
MISTYROSE2 = (238, 213, 210)
MISTYROSE3 = (205, 183, 181)
MISTYROSE4 = (139, 125, 123)
AZURE1 = (240, 255, 255)
AZURE2 = (224, 238, 238)
AZURE3 = (193, 205, 205)
AZURE4 = (131, 139, 139)
SLATEBLUE1 = (131, 111, 255)
SLATEBLUE2 = (122, 103, 238)
SLATEBLUE3 = (105, 89, 205)
SLATEBLUE4 = (71, 60, 139)
ROYALBLUE1 = (72, 118, 255)
ROYALBLUE2 = (67, 110, 238)
ROYALBLUE3 = (58, 95, 205)
ROYALBLUE4 = (39, 64, 139)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 0, 238)
BLUE3 = (0, 0, 205)
BLUE4 = (0, 0, 139)
DODGERBLUE1 = (30, 144, 255)
DODGERBLUE2 = (28, 134, 238)
DODGERBLUE3 = (24, 116, 205)
DODGERBLUE4 = (16, 78, 139)
STEELBLUE1 = (99, 184, 255)
STEELBLUE2 = (92, 172, 238)
STEELBLUE3 = (79, 148, 205)
STEELBLUE4 = (54, 100, 139)
DEEPSKYBLUE1 = (0, 191, 255)
DEEPSKYBLUE2 = (0, 178, 238)
DEEPSKYBLUE3 = (0, 154, 205)
DEEPSKYBLUE4 = (0, 104, 139)
SKYBLUE1 = (135, 206, 255)
SKYBLUE2 = (126, 192, 238)
SKYBLUE3 = (108, 166, 205)
SKYBLUE4 = (74, 112, 139)
LIGHTSKYBLUE1 = (176, 226, 255)
LIGHTSKYBLUE2 = (164, 211, 238)
LIGHTSKYBLUE3 = (141, 182, 205)
LIGHTSKYBLUE4 = (96, 123, 139)
SLATEGRAY1 = (198, 226, 255)
SLATEGRAY2 = (185, 211, 238)
SLATEGRAY3 = (159, 182, 205)
SLATEGRAY4 = (108, 123, 139)
lightsteelblue1 = (202, 225, 255)
lightsteelblue2 = (188, 210, 238)
lightsteelblue3 = (162, 181, 205)
lightsteelblue4 = (110, 123, 139)
lightblue1 = (191, 239, 255)
lightblue2 = (178, 223, 238)
lightblue3 = (154, 192, 205)
lightblue4 = (104, 131, 139)
lightcyan1 = (224, 255, 255)
lightcyan2 = (209, 238, 238)
lightcyan3 = (180, 205, 205)
lightcyan4 = (122, 139, 139)
paleturquoise1 = (187, 255, 255)
paleturquoise2 = (174, 238, 238)
paleturquoise3 = (150, 205, 205)
paleturquoise4 = (102, 139, 139)
cadetblue1 = (152, 245, 255)
cadetblue2 = (142, 229, 238)
cadetblue3 = (122, 197, 205)
cadetblue4 = (83, 134, 139)
turquoise1 = (0, 245, 255)
turquoise2 = (0, 229, 238)
turquoise3 = (0, 197, 205)
turquoise4 = (0, 134, 139)
cyan1 = (0, 255, 255)
cyan2 = (0, 238, 238)
cyan3 = (0, 205, 205)
cyan4 = (0, 139, 139)
darkslategray1 = (151, 255, 255)
darkslategray2 = (141, 238, 238)
darkslategray3 = (121, 205, 205)
darkslategray4 = (82, 139, 139)
aquamarine1 = (127, 255, 212)
aquamarine2 = (118, 238, 198)
aquamarine3 = (102, 205, 170)
aquamarine4 = (69, 139, 116)
darkseagreen1 = (193, 255, 193)
darkseagreen2 = (180, 238, 180)
darkseagreen3 = (155, 205, 155)
darkseagreen4 = (105, 139, 105)
seagreen1 = (84, 255, 159)
seagreen2 = (78, 238, 148)
seagreen3 = (67, 205, 128)
seagreen4 = (46, 139, 87)
palegreen1 = (154, 255, 154)
palegreen2 = (144, 238, 144)
palegreen3 = (124, 205, 124)
palegreen4 = (84, 139, 84)
springgreen1 = (0, 255, 127)
springgreen2 = (0, 238, 118)
springgreen3 = (0, 205, 102)
springgreen4 = (0, 139, 69)
green1 = (0, 255, 0)
green2 = (0, 238, 0)
green3 = (0, 205, 0)
green4 = (0, 139, 0)
chartreuse1 = (127, 255, 0)
chartreuse2 = (118, 238, 0)
chartreuse3 = (102, 205, 0)
chartreuse4 = (69, 139, 0)
olivedrab1 = (192, 255, 62)
olivedrab2 = (179, 238, 58)
olivedrab3 = (154, 205, 50)
olivedrab4 = (105, 139, 34)
darkolivegreen1 = (202, 255, 112)
darkolivegreen2 = (188, 238, 104)
darkolivegreen3 = (162, 205, 90)
darkolivegreen4 = (110, 139, 61)
khaki1 = (255, 246, 143)
khaki2 = (238, 230, 133)
khaki3 = (205, 198, 115)
khaki4 = (139, 134, 78)
lightgoldenrod1 = (255, 236, 139)
lightgoldenrod2 = (238, 220, 130)
lightgoldenrod3 = (205, 190, 112)
lightgoldenrod4 = (139, 129, 76)
lightyellow1 = (255, 255, 224)
lightyellow2 = (238, 238, 209)
lightyellow3 = (205, 205, 180)
lightyellow4 = (139, 139, 122)
yellow1 = (255, 255, 0)
yellow2 = (238, 238, 0)
yellow3 = (205, 205, 0)
yellow4 = (139, 139, 0)
gold1 = (255, 215, 0)
gold2 = (238, 201, 0)
gold3 = (205, 173, 0)
gold4 = (139, 117, 0)
goldenrod1 = (255, 193, 37)
goldenrod2 = (238, 180, 34)
goldenrod3 = (205, 155, 29)
goldenrod4 = (139, 105, 20)
darkgoldenrod1 = (255, 185, 15)
darkgoldenrod2 = (238, 173, 14)
darkgoldenrod3 = (205, 149, 12)
darkgoldenrod4 = (139, 101, 8)
rosybrown1 = (255, 193, 193)
rosybrown2 = (238, 180, 180)
rosybrown3 = (205, 155, 155)
rosybrown4 = (139, 105, 105)
indianred1 = (255, 106, 106)
indianred2 = (238, 99, 99)
indianred3 = (205, 85, 85)
indianred4 = (139, 58, 58)
sienna1 = (255, 130, 71)
sienna2 = (238, 121, 66)
sienna3 = (205, 104, 57)
sienna4 = (139, 71, 38)
burlywood1 = (255, 211, 155)
burlywood2 = (238, 197, 145)
burlywood3 = (205, 170, 125)
burlywood4 = (139, 115, 85)
wheat1 = (255, 231, 186)
wheat2 = (238, 216, 174)
wheat3 = (205, 186, 150)
wheat4 = (139, 126, 102)
tan1 = (255, 165, 79)
tan2 = (238, 154, 73)
tan3 = (205, 133, 63)
tan4 = (139, 90, 43)
chocolate1 = (255, 127, 36)
chocolate2 = (238, 118, 33)
chocolate3 = (205, 102, 29)
chocolate4 = (139, 69, 19)
firebrick1 = (255, 48, 48)
firebrick2 = (238, 44, 44)
firebrick3 = (205, 38, 38)
firebrick4 = (139, 26, 26)
brown1 = (255, 64, 64)
brown2 = (238, 59, 59)
brown3 = (205, 51, 51)
brown4 = (139, 35, 35)
salmon1 = (255, 140, 105)
salmon2 = (238, 130, 98)
salmon3 = (205, 112, 84)
salmon4 = (139, 76, 57)
lightsalmon1 = (255, 160, 122)
lightsalmon2 = (238, 149, 114)
lightsalmon3 = (205, 129, 98)
lightsalmon4 = (139, 87, 66)
orange1 = (255, 165, 0)
orange2 = (238, 154, 0)
orange3 = (205, 133, 0)
orange4 = (139, 90, 0)
darkorange1 = (255, 127, 0)
darkorange2 = (238, 118, 0)
darkorange3 = (205, 102, 0)
darkorange4 = (139, 69, 0)
coral1 = (255, 114, 86)
coral2 = (238, 106, 80)
coral3 = (205, 91, 69)
coral4 = (139, 62, 47)
tomato1 = (255, 99, 71)
tomato2 = (238, 92, 66)
tomato3 = (205, 79, 57)
tomato4 = (139, 54, 38)
orangered1 = (255, 69, 0)
orangered2 = (238, 64, 0)
orangered3 = (205, 55, 0)
orangered4 = (139, 37, 0)
red1 = (255, 0, 0)
red2 = (238, 0, 0)
red3 = (205, 0, 0)
red4 = (139, 0, 0)
debianred = (215, 7, 81)
deeppink1 = (255, 20, 147)
deeppink2 = (238, 18, 137)
deeppink3 = (205, 16, 118)
deeppink4 = (139, 10, 80)
hotpink1 = (255, 110, 180)
hotpink2 = (238, 106, 167)
hotpink3 = (205, 96, 144)
hotpink4 = (139, 58, 98)
pink1 = (255, 181, 197)
pink2 = (238, 169, 184)
pink3 = (205, 145, 158)
pink4 = (139, 99, 108)
lightpink1 = (255, 174, 185)
lightpink2 = (238, 162, 173)
lightpink3 = (205, 140, 149)
lightpink4 = (139, 95, 101)
palevioletred1 = (255, 130, 171)
palevioletred2 = (238, 121, 159)
palevioletred3 = (205, 104, 137)
palevioletred4 = (139, 71, 93)
maroon1 = (255, 52, 179)
maroon2 = (238, 48, 167)
maroon3 = (205, 41, 144)
maroon4 = (139, 28, 98)
violetred1 = (255, 62, 150)
violetred2 = (238, 58, 140)
violetred3 = (205, 50, 120)
violetred4 = (139, 34, 82)
magenta1 = (255, 0, 255)
magenta2 = (238, 0, 238)
magenta3 = (205, 0, 205)
magenta4 = (139, 0, 139)
orchid1 = (255, 131, 250)
orchid2 = (238, 122, 233)
orchid3 = (205, 105, 201)
orchid4 = (139, 71, 137)
plum1 = (255, 187, 255)
plum2 = (238, 174, 238)
plum3 = (205, 150, 205)
plum4 = (139, 102, 139)
mediumorchid1 = (224, 102, 255)
mediumorchid2 = (209, 95, 238)
mediumorchid3 = (180, 82, 205)
mediumorchid4 = (122, 55, 139)
darkorchid1 = (191, 62, 255)
darkorchid2 = (178, 58, 238)
darkorchid3 = (154, 50, 205)
darkorchid4 = (104, 34, 139)
purple1 = (155, 48, 255)
purple2 = (145, 44, 238)
purple3 = (125, 38, 205)
purple4 = (85, 26, 139)
mediumpurple1 = (171, 130, 255)
mediumpurple2 = (159, 121, 238)
mediumpurple3 = (137, 104, 205)
mediumpurple4 = (93, 71, 139)
thistle1 = (255, 225, 255)
thistle2 = (238, 210, 238)
thistle3 = (205, 181, 205)
thistle4 = (139, 123, 139)
gray0 = (0, 0, 0)
grey0 = (0, 0, 0)
gray1 = (3, 3, 3)
grey1 = (3, 3, 3)
gray2 = (5, 5, 5)
grey2 = (5, 5, 5)
gray3 = (8, 8, 8)
grey3 = (8, 8, 8)
gray4 = (10, 10, 10)
grey4 = (10, 10, 10)
gray5 = (13, 13, 13)
grey5 = (13, 13, 13)
gray6 = (15, 15, 15)
grey6 = (15, 15, 15)
gray7 = (18, 18, 18)
grey7 = (18, 18, 18)
gray8 = (20, 20, 20)
grey8 = (20, 20, 20)
gray9 = (23, 23, 23)
grey9 = (23, 23, 23)
gray10 = (26, 26, 26)
grey10 = (26, 26, 26)
gray11 = (28, 28, 28)
grey11 = (28, 28, 28)
gray12 = (31, 31, 31)
grey12 = (31, 31, 31)
gray13 = (33, 33, 33)
grey13 = (33, 33, 33)
gray14 = (36, 36, 36)
grey14 = (36, 36, 36)
gray15 = (38, 38, 38)
grey15 = (38, 38, 38)
gray16 = (41, 41, 41)
grey16 = (41, 41, 41)
gray17 = (43, 43, 43)
grey17 = (43, 43, 43)
gray18 = (46, 46, 46)
grey18 = (46, 46, 46)
gray19 = (48, 48, 48)
grey19 = (48, 48, 48)
gray20 = (51, 51, 51)
grey20 = (51, 51, 51)
gray21 = (54, 54, 54)
grey21 = (54, 54, 54)
gray22 = (56, 56, 56)
grey22 = (56, 56, 56)
gray23 = (59, 59, 59)
grey23 = (59, 59, 59)
gray24 = (61, 61, 61)
grey24 = (61, 61, 61)
gray25 = (64, 64, 64)
grey25 = (64, 64, 64)
gray26 = (66, 66, 66)
grey26 = (66, 66, 66)
gray27 = (69, 69, 69)
grey27 = (69, 69, 69)
gray28 = (71, 71, 71)
grey28 = (71, 71, 71)
gray29 = (74, 74, 74)
grey29 = (74, 74, 74)
gray30 = (77, 77, 77)
grey30 = (77, 77, 77)
gray31 = (79, 79, 79)
grey31 = (79, 79, 79)
gray32 = (82, 82, 82)
grey32 = (82, 82, 82)
gray33 = (84, 84, 84)
grey33 = (84, 84, 84)
gray34 = (87, 87, 87)
grey34 = (87, 87, 87)
gray35 = (89, 89, 89)
grey35 = (89, 89, 89)
gray36 = (92, 92, 92)
grey36 = (92, 92, 92)
gray37 = (94, 94, 94)
grey37 = (94, 94, 94)
gray38 = (97, 97, 97)
grey38 = (97, 97, 97)
gray39 = (99, 99, 99)
grey39 = (99, 99, 99)
gray40 = (102, 102, 102)
grey40 = (102, 102, 102)
gray41 = (105, 105, 105)
grey41 = (105, 105, 105)
gray42 = (107, 107, 107)
grey42 = (107, 107, 107)
gray43 = (110, 110, 110)
grey43 = (110, 110, 110)
gray44 = (112, 112, 112)
grey44 = (112, 112, 112)
gray45 = (115, 115, 115)
grey45 = (115, 115, 115)
gray46 = (117, 117, 117)
grey46 = (117, 117, 117)
gray47 = (120, 120, 120)
grey47 = (120, 120, 120)
gray48 = (122, 122, 122)
grey48 = (122, 122, 122)
gray49 = (125, 125, 125)
grey49 = (125, 125, 125)
gray50 = (127, 127, 127)
grey50 = (127, 127, 127)
gray51 = (130, 130, 130)
grey51 = (130, 130, 130)
gray52 = (133, 133, 133)
grey52 = (133, 133, 133)
gray53 = (135, 135, 135)
grey53 = (135, 135, 135)
gray54 = (138, 138, 138)
grey54 = (138, 138, 138)
gray55 = (140, 140, 140)
grey55 = (140, 140, 140)
gray56 = (143, 143, 143)
grey56 = (143, 143, 143)
gray57 = (145, 145, 145)
grey57 = (145, 145, 145)
gray58 = (148, 148, 148)
grey58 = (148, 148, 148)
gray59 = (150, 150, 150)
grey59 = (150, 150, 150)
gray60 = (153, 153, 153)
grey60 = (153, 153, 153)
gray61 = (156, 156, 156)
grey61 = (156, 156, 156)
gray62 = (158, 158, 158)
grey62 = (158, 158, 158)
gray63 = (161, 161, 161)
grey63 = (161, 161, 161)
gray64 = (163, 163, 163)
grey64 = (163, 163, 163)
gray65 = (166, 166, 166)
grey65 = (166, 166, 166)
gray66 = (168, 168, 168)
grey66 = (168, 168, 168)
gray67 = (171, 171, 171)
grey67 = (171, 171, 171)
gray68 = (173, 173, 173)
grey68 = (173, 173, 173)
gray69 = (176, 176, 176)
grey69 = (176, 176, 176)
gray70 = (179, 179, 179)
grey70 = (179, 179, 179)
gray71 = (181, 181, 181)
grey71 = (181, 181, 181)
gray72 = (184, 184, 184)
grey72 = (184, 184, 184)
gray73 = (186, 186, 186)
grey73 = (186, 186, 186)
gray74 = (189, 189, 189)
grey74 = (189, 189, 189)
gray75 = (191, 191, 191)
grey75 = (191, 191, 191)
gray76 = (194, 194, 194)
grey76 = (194, 194, 194)
gray77 = (196, 196, 196)
grey77 = (196, 196, 196)
gray78 = (199, 199, 199)
grey78 = (199, 199, 199)
gray79 = (201, 201, 201)
grey79 = (201, 201, 201)
gray80 = (204, 204, 204)
grey80 = (204, 204, 204)
gray81 = (207, 207, 207)
grey81 = (207, 207, 207)
gray82 = (209, 209, 209)
grey82 = (209, 209, 209)
gray83 = (212, 212, 212)
grey83 = (212, 212, 212)
gray84 = (214, 214, 214)
grey84 = (214, 214, 214)
gray85 = (217, 217, 217)
grey85 = (217, 217, 217)
gray86 = (219, 219, 219)
grey86 = (219, 219, 219)
gray87 = (222, 222, 222)
grey87 = (222, 222, 222)
gray88 = (224, 224, 224)
grey88 = (224, 224, 224)
gray89 = (227, 227, 227)
grey89 = (227, 227, 227)
gray90 = (229, 229, 229)
grey90 = (229, 229, 229)
gray91 = (232, 232, 232)
grey91 = (232, 232, 232)
gray92 = (235, 235, 235)
grey92 = (235, 235, 235)
gray93 = (237, 237, 237)
grey93 = (237, 237, 237)
gray94 = (240, 240, 240)
grey94 = (240, 240, 240)
gray95 = (242, 242, 242)
grey95 = (242, 242, 242)
gray96 = (245, 245, 245)
grey96 = (245, 245, 245)
gray97 = (247, 247, 247)
grey97 = (247, 247, 247)
gray98 = (250, 250, 250)
grey98 = (250, 250, 250)
gray99 = (252, 252, 252)
grey99 = (252, 252, 252)
gray100 = (255, 255, 255)
grey100 = (255, 255, 255)
dark_grey = (169, 169, 169)
darkgrey = (169, 169, 169)
dark_gray = (169, 169, 169)
darkgray = (169, 169, 169)
dark_blue = (0, 0, 139)
darkblue = (0, 0, 139)
dark_cyan = (0, 139, 139)
darkcyan = (0, 139, 139)
dark_magenta = (139, 0, 139)
darkmagenta = (139, 0, 139)
dark_red = (139, 0, 0)
darkred = (139, 0, 0)
light_green = (144, 238, 144)
lightgreen = (144, 238, 144)

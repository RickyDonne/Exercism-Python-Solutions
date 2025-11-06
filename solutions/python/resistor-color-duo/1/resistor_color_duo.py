color_map = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors):
    resistance = ""

    try:
        for color in colors:
            if len(resistance) < 2:
                resistance += str(color_map[color])
    
        return int(resistance)
    except KeyError:
        raise ValueError (f"invalid color {color}")

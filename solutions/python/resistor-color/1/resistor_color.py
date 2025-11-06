def colors()-> list:
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    
def color_code(color:str) -> int:

    for index, code in enumerate(colors()):
        if color == code:
            return index
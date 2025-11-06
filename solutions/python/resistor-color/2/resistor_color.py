def colors()-> list:
    """list the different band colors"""
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
    """look up the numerical value associated with a particular color band"""
    return colors().index(color)
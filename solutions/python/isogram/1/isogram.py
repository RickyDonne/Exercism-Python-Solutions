def is_isogram(string):
    # string = string.lower()
    # char = {ch for ch in string if ch.isalpha()}
    # non_alpha = string.count(" ")
    # non_alpha += string.count("-")

    # return len(char) + non_alpha == len(string)
    cleaned = [ch.lower() for ch in string if ch.isalpha()]
    return len(cleaned) == len(set(cleaned))
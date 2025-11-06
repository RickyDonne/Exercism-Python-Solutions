def is_valid(isbn):
    x = isbn
    x = x.replace('-', '')
    if len(x) != 10:
        return False
    total = 0
    for i, n in enumerate(x):
        if n.upper() == 'X' and i == 9:
            value = 10
        elif n.isnumeric():
            value = int(n)
        else:
            return False
        
        total += value * (10 - i)
    
    return total % 11 == 0


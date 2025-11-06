def score(x:float, y:float) -> int:
    total = x**2 + y**2
    points = [(1, 10), (25, 5), (100, 1)]
    for limit, point in points:
        if total <= limit:
            return point
    return 0
    
    '''
    inner = 1
    middle = 25
    outer = 100

    points = {'inner':10,
             'middle':5,
             'outer':1}
             
    if total <= inner:
        return points['inner']
    if total <= middle:
        return points['middle']
    if total <= outer:
        return points['outer']
    '''
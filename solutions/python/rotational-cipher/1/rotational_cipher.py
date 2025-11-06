def rotate(text, key):
    x = text
    k = key
    if k == 26 or k == 0:
        return (x)
        
    new = ''
    for ch in x:
        a = ('abcdefghijklmnopqrstuvwxyz')
        if ch.isalpha():
            if ch.isupper():
                a = a.upper()
            i = a.find(ch)
            i += k
            if i >= 26:
                i -= 26
            new += a[i]
        else:
            new += ch
    
    return(new)

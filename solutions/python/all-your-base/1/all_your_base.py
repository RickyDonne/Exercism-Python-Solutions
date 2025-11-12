def rebase(input_base, digits, output_base):
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    
    
    digits = digits[::-1]
    sum = 0
    for i, n in enumerate(digits):
        if n >= 0 and n < input_base:
            sum += n * input_base**i
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")
            break
    

    remainder = []
    q, r = 1, 0
    digits_base10 = sum

    while q > 0:
        q = digits_base10 // output_base
        r = digits_base10 % output_base

        digits_base10 = q
        remainder.append(r)

    return remainder[::-1]


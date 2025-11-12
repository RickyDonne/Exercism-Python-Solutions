def rebase(input_base, digits, output_base):
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    decimal_value = 0
    for n in digits:
        if n < 0 or n >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal_value = decimal_value * input_base + n
    
    if decimal_value == 0:
        return [0]
        
    result = []
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, output_base)
        result.append(remainder)

    return result[::-1]
    
    """
    remainder = []
    q, r = 1, 0
    digits_base10 = sum

    while q > 0:
        q = digits_base10 // output_base
        r = digits_base10 % output_base

        digits_base10 = q
        remainder.append(r)

    return remainder[::-1]
    """
    

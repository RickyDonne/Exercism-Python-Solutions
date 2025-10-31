def isprime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Check only odd numbers from 3 up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    
def classify(number:int)->str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    if isprime(number):
        return "deficient"
        
    sum = 0
    
    for i in range(1, number):
        if number % i == 0 and i != number:
            sum += i
            if sum > number:
                break

    if sum == number:
        return "perfect"

    if sum > number:
        return "abundant"

    if sum < number:
        return "deficient"

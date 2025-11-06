def is_armstrong_number(number):
    digit = str(number)
    power = len(digit)
    total = sum(int(i) ** power for i in digit)

    return number == total

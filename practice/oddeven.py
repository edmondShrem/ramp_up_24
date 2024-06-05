def oddEven (num:int):
    rem = num % 2
    if rem == 0:
        return str(num) + " is even."
    return str(num) + " is odd."
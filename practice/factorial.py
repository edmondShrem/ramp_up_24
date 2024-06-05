def iterFac(num:int):
    product = num
    while num > 1:
        num = num - 1
        product *= num
    return product

def recFac(num:int):
    if num == 1:
        return 1
    else:
        return num * recFac(num-1)


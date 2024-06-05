def number_length(num):
    length = 1
    while num >= 10:
        num = num/10
        length = length + 1
    return length

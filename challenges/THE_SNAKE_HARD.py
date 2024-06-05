def snakefill(n:int):
    squares = n**2
    snek = 1
    eats = 0
    while snek * 2 <= squares:
        snek *= 2
        eats += 1
    return eats


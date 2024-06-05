def interview(l:list, time:int):
    if time > 120:
        return "disqualified"
    if len(l) != 8:
        return "disqualified"
    for i, t in enumerate(l):
        if i <= 1:
            if t > 5:
                return "disqualified"
        elif i <= 3:
            if t > 10:
                return "disqualified"
        elif i <= 5:
            if t > 15:
                return "disqualified"
        elif i <= 7:
            if t > 20:
                return "disqualified"
    return "qualified"

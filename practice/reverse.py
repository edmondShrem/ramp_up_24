def reverse(s:str):
    text = s[::-1]
    vowels = 0
    for c in s:
        if isVowel(c):
            vowels += 1
    return {"reversed":text, "vowel count":vowels}

def isVowel(c:chr):
    return (str(c) == 'a' or str(c) == 'A'
            or str(c) == 'e' or str(c) == 'E'
            or str(c) == 'i' or str(c) == 'I'
            or str(c) == 'o' or str(c) == 'O'
            or str(c) == 'u'or str(c) == 'U')

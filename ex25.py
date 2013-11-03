def bw(stuff):
    words = stuff.split(' ')
    return words

def sw(words):
    return sorted(words)

def pfw(words):
    word = words.pop(0)
    print word

def plw(words):
    word = words.pop(-1)
    print word

def ss(sentence):
    words = bw(sentence)
    return sw(words)

def pfal(sentence):
    words = bw(sentence)
    pfw(words)
    plw(words)

def pfals(sentence):
    words = ss(sentence)
    pfw(words)
    plw(words)


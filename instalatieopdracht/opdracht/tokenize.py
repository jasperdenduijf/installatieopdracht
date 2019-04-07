def tokenize(string):
    returnlist =list()
    f = open(string)
    b = "!,.():"
    for word in f.read().split():
        for char in b:
            word = word.replace(char,"").lower()
        returnlist.append(word)
    return returnlist
        

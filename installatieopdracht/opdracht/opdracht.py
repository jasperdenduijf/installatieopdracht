from tokenize import tokenize

wordlist = tokenize('notulen.txt')

for word in wordlist:
    if word == "de":
        print("Hoera!")
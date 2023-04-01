def cezar(wiadomosc, klucz, alfabet="abcdefghijklmnopqrstuvwxyz"):
    wiadomosc=wiadomosc.lower()
    litery = ''
    for i in wiadomosc:
        if i in alfabet:
            litery+=i
    
    zaszyfrowana = ''
    for i in litery:
        index = alfabet.index(i)
        zaszyfrowana+= alfabet[(index+klucz)%len(alfabet)]
    index = 0
    wynik = ''
    for i in wiadomosc:
        if i in alfabet:
            wynik+=zaszyfrowana[index]
            index+=1
        else:
            wynik+=i
    return wynik

print(cezar("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll",5))
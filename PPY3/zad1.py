liczby = input("podaj liczby po przecinku: ")
tablica = liczby.split(',')
najmniejsza = int(tablica[0])
najwieksza = int(tablica[0])
for tab in tablica:
    if(int(tab)<najmniejsza): najmniejsza = int(tab)
    if(int(tab)>najwieksza): najwieksza = int(tab)
print("Najmniejsza: "+str(najmniejsza)+"\nNajwieszka: "+str(najwieksza))
import random

lista_miast = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań","Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok","Słupsk","Gdynia","Zambrów"]
wynik = []
ilosc_miast = len(lista_miast)
for x in range(ilosc_miast,0,-1):
    losowa = random.randint(0,ilosc_miast-1)
    losowe_miasto = lista_miast[losowa]
    ilosc_miast-=1
    wynik.append(losowe_miasto)
    lista_miast.remove(losowe_miasto)

wynik.sort()

for x in wynik:
    print(x)


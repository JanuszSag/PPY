import random

lista_miast = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań","Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok","Słupsk","Gdynia","Zambrów"]
wynik = []
for x in range(10):
    losowa = random.randint(0,len(lista_miast)-1)
    wynik.append(lista_miast[losowa])
    lista_miast.remove(lista_miast[losowa])

wynik.sort()

for x in wynik:
    print(x)
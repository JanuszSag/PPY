#pierwsze
print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("A) oglądanie telewizji/filmów/seriali")
print("B) czytanie książek/czasopism")
print("C) słuchanie muzyki")
odpowiedz = input("Podaj odpowiedz: ")
match odpowiedz:
    case "A":
        print("Twoja odpowiedz to oglądanie telewizji/filmów/seriali")
    case "B":
        print("Twoja odpowiedz to czytanie książek/czasopism")
    case "C":
        print("Twoja odpowiedz to słuchanie muzyki")
    case _:
        print("twoja odpowiedz jest bledna")
#drugie
print("W jakich okolicznościach czytasz książki najczęściej?")
print("A) podczas podróży")
print("B) w czasie wolnym (po pracy, na urlopie)")
print("C) podczas pracy/nauki (to ich element)")
odpowiedz = input("Podaj odpowiedz: ")
match odpowiedz:
    case "A":
        print("Twoja odpowiedz to podczas podróży")
    case "B":
        print("Twoja odpowiedz to w czasie wolnym (po pracy, na urlopie)")
    case "C":
        print("Twoja odpowiedz to podczas pracy/nauki (to ich element)")
    case _:
        print("twoja odpowiedz jest bledna")
#trzecie
print("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print("A) chęć poszerzenia wiedzy")
print("B) czytanie mnie relaksuje/odpręża")
print("C) fakt, że czytanie jest modne")
odpowiedz = input("Podaj odpowiedz: ")
match odpowiedz:
    case "A":
        print("Twoja odpowiedz to chęć poszerzenia wiedzy")
    case "B":
        print("Twoja odpowiedz to czytanie mnie relaksuje/odpręża")
    case "C":
        print("Twoja odpowiedz to fakt, że czytanie jest modne")
    case _:
        print("twoja odpowiedz jest bledna")
#czwarte
print("Po książki w jakiej formie sięgasz najczęściej? ")
print("A) papierowej (tradycyjnej)")
print("B) e-booki (książki elektroniczne) na komputerze")
print("C) e-booki na tablecie/telefonie")
odpowiedz = input("Podaj odpowiedz: ")
match odpowiedz:
    case "A":
        print("Twoja odpowiedz to papierowej (tradycyjnej)")
    case "B":
        print("Twoja odpowiedz to e-booki (książki elektroniczne) na komputerze")
    case "C":
        print("Twoja odpowiedz to e-booki na tablecie/telefonie")
    case _:
        print("twoja odpowiedz jest bledna")
#piate
print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("A) żadnej w całości - jedynie fragmenty")
print("B) 1")
print("C) 2 lub 3")
odpowiedz = input("Podaj odpowiedz: ")
match odpowiedz:
    case "A":
        print("Twoja odpowiedz to żadnej w całości - jedynie fragmenty")
    case "B":
        print("Twoja odpowiedz to 1")
    case "C":
        print("Twoja odpowiedz to 2 lub 3")
    case _:
        print("twoja odpowiedz jest bledna")
#szoste
print("Jak często średnio czytasz książki?:")
print("A) codziennie")
print("B) raz w miesiącu")
print("C) wcale")
odpowiedz = input("Podaj odpowiedz: ")
match odpowiedz:
    case "A":
        print("Twoja odpowiedz to codziennie")
    case "B":
        print("Twoja odpowiedz to raz w miesiącu")
    case "C":
        print("Twoja odpowiedz to wcale")
    case _:
        print("twoja odpowiedz jest bledna")
## TODO wielokrotny wybór
warunek = ""
print("Po jakie gatunki książek sięgasz najczęściej? ")
tablica =[]
while warunek != "koniec":
    print("A) kryminały/thrillery")
    print("B) romanse")
    print("C) psychologiczne")
    warunek = input("podaj litere lub napisz koniec aby zakonczyc wybor ")
    match warunek:
        case "A":
            tablica.append("kryminały/thrillery")
        case "B":
            tablica.append("romanse")
        case "C":
            tablica.append("psychologiczne")
        case _:
            print("niepoprawna odpowiedz")

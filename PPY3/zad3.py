import getpass
import random

rundy = int(input("Podaj ilosc rund: "))
czyKomputer = input("Chcesz grać z komputerem (1), czy z innym graczem (2)? ")

match int(czyKomputer):
    case 1:
        for x in range(rundy):
            gracz = input("Papier (1), Kamień (2), Nożyce (3)")
            komputer = random.randint(1,3)
            match komputer:
                case 1:
                    print("Komputer wybrał papier")
                case 2:
                    print("Komputer wybrał kamień")
                case 3:
                    print("Komputer wybrał nożyce")

            if (int(gracz) == komputer): print("Remis!")
            if (int(gracz) == 1 and komputer == 2 or int(gracz) == 2 and komputer == 3 or int(gracz) == 3 and komputer == 1): print("Wygrałaś/eś!")
            else: print("Przegrałaś/eś")

    case 2:
        for x in range(rundy):
            wynik_pierwszy = 0
            wynik_drugi = 0
            pierwszy = getpass.getpass("Gracz 1: Papier (1), Kamień (2), Nożyce (3) ")
            drugi = getpass.getpass("Gracz 2: Papier (1), Kamień (2), Nożyce (3) ")
            if (int(pierwszy) == int(drugi)): print("Remis!")
            if (int(pierwszy) == 1 and int(drugi) == 2 or int(pierwszy) == 2 and int(drugi) == 3 or int(pierwszy) == 3 and int(drugi) == 1): 
                print("Wygrywa gracz 1!")
                wynik_pierwszy+=1
            else :
                print("Wygrywa gracz 2!")
                wynik_drugi+=1
        print("Wyniki")
        print("Pierwszy gracz ma {} punktów".format(wynik_pierwszy))
        print("Drugi gracz ma {} punktów".format(wynik_drugi))
        

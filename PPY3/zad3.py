import getpass
import random

rundy = int(input("Podaj ilosc rund: "))
czyKomputer = input("Chcesz grać z komputerem (1), czy z innym graczem (2)? ")

match int(czyKomputer):
    case 1:
        for x in range(rundy):
            gracz = input("Papier (1), Kamień (2), Nożyce (3)")
            komputer = random.randint(1,3)
            wybor = ["Papier","Kamien","Nożyce"]
            match komputer:
                case 1:
                    print("Komputer wybrał papier")
                case 2:
                    print("Komputer wybrał kamień")
                case 3:
                    print("Komputer wybrał nożyce")

            if (int(gracz) == 1 and komputer == 1): print("Remis!")
            if (int(gracz) == 1 and komputer == 2): print("Wygrałaś/eś!")
            if (int(gracz) == 1 and komputer == 3): print("Przegrałaś/eś")
            if (int(gracz) == 2 and komputer == 1): print("Przegrałaś/eś!")
            if (int(gracz) == 2 and komputer == 2): print("Remis!")
            if (int(gracz) == 2 and komputer == 3): print("Wygrałaś/eś")
            if (int(gracz) == 3 and komputer == 1): print("Wygrałaś/eś!")
            if (int(gracz) == 3 and komputer == 2): print("Przegrałaś/eś!")
            if (int(gracz) == 3 and komputer == 3): print("Remis")

    case 2:
        for x in range(rundy):
            pierwszy = getpass.getpass("Gracz 1: Papier (1), Kamień (2), Nożyce (3) ")
            drugi = getpass.getpass("Gracz 2: Papier (1), Kamień (2), Nożyce (3) ")
            if (int(pierwszy) == 1 and int(drugi) == 1): print("Remis!")
            if (int(pierwszy) == 1 and int(drugi) == 2): print("Wygrywa gracz 1!")
            if (int(pierwszy) == 1 and int(drugi) == 3): print("Wygrywa gracz 2!")
            if (int(pierwszy) == 2 and int(drugi) == 1): print("Wygrywa gracz 2!")
            if (int(pierwszy) == 2 and int(drugi) == 2): print("Remis!")
            if (int(pierwszy) == 2 and int(drugi) == 3): print("Wygrywa gracz 1!")
            if (int(pierwszy) == 3 and int(drugi) == 1): print("Wygrywa gracz 1!")
            if (int(pierwszy) == 3 and int(drugi) == 2): print("Wygrywa gracz 2!")
            if (int(pierwszy) == 3 and int(drugi) == 3): print("Remis")

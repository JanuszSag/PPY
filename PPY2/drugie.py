def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnozenie(a,b):
    return a*b
def dzielenie(a,b):
    return a/b

pierwsza_liczba = input("Podaj pierwsza liczbe: ")
druga_liczba = input("Podaj druga liczbe: ")
operator = input("Podaj operator: ")
match operator:
    case "+":
        dodawanie(pierwsza_liczba,druga_liczba)
    case "-":
        odejmowanie(pierwsza_liczba,druga_liczba)
    case "*":
        mnozenie(pierwsza_liczba,druga_liczba)
    case "/":
        dzielenie(pierwsza_liczba,druga_liczba)
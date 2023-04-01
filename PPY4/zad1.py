import math

def funkcja(podlogaDlugosc, podlogaSzerokosc, panelDlugosc, panelSzerokosc, opakowanie):
    podlogaPowierzchnia = podlogaDlugosc*podlogaSzerokosc*1.1
    panelPowierzchnia = panelDlugosc*panelSzerokosc
    return "Potrzeba "+ str( math.ceil((podlogaPowierzchnia/panelPowierzchnia)/opakowanie))+" paneli"


print(funkcja(4,4,0.20,1,10))
#1.
#a)
pierwszy_wyraz = drugi_wyraz = trzeci_wyraz = "Python 2023"

print(pierwszy_wyraz==drugi_wyraz and drugi_wyraz==trzeci_wyraz)
#b)
print(str(type(pierwszy_wyraz))+hex(id(pierwszy_wyraz)))
print(str(type(drugi_wyraz))+hex(id(drugi_wyraz)))
print(str(type(trzeci_wyraz))+hex(id(trzeci_wyraz)))

trzeci_wyraz = "Java 11"

print(pierwszy_wyraz==drugi_wyraz and drugi_wyraz==trzeci_wyraz)

print(str(type(pierwszy_wyraz))+hex(id(pierwszy_wyraz)))
print(str(type(drugi_wyraz))+hex(id(drugi_wyraz)))
print(str(type(trzeci_wyraz))+hex(id(trzeci_wyraz)))
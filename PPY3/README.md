# PPY3
## 1.
Napisz program, który pobierze od użytkownika liczby rozdzielone przecinkiem a następnie policzy znajdzie ich max oraz min, bez używania wbudowanych funkcji
## 2. 
Napisz program, który wyświetli plan wycieczki – wybierając losowo z listy 10 największych miast w Polsce miasta do odwiedzenia. Miast ma być 10, nie mogą się powtarzać
## 3.
Napisz grę – papier nożyce kamień.
* Gra pozwoli wybrać ilość rund.
* Pozwoli wybrać tryb gry – komputer / 2 graczy (hot seats)
* Pozwoli nazwać graczy.
* Zapamięta wynik z każdej rundy.
* Na koniec wyświetli listę wyników oraz ostateczny wynik z informacją, który gracz wygrał.
W opcji hot seats należy użyć getpass:
```python
import getpasschoice = getpass.getpass('wybór: ')
print(choice)
```
# PPY4
## 1.
Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele. Dane wejściowe to długość i szerokość podłogi. (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela oraz ilość paneli w opakowaniu.
## 2. 
Napisz funkcję sprawdzającą czy podane liczby są  liczbami pierwszymi w szybszy sposób niż wprzykładzie. Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są liczbami pierwszymi.

np.:
```python
prime(0, 1, 2, 3, 4, 5)
```
0 is not prime
1 is not prime
2 is prime number
3 is prime number
4 is not prime
5 is prime number
## 3.
Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery. 
    
Funkcja przyjmuje: 
* wiadomość – tekst do zaszyfrowania.
* klucz – liczbę o ile należy przesunąć litery w alfabecie

oraz zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. 

Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian

Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres tablicy z alfabetem oraz  problem podania klucza o dowolnej wielkości

Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego


Przykład:
```python
enc = caesar_cipher(data, 5)
```
zamieni:

The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll

na:

ymj uwtojhy lzyjsgjwl jgttp tk fqnhj’x fiajsyzwjx ns btsijwqfsi, gd qjbnx hfwwtqq

```python
enc = caesar_cipher(data, 3,["a","B"])
```

Zamieni wszystkie ,,a'' na duże ,,B'' ze względu na podany alfabet:

the project gutenberg ebook of Blice’s Bdventures in wonderlBnd, by lewis cBrroll
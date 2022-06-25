"""
Wymagania:
Napisz program, który wczytuje od użytkownika wartości
i dodaje je do listy dopóki użytkownik nie poda wartości 'nie'

Wypisz listę na ekran.
"""

lista = []
while True:
    wartosc = input('Podaj wartosc: ')
    if wartosc == 'nie':
        break
    lista.append(wartosc)

print(lista)
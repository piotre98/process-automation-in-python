"""
Wymagania:
Napisz program
pytajacy uzytkownika o litere a nastepnie
wypisujacy litery (z zakresu od a do z)
zaczynajac od a a konczac na wprowadzonej literze przez uzytkownika
zakoncz program jesli uzytkownik wpisze slowo "exit" lub "quit"
"""

from string import ascii_lowercase

while True:
    litera = input('Podaj litere: ')
    #print(ascii_lowercase)

    if litera == 'exit' or litera == 'quit':
        break

    for letter in ascii_lowercase:
        print(letter)
        if litera == letter:
            break


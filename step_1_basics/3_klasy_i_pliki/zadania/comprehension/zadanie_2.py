"""
Mając słownik inventory
Stwórz klucz "pocket" w którym będzie lsita stringów: 'seashell', 'strange berry', and 'lint'.
usuń sztylet z plecaka
dodaj 340 monet
wypisz listę wszystkich posiadanych przedmiotów
"""
inventory = {
    'coins': 723,
    'pouch': ['elixir', 'potion', 'gemstone'],
    'backpack': ['buckler', 'dagger', 'torch', 'bread loaf']
}

inventory['backpack'].remove('dagger')

items = [v for k, v in inventory.items()]
print(items)
single_items = [item for item in items if not isinstance(item, list)]
print(single_items)
nested_list = [item for item in items if isinstance(item, list)]
print(nested_list)
flat = [item for sublist in nested_list for item in sublist] #tylko dwa poziomy
print(flat)


def flatten(source_list):
    if source_list == []:
        return source_list
    if isinstance(source_list[0], list):
        return flatten(source_list[0]) + flatten(source_list[1:])
    return source_list[:1] + flatten(source_list[1:])

flatten(nested_list)

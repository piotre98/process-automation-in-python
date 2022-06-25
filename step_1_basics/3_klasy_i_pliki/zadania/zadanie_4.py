"""
Używając rekurencji napisz znajdującą największy wspólny dzielnik.
Algorytm euklidesa:
Aby obliczyć NWD(a,b), wykonujemy kolejno następujące kroki:
 -> Dzielimy z resztą liczbę a przez liczbę b
 -> jeżeli reszta jest równa 0, to NWD(a,b)=b
 -> jeżeli reszta jest różna od 0, to przypisujemy liczbie a wartość liczby b, liczbie b wartość otrzymanej reszty, a następnie wykonujemy ponownie punkt karty.
"""
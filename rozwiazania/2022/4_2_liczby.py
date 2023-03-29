def czynniki_pierwsze(liczba):
    informacje_o_liczbie = [list(), set()]
    czynniki = informacje_o_liczbie[0]
    czynniki_bez_powtorzen = informacje_o_liczbie[1]

    obecna_pierwsza = 2

    while liczba > 1:
        while liczba % obecna_pierwsza == 0:
            czynniki.append(obecna_pierwsza)
            czynniki_bez_powtorzen.add(obecna_pierwsza)
            liczba /= obecna_pierwsza

        obecna_pierwsza += 1

    return informacje_o_liczbie


# plik = open('liczby.txt', 'r')
plik = open('przyklad.txt', 'r')
liczby = plik.read().split('\n')

informacje_o_liczbach = {}

for liczba in liczby:
    if liczba == "":
        break
    informacje_o_liczbach[liczba] = czynniki_pierwsze(int(liczba))

liczba_max_czynnikow = -1
max_czynnikow = -1
liczba_max_roznych_czynnikow = -1
max_roznych_czynnikow = -1

print(informacje_o_liczbach)

for liczba, informacje_o_liczbie in informacje_o_liczbach.items():
    ile_czynnikow = len(informacje_o_liczbie[0])
    ile_roznych_czynnikow = len(informacje_o_liczbie[1])

    if ile_czynnikow > max_czynnikow:
        liczba_max_czynnikow = liczba
        max_czynnikow = ile_czynnikow

    if ile_roznych_czynnikow > max_roznych_czynnikow:
        liczba_max_roznych_czynnikow = liczba
        max_roznych_czynnikow = ile_roznych_czynnikow

print(liczba_max_czynnikow, max_czynnikow, liczba_max_roznych_czynnikow, max_roznych_czynnikow)

plik.close()

# plik = open("liczby.txt", "r")
plik = open('przyklad.txt', 'r')

liczby = plik.read().split('\n')
ile_pierwsza_ostatnia = 0
liczba_pierwsza_ostatnia = None

for liczba in liczby:
    if liczba == "":
        break
    if liczba[0] == liczba[len(liczba) - 1]:
        ile_pierwsza_ostatnia += 1

        if liczba_pierwsza_ostatnia is None:
            liczba_pierwsza_ostatnia = liczba

print(ile_pierwsza_ostatnia, liczba_pierwsza_ostatnia)

plik.close()

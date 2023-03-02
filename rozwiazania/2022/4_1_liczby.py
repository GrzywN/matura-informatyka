liczby = open("liczby.txt", "r").read().split('\n')
# liczby = open("przyklad.txt", "r").read().split('\n')
ile_pierwsza_ostatnia = 0
liczba_pierwsza_ostatnia = None

print(liczby[len(liczby) - 1])

for liczba in liczby:
    if liczba == "":
        break
    if liczba[0] == liczba[len(liczba) - 1]:
        ile_pierwsza_ostatnia += 1

        if liczba_pierwsza_ostatnia == None:
            liczba_pierwsza_ostatnia = liczba

print(ile_pierwsza_ostatnia, liczba_pierwsza_ostatnia)

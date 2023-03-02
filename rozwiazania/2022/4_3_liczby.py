def trojka(x: int, y: int, z: int) -> bool:
    return \
        z % y == 0 \
        and y % x == 0\
        and x != y\
        and y != z

def piatka(u, w, x, y, z):
    return \
        z % y == 0\
        and y % x == 0\
        and x % w == 0\
        and w % u == 0\
        and u != w\
        and w != x\
        and x != y\
        and y != z\

# print(trojka(2, 6, 12))
# print(trojka(2, 10, 12))

liczby = open("przyklad.txt", "r").read().split("\n")[:-1]

for i in range(len(liczby)):
    liczby[i] = int(liczby[i])
liczby.sort()


# Trojki

pierwszy_wsk = 0
drugi_wsk = 1
trzeci_wsk = 2
trojki = []

while True:
    x = liczby[pierwszy_wsk]
    y = liczby[drugi_wsk]
    z = liczby[trzeci_wsk]
    czy_trojka = trojka(x, y, z)

    if czy_trojka:
        trojki.append((x, y, z))

    if trzeci_wsk == len(liczby) - 2:
        drugi_wsk += 1
        trzeci_wsk = drugi_wsk + 1
    elif trzeci_wsk < len(liczby) - 1:
        trzeci_wsk += 1
    elif drugi_wsk == len(liczby) - 3:
        pierwszy_wsk += 1
        drugi_wsk = pierwszy_wsk + 1
        trzeci_wsk = drugi_wsk + 1
    elif drugi_wsk < len(liczby) - 2:
        drugi_wsk += 1
    elif pierwszy_wsk == len(liczby) - 4:
        break
    else:
        pierwszy_wsk += 1
        drugi_wsk = pierwszy_wsk + 1
        trzeci_wsk = drugi_wsk + 1

print(trojki)
# exit()

# Piatki (nie dziala prawidłowo)
pierwszy_wsk = 0
drugi_wsk = 1
trzeci_wsk = 2
czwarty_wsk = 3
piaty_wsk = 4
piatki = []

while True:
    u = liczby[pierwszy_wsk]
    w = liczby[drugi_wsk]
    x = liczby[trzeci_wsk]
    y = liczby[czwarty_wsk]
    z = liczby[piaty_wsk]

    czy_piatka = piatka(u, w, x, y, z)

    if czy_piatka:
        piatki.append((u, w, x, y, z))

    if piaty_wsk == len(liczby) - 2:
        czwarty_wsk += 1
        piaty_wsk = czwarty_wsk + 1
    elif piaty_wsk < len(liczby) - 1:
        piaty_wsk += 1
    elif czwarty_wsk == len(liczby) - 3:
        trzeci_wsk += 1
        czwarty_wsk = trzeci_wsk + 1
        piaty_wsk = czwarty_wsk + 1
    elif czwarty_wsk < len(liczby) - 2:
        czwarty_wsk += 1
    elif trzeci_wsk == len(liczby) - 4:
        drugi_wsk += 1
        trzeci_wsk = drugi_wsk + 1
        czwarty_wsk = trzeci_wsk + 1
        piaty_wsk = czwarty_wsk + 1
    elif trzeci_wsk < len(liczby) - 3:
        trzeci_wsk += 1
    elif drugi_wsk == len(liczby) - 5:
        pierwszy_wsk += 1
        drugi_wsk = pierwszy_wsk + 1
        trzeci_wsk = drugi_wsk + 1
        czwarty_wsk = trzeci_wsk + 1
        piaty_wsk = czwarty_wsk + 1
    elif drugi_wsk < len(liczby) - 4:
        drugi_wsk += 1
    elif pierwszy_wsk == len(liczby) - 6:
        break
    else:
        pierwszy_wsk += 1
        drugi_wsk = pierwszy_wsk + 1
        trzeci_wsk = drugi_wsk + 1
        czwarty_wsk = trzeci_wsk + 1
        piaty_wsk = czwarty_wsk + 1

print(piatki)

# file = open("przyklad.txt", 'r')
file = open("liczby.txt", 'r')
f = list(map(int, file))

trojki = []
czworki = []
piatki = []

for x in f:
    for y in f:
        for z in f:
            if z % y == 0 and x % y == 0 and x != y and y != z and x != z:
                trojka = sorted([x, y, z])
                trojki.append(trojka)
                x1, y1, z1 = trojka

                for u in f:
                    if u == x1 or u == y1 or u == z1:
                        continue

                    przed_x = u % x1 == 0
                    pomiedzy_x_i_y = x1 % u == 0 and u % y1 == 0
                    pomiedzy_y_i_z = y1 % u == 0 and u % z1 == 0
                    po_z = z1 == u

                    if przed_x or pomiedzy_x_i_y or pomiedzy_y_i_z or po_z:
                        czworka = sorted([x, y, z, u])
                        czworki.append(czworka)
                        x2, y2, z2, u2 = czworka

                        for w in f:
                            if w == x2 or w == y2 or w == z2 or w == u2:
                                continue

                            przed_x = w % x2 == 0
                            pomiedzy_x_i_y = x2 % w == 0 and w % y2 == 0
                            pomiedzy_y_i_z = y2 % w == 0 and w % z2 == 0
                            pomiedzy_z_i_u = z2 % w == 0 and w % u2 == 0
                            po_u = u2 % w == 0

                            if przed_x or pomiedzy_x_i_y or pomiedzy_y_i_z or pomiedzy_z_i_u or po_u:
                                piatka = sorted([x, y, z, u, w])
                                piatki.append(piatka)

# Usuwanie duplikatów i wyświetlanie
unikalne_trojki = set(frozenset(sublist) for sublist in trojki)
unikalne_czworki = set(frozenset(sublist) for sublist in czworki)
unikalne_piatki = set(frozenset(sublist) for sublist in piatki)

# for set in unikalne_trojki:
# for set in unikalne_czworki:
for set in unikalne_piatki:
    for liczba in sorted(list(set)):
        print(liczba, end=" ")
    print()

file.close()

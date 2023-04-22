liczby = []

with open('liczby.txt', 'r') as f:
    for line in f:
        line = line.strip()
        liczby.append(int(line))

roznych_liczb = len(set(liczby))
dwa_razy = 0
trzy_razy = 0

for unikalna_liczba in set(liczby):
    ile_razy_wystepuje = liczby.count(unikalna_liczba)

    if ile_razy_wystepuje == 2:
        dwa_razy += 1
    elif ile_razy_wystepuje == 3:
        trzy_razy += 1

print(roznych_liczb, dwa_razy, trzy_razy)
liczby = []

with open('liczby.txt', 'r') as f:
    for line in f:
        line = line.strip()
        liczby.append(int(line))


max_roznica = 0
max_roznica_liczba = 0

for liczba in liczby:
    odbicie = int(str(liczba)[::-1])

    roznica = abs(liczba - odbicie)

    if roznica > max_roznica:
        max_roznica = roznica
        max_roznica_liczba = liczba

print(max_roznica_liczba, max_roznica)
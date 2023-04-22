liczby = []

with open('liczby.txt', 'r') as f:
    for line in f:
        line = line.strip()
        liczby.append(int(line))

for liczba in liczby:
    odbicie = int(str(liczba)[::-1])

    if odbicie % 17 == 0:
        print(odbicie)
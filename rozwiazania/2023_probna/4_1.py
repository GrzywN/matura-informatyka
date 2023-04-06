counter = 0

with open("liczby_h.txt", "r") as f:
    for line in f:
        line = line.strip()

        if line[:2] == line[-1]+line[-2]:
            counter += 1

print(counter)

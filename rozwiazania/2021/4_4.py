DOPISZ = "DOPISZ"
ZMIEN = "ZMIEN"
USUN = "USUN"
PRZESUN = "PRZESUN"

instrukcje = []

with open("instrukcje.txt", "r") as f:
    for line in f:
        instrukcje.append(line.strip("\n"))

znaki = []

for instrukcja in instrukcje:
    if instrukcja.startswith(DOPISZ):
        znaki.append(instrukcja[-1])
    elif instrukcja.startswith(ZMIEN):
        znaki.pop()
        znaki.append(instrukcja[-1])
    elif instrukcja.startswith(USUN):
        for _ in range(int(instrukcja[-1])):
            znaki.pop()
    elif instrukcja.startswith(PRZESUN):
        try:
            idx = znaki.index(instrukcja[-1])
            if znaki[idx] == 'Z':
                znaki[idx] = 'A'
            else:
                znaki[idx] = chr(ord(znaki[idx]) + 1)
        except ValueError:
            continue

print("".join(znaki))

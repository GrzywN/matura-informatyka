DOPISZ = "DOPISZ"
ZMIEN = "ZMIEN"
USUN = "USUN"
PRZESUN = "PRZESUN"

instrukcje = []
ile_instrukcji_pod_rzad = {}

with open("instrukcje.txt", "r") as f:
    for line in f:
        instrukcje.append(line.strip("\n").split(" ")[0])

obecny_ciag = instrukcje[0]
max_ile_z_rzedu = 0
ile_z_rzedu = 1
max_instrukcja = ""

for i in range(1, len(instrukcje)):
    if instrukcje[i - 1] == instrukcje[i]:
        ile_z_rzedu += 1
    else:
        max_ile_z_rzedu = max(max_ile_z_rzedu, ile_z_rzedu)
        if max_ile_z_rzedu == ile_z_rzedu:
            max_instrukcja = instrukcje[i - 1]
        ile_z_rzedu = 1

print(max_instrukcja, max_ile_z_rzedu)

DOPISZ = "DOPISZ"
ZMIEN = "ZMIEN"
USUN = "USUN"
PRZESUN = "PRZESUN"

ile_do_dopisania = 0
ile_do_usuniecia = 0

with open("instrukcje.txt", "r") as f:
    for line in f:
        if line.startswith(DOPISZ):
            ile_do_dopisania += 1
        elif line.startswith(USUN):
            ile_do_usuniecia += 1

ile_znakow = ile_do_dopisania - ile_do_usuniecia
print(ile_znakow)

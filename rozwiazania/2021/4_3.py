DOPISZ = "DOPISZ"
ZMIEN = "ZMIEN"
USUN = "USUN"
PRZESUN = "PRZESUN"

litery = {}

with open("instrukcje.txt", "r") as f:
    for line in f:
        if line.startswith(DOPISZ):
            litera = line.strip("\n").split(" ")[1]
            if litera in litery:
                litery[litera] += 1
            else:
                litery[litera] = 1

max_count_litera = ""
max_count = 0

for k, v in litery.items():
    if v > max_count:
        max_count_litera = k
        max_count = v

print(max_count_litera, max_count)

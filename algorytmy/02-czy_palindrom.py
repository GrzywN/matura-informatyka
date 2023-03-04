def czy_palindrom(tekst: str) -> bool:
    for i in range(len(tekst)):
        poczatek = i
        koniec = len(tekst) - 1 - i

        if not tekst[poczatek] == tekst[koniec]:
            return False

    return True


# Złożoność czasowa - O(n)
# Złożoność pamięciowa - O(1)

print(czy_palindrom("ala"))
print(czy_palindrom("alla"))
print(czy_palindrom("kajak"))
print(czy_palindrom("Ala ma kota"))
print(czy_palindrom("Ala"))
print(czy_palindrom("alda"))

# True
# True
# True
# False
# False
# False

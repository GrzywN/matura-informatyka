def czy_pierwsza(liczba: int) -> bool:
    if liczba < 2:
        return False

    i = 2
    while i <= liczba ** 0.5:
        if liczba % i == 0:
            return False
        i += 1

    return True


# Złożoność czasowa - O(sqrt(n))
# Złożoność pamięciowa - O(1)

print(czy_pierwsza(2))
print(czy_pierwsza(5))
print(czy_pierwsza(12))
print(czy_pierwsza(1))
print(czy_pierwsza(8))
print(czy_pierwsza(25))

# True
# True
# False
# False
# False
# False

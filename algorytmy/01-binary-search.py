def binary_search(liczby: list[int],  cel: int) -> int:
    lewo, prawo = 0, len(liczby)

    while lewo < prawo:
        srodek = (lewo + prawo) // 2

        if liczby[srodek] < cel:
            lewo = srodek + 1
        else:
            prawo = srodek

    return lewo


# Złożoność czasowa - O(log n)
# Złożoność pamięciowa - O(1)

print(binary_search([3, 4, 5, 6, 7, 8],  3))
print(binary_search([3, 4, 5, 6, 7, 8],  4))
print(binary_search([3, 4, 5, 6, 7, 8],  8))
# 0
# 1
# 5

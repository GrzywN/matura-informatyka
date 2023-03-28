def posortuj(tab: list[int], n: int) -> None:
    for i in range(n):
        for j in range(n):
            if tab[i] < tab[j]:
                tab[i], tab[j] = tab[j], tab[i]


def znajdz(tab: list[int], n: int, target: int) -> int:
    for i in range(n):
        if tab[i] == target:
            return i
    return -1


def najwieksza(tab: list[int], n: int) -> int:
    curr_max = -1
    for i in range(n):
        if curr_max < tab[i]:
            curr_max = tab[i]
    return curr_max


def ile_do_zamiany(n: int, A: list[int]) -> int:
    posortuj(A, n)
    k = 0

    for i in range(n):
        szukana_liczba = i+1
        index_szukanej_liczby = znajdz(A, n, szukana_liczba)

        if index_szukanej_liczby == -1:
            ostatnia_liczba = 0
            znaleziono_duplikat = False
            for j in range(n):
                if ostatnia_liczba == A[j]:
                    A[j] = szukana_liczba
                    posortuj(A, n)
                    znaleziono_duplikat = True
                    k += 1
                    break
                ostatnia_liczba = A[j]

            if not znaleziono_duplikat:
                max_liczba = najwieksza(A, n)
                index_liczby = znajdz(A, n, max_liczba)

                A[index_liczby] = szukana_liczba
                k += 1

    return k


print(ile_do_zamiany(3, [1, 3, 1]))
print(ile_do_zamiany(4, [1, 4, 2, 5]))
print(ile_do_zamiany(5, [2, 2, 2, 2, 2]))
print(ile_do_zamiany(4, [4, 2, 3, 1]))
print(ile_do_zamiany(6, [5, 4, 1, 5, 6, 8]))
print(ile_do_zamiany(6, [8, 4, 9, 6, 5, 7]))

# 1
# 1
# 4
# 0
# 2
# 3

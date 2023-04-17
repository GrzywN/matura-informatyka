def simple_sort(tab: list[int], n: int) -> None:
    for i in range(n):
        for j in range(n):
            if tab[i] < tab[j]:
                tmp = tab[i]
                tab[i] = tab[j]
                tab[j] = tmp

# Mniejszy (<) to rosnąco, Większy (>) malejąco.
# Złożoność czasowa - O(n^2)
# Złożoność pamięciowa - O(1)

tablica = [1, 5, 3, 2, 9]
n = len(tablica)

print(tablica)
simple_sort(tablica, 5)
print(tablica)

# Banalnie prosty niewydajny algorytm sortowania w sam raz na maturkę do części teoretycznej.
# https://youtu.be/_W0yUJlscRA

# dla i = 1..n
#   dla j = 1..n
#     jeżeli tab[i] < tab[j] wykonaj:
#       tmp <- tab[i]
#       tab[i] <- tab[j]
#       tab[j] <- tmp

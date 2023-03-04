def szukaj_w_tekscie(tekst: str, wzorzec: str) -> int:
    return tekst.find(wzorzec)


# Złożoność czasowa - O(n)
# Złożoność pamięciowa - O(1)

print(szukaj_w_tekscie("Ala ma kota", "ma "))
print(szukaj_w_tekscie("Ala ma kota", "Ala"))
print(szukaj_w_tekscie("Ala ma kota", "no nie gadaj..."))

# 4
# 0
# -1

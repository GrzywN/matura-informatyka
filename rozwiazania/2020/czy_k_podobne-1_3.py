import unittest

# Opis
# Zadanie 1. Podobne tablice
# Niech n będzie dodatnią liczbą całkowitą, a A[1..n] i B[1..n] będą n-elementowymi tablicami
# liczb całkowitych.
# Dla nieujemnej liczby całkowitej k, gdzie k < n, powiemy, że tablice A i B są k-podobne, gdy
# A[1..k] = B[n-k+1..n] oraz A[k+1..n] = B[1..n-k].
# Liczbę k nazywamy świadectwem podobieństwa.
# Uwaga: dla k = 0 przyjmujemy, że prawdziwe jest A[1..0]=B[n+1..n].
# Zadanie 1.2. (0–3)
# Zapisz w wybranej przez siebie notacji (w postaci pseudokodu, listy kroków lub w wybranym
# języku programowania) funkcję czy_k_podobne(n, A, B, k), gdzie A i B są n-elementowymi
# tablicami liczb całkowitych. Wynikiem funkcji jest PRAWDA, jeśli tablice A i B są k-podobne
# dla zadanego parametru k, natomiast FAŁSZ – w przeciwnym przypadku.
# Uwaga: w zapisie możesz wykorzystać tylko operacje arytmetyczne (dodawanie,
# odejmowanie, mnożenie, dzielenie, dzielenie całkowite, reszta z dzielenia), odwoływanie się
# do pojedynczych elementów tablicy, porównywanie liczb, instrukcje sterujące i przypisania do
# zmiennych lub samodzielnie napisane funkcje zawierające wyżej wymienione operacje.
# Specyfikacja:
# Dane:
# n – dodatnia liczba całkowita
# A[1..n], B[1..n] – n-elementowe tablice liczb całkowitych
# k – nieujemna liczba całkowita mniejsza niż n
# Wynik:
# PRAWDA, jeśli tablice A i B są k-podobne dla podanego parametru k
# FAŁSZ w przeciwnym przypadku.

# Zadanie
# Zadanie 1.2. (0–3)
# Zapisz w wybranej przez siebie notacji (w postaci pseudokodu, listy kroków lub w wybranym
# języku programowania) funkcję czy_k_podobne(n, A, B, k), gdzie A i B są n-elementowymi
# tablicami liczb całkowitych. Wynikiem funkcji jest PRAWDA, jeśli tablice A i B są k-podobne
# dla zadanego parametru k, natomiast FAŁSZ – w przeciwnym przypadku.
# Uwaga: w zapisie możesz wykorzystać tylko operacje arytmetyczne (dodawanie,
# odejmowanie, mnożenie, dzielenie, dzielenie całkowite, reszta z dzielenia), odwoływanie się
# do pojedynczych elementów tablicy, porównywanie liczb, instrukcje sterujące i przypisania do
# zmiennych lub samodzielnie napisane funkcje zawierające wyżej wymienione operacje.
# Specyfikacja:
# Dane:
# n – dodatnia liczba całkowita
# A[1..n], B[1..n] – n-elementowe tablice liczb całkowitych
# k – nieujemna liczba całkowita mniejsza niż n
# Wynik:
# PRAWDA, jeśli tablice A i B są k-podobne dla podanego parametru k
# FAŁSZ w przeciwnym przypadku.


def czy_k_podobne(n, A, B, k):
    i = 0
    j = n - k
    while i < k or j < n:
        if A[i] != B[j]:
            return False
        j += 1
        i += 1

    i = k
    j = 0
    while i < n or j < (n-k):
        if A[i] != B[j]:
            return False

        j += 1
        i += 1

    return True

# Time complexity: O(N)
# Space complexity: O(1)


def czy_podobne(n, A, B):
    i = 0
    while i < n - 1:
        if czy_k_podobne(n, A, B, i):
            return True
        i += 1
    return False

# Time complexity: O(N)
# Space complexity: O(1)


class TestujPodanePrzypadki(unittest.TestCase):

    def test_pierwszy(self):
        self.assertTrue(
            czy_podobne(3, [5, 7, 9], [5, 7, 9])
        )

    def test_drugi(self):
        self.assertTrue(
            czy_podobne(5, [4, 7, 1, 4, 5], [1, 4, 5, 4, 7])
        )

    def test_trzeci(self):
        self.assertFalse(
            czy_podobne(5, [10, 9, 12, 10, 9], [10, 10, 9, 9, 12])
        )


if __name__ == '__main__':
    unittest.main()

def dopelnienie(n: int) -> int:
    wartosc_liczby = 1
    d = 0

    while n > 0:
        cyfra = n % 10
        dopelnienie_cyfry = 9 - cyfra

        d = d + (dopelnienie_cyfry * wartosc_liczby)

        n = n // 10
        wartosc_liczby = wartosc_liczby * 10

    return d


print(dopelnienie(1000))

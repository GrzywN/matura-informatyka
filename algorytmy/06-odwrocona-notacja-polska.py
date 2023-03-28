from collections import deque


def odwrocona_notacja_polska(tablica: list[str]) -> int:
    stos = deque()
    operatory = ['+', '-', '*', '/']

    for znak in tablica:
        if znak in operatory:
            operator = znak
            drugi_operand = stos.pop()
            pierwszy_operand = stos.pop()

            wynik = int(eval(f"{pierwszy_operand}{operator}{drugi_operand}"))
            stos.append(wynik)
        else:
            stos.append(int(znak))

    wynik = stos.pop()
    return wynik

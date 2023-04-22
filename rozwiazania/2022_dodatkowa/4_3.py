def prime_factors(n):
    factors = []
    k = 2

    while n >= 0 and k <= n ** 0.5:
        while n % k == 0:
            n //= k
            factors.append(k)
        k += 1
    return factors


def is_prime(n):
    if n < 2:
        return False

    factors = prime_factors(n)
    if len(factors) == 0:
        return True

    return False


liczby = []

with open('liczby.txt', 'r') as f:
    for line in f:
        line = line.strip()
        liczby.append(int(line))

for liczba in liczby:
    odbicie = int(str(liczba)[::-1])

    if is_prime(liczba) and is_prime(odbicie):
        print(liczba)
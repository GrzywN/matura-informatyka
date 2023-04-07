def prime_factors(num: int) -> list[int]:
    k = 2
    factors = []

    while num > 1 and k <= num ** 0.5:
        while num % k == 0:
            factors.append(k)
            num //= k
        k += 1
    return factors


numbers = []
with open("liczby_h.txt", "r") as f:
    for line in f:
        line = line.strip()

        numbers.append(int(line, 16))

prime_numbers = []
for number in numbers:
    if len(prime_factors(number)) == 0:
        prime_numbers.append(number)

print(len(prime_numbers))

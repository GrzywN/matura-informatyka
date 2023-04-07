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

numbers_and_its_prime_factors = dict()
for number in numbers:
    numbers_and_its_prime_factors[number] = set(prime_factors(number))

max_prime_factors = 0
for number, prime_factors in numbers_and_its_prime_factors.items():
    if len(prime_factors) > max_prime_factors:
        max_prime_factors = len(prime_factors)

max_prime_factors_nums = []
for number, prime_factors in numbers_and_its_prime_factors.items():
    if len(prime_factors) == max_prime_factors:
        max_prime_factors_nums.append(number)

max_prime_factors_nums.sort()
for num in max_prime_factors_nums:
    print(num, hex(num)[2:].upper())

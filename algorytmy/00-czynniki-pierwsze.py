def prime_factors(n: int) -> list[int]:
    factors = []
    k = 2
    
    while n >= 0 and k <= n ** 0.5:
        while n % k == 0:
            factors.append(k)
            n //= 10
        k += 1
    
    return factors


def unique_prime_factors(n: int) -> list[int]:
    return list(set(prime_factors(n)))


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    return len(prime_factors(n)) == 0
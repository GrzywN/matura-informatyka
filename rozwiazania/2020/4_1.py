def prime_factors(num: int) -> list[int]:
    prime_factors_list = []

    k = 2
    while num >= 0 and k <= num ** 0.5:
        while num % k == 0:
            prime_factors_list.append(k)
            num //= k
        k += 1

    return prime_factors_list


def is_even(num: int) -> bool:
    return num % 2 == 0


def is_prime(num: int) -> bool:
    if num == 1:
        return False

    how_many_prime_factors = len(prime_factors(num))
    return how_many_prime_factors == 0


numbers = []
with open('pary.txt', 'r') as f:
    for line in f:
        line = line.strip()
        num, word = line.split(" ")
        numbers.append(int(num))

even_numbers = [number for number in numbers if is_even(number)]

lines = []
for number in even_numbers:
    prime_nums = [n for n in range(1, number + 1) if is_prime(n)]
    max_diff = 0
    max_diff_prime_nums_pair = []

    for i in range(len(prime_nums)):
        for j in range(len(prime_nums)):
            if prime_nums[i] + prime_nums[j] == number:
                if abs(prime_nums[i] - prime_nums[j]) >= max_diff:
                    max_diff = abs(prime_nums[i] - prime_nums[j])
                    max_diff_prime_nums_pair = sorted([prime_nums[i], prime_nums[j]])

    print(number, max_diff_prime_nums_pair[0], max_diff_prime_nums_pair[1])
    lines.append(f"{number} {max_diff_prime_nums_pair[0]} {max_diff_prime_nums_pair[1]}\n")

with open('wyniki4.txt', 'a') as f:
    f.write('\n4.1\n\n')
    f.writelines(lines)

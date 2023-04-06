numbers = []
with open("liczby_h.txt", "r") as f:
    for line in f:
        line = line.strip()
        numbers.append(int(line))

numbers_and_num_of_bits = dict()
for num in numbers:
    numbers_and_num_of_bits[num] = str(bin(num)).count('1')

max_bits = 0
for num, bits in numbers_and_num_of_bits.items():
    if bits > max_bits:
        max_bits = bits

max_bits_nums = []
for num, bits in numbers_and_num_of_bits.items():
    if bits == max_bits:
        max_bits_nums.append(num)

for num in max_bits_nums:
    print(hex(num), bin(num))

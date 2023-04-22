strings = []

with open('napisy.txt', 'r') as f:
    for line in f:
        line = line.strip()
        strings.append(line)

how_many_nums = 0
for string in strings:
    how_many_nums += string.count("0")
    how_many_nums += string.count("1")
    how_many_nums += string.count("2")
    how_many_nums += string.count("3")
    how_many_nums += string.count("4")
    how_many_nums += string.count("5")
    how_many_nums += string.count("6")
    how_many_nums += string.count("7")
    how_many_nums += string.count("8")
    how_many_nums += string.count("9")

print(how_many_nums)

strings = []

with open('napisy.txt', 'r') as f:
    for line in f:
        line = line.strip()
        strings.append(line)


strings_with_nums_only = []
for string in strings:
    current_row = []
    for character in string:
        if character == '0' or \
                character == '1' or \
                character == '2' or \
                character == '3' or \
                character == '4' or \
                character == '5' or \
                character == '6' or \
                character == '7' or \
                character == '8' or \
                character == '9':
            current_row.append(character)
    strings_with_nums_only.append(current_row)

current_numer_of_x_letters = 0
for row in strings_with_nums_only:
    row_numbers = []
    if len(row) >= 2:
        for i in range(0, len(row), 2):
            if current_numer_of_x_letters >= 3:
                break

            number = int("".join(row[i:i+2]))

            if number < 65 or number > 90:
                continue

            letter = chr(number)
            if letter == 'X':
                current_numer_of_x_letters += 1

            print(chr(number), end="")

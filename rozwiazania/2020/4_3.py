numbers_and_words = []
with open('pary.txt', 'r') as f:
    for line in f:
        line = line.strip()
        num, word = line.split(" ")
        numbers_and_words.append([int(num), str(word)])

with_len_equals_num = [[num, word] for num, word in numbers_and_words if num == len(word)]

first_element_of_sorted_output = sorted(with_len_equals_num)[0]
number, word = first_element_of_sorted_output
print(number, word)

with open('wyniki4.txt', 'a') as f:
    f.write('\n4.3\n\n')
    f.write(f"{number} {word}\n")

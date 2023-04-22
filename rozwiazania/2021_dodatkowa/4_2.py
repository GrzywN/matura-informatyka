strings = []

with open('napisy.txt', 'r') as f:
    for line in f:
        line = line.strip()
        strings.append(line)


current_letter_index = 0
secret = []
for i in range(20, len(strings) + 20, 20):
    secret.append(strings[i-1][current_letter_index])
    current_letter_index += 1

secret_str = "".join(secret)
print(secret_str)

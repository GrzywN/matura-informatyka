def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l <= r:
        if not s[l] == s[r]:
            return False
        l += 1
        r -= 1
    return True


strings = []

with open('napisy.txt', 'r') as f:
    for line in f:
        line = line.strip()
        strings.append(line)

palindromes = []
for string in strings:
    if is_palindrome(string + string[0]):
        palindromes.append(string + string[0])
    elif is_palindrome(string[-1] + string):
        palindromes.append(string[-1] + string)

middle_letters = [string[len(string) // 2] for string in palindromes]
middle_letters_str = "".join(middle_letters)

print(middle_letters_str)

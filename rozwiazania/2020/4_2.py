words = []
with open('pary.txt', 'r') as f:
    for line in f:
        line = line.strip()
        num, word = line.split(" ")
        words.append(str(word))

lines = []
for word in words:
    max_streak = 1
    max_streak_letter = word[0]
    current_streak = 1
    current_streak_letter = word[0]

    for i in range(1, len(word)):
        if word[i - 1] == word[i] and word[i] == current_streak_letter:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
                max_streak_letter = current_streak_letter
        else:
            current_streak = 1
            current_streak_letter = word[i]

    lines.append(f"{max_streak_letter * max_streak} {max_streak}\n")
    print(max_streak_letter * max_streak, max_streak)

with open('wyniki4.txt', 'a') as f:
    f.write('\n4.2\n\n')
    f.writelines(lines)

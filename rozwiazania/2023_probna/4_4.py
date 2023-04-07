numbers = []
with open("liczby_h.txt", "r") as f:
    for line in f:
        line = line.strip()
        numbers.append(int(line, 16))

max_monotonic_and_rising = 0
current_streak = 0
for i in range(1, len(numbers)):
    current_r = numbers[i - 1] - numbers[i]
    if current_r < 0:
        current_streak += 1
    else:
        if current_streak > max_monotonic_and_rising:
            max_monotonic_and_rising = current_streak
        current_streak = 0

print(max_monotonic_and_rising)

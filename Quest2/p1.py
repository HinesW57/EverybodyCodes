f = open("everybody_codes_e2024_q2_p1.txt")


first_line = f.readline()
first_line = first_line[6:]
runes = first_line.strip().split(",")
words = f.read().strip().split(" ")
print(first_line)
print(words)
total = 0
for word in words:
    for rune in runes:
        if rune in word:
            total += 1
print(total)
f.close()

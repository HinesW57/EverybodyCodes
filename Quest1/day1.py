f = open("everybody_codes_e2024_q1_p1.txt")

total = 0
for c in f.read():
    if c == "B":
        total += 1
    elif c == "C":
        total += 3

print(total)
f.close()

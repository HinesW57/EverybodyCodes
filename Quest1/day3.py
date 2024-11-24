f = open("everybody_codes_e2024_q1_p3.txt")

total = 0
string = f.read()
text = []

for i in range(0, len(string), 3):
    text.append(string[i : i + 3])

for g in text:
    cnt = g.count("x")

    for l in g:
        if l == "B":
            total += 1
        elif l == "C":
            total += 3
        elif l == "D":
            total += 5

    if cnt == 1:
        total += 2
    elif cnt == 0:
        total += 6

print(total)
f.close()

f = open("everybody_codes_e2024_q1_p2.txt")

total = 0
string = f.read()
text = []

for i in range(0, len(string), 2):
    text.append(string[i : i + 2])

for g in text:
    single = True
    if "x" not in g:
        single = False
    for l in g:
        if l == "B":
            total += 1
        elif l == "C":
            total += 3
        elif l == "D":
            total += 5
    if not single:
        total += 2

print(total)
f.close()

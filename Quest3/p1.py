with open("everybody_codes_e2024_q03_p1.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]
    print(*lines, sep="\n")
    rows = len(lines)
    cols = len(lines[0])

    # neighbors = [[0,1],[0,-1],[1,0],[-1,0]]

    level = 1
    while level < cols:
        counter = 0
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == ".":
                    lines[r][c] = 0
                elif lines[r][c] == "#":
                    lines[r][c] = 1
                    counter += 1
                elif (0 <= r - 1 < rows) and (0 <= c - 1< cols)
                    and (0 <= r + 1 < rows) and (0 <= c + 1< cols):
                    if (
                        lines[r][c] == lines[r - 1][c]
                        and lines[r][c] == lines[r][c - 1]
                        and lines[r][c] == lines[r + 1][c]
                        and lines[r][c] == lines[r][c + 1]
                    ):
                        lines[r][c] = level
        level += 1

        print("****************************************************")
        print(*lines, sep="\n")
        print(counter)

f.close()

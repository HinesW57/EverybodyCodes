with open("everybody_codes_e2024_q03_p1.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]

rows = len(lines)
cols = len(lines[0])

# convert grid to numeric heights
for r in range(rows):
    for c in range(cols):
        if lines[r][c] == ".":
            lines[r][c] = 0
        elif lines[r][c] == "#":
            lines[r][c] = 1

# directions for neighbors (N,S,E,W)
neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

total_removed = 0  # total blocks safely removed

while True:
    next_grid = [row[:] for row in lines]
    removed_this_level = 0

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] > 0:  # only consider cells with blocks
                can_dig = True

                # check all neighbors
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 < nr < rows and 0 < nc < cols:
                        if lines[nr][nc] == (lines[r][c] - 1) > 1:
                            can_dig = False
                            break

                # safely dig if possible
                if can_dig:
                    next_grid[r][c] -= 1
                    removed_this_level += 1

    if removed_this_level == 0:  # stop when no more blocks can be removed
        break

    lines = next_grid
    total_removed += removed_this_level

    # debugging output
    print(f"Level complete: Removed {removed_this_level} blocks")
    print("Grid state:")
    for row in lines:
        print("".join(str(cell) for cell in row))

print(f"Total blocks removed: {total_removed}")

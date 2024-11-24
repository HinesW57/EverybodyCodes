# f = open("everybody_codes_e2024_q2_p1.txt")


# first_line = f.readline()
# first_line = first_line[6:]
# runes = first_line.strip().split(",")

# f.close()


# Below code is helped with ChatGPT Tutoring:
def search_horizontal(runes, inscriptions):
    rows = len(inscriptions)
    cols = len(inscriptions[0])

    covered_indices = set()

    for r, row in enumerate(inscriptions):
        for rune in runes:
            pattern_length = len(rune)
            extended_row = row + row  # simulate wrap around

            # search in both direction
            for direction in [rune, rune[::-1]]:
                start = 0
                while True:
                    index = extended_row.find(direction, start)
                    if (
                        index == -1 or index >= cols
                    ):  # only count matches in the actual row
                        break

                    # add indices for the match
                    for i in range(index, index + pattern_length):
                        covered_indices.add((r, i % cols))  # use modulo for wrapping

                    start = index + 1

    return covered_indices


def search_vertical(runes, inscriptions):
    rows = len(inscriptions)
    cols = len(inscriptions[0])

    covered_indices = set()

    for c in range(cols):  # for each column
        column = get_column(inscriptions, c)
        extended_column = column

        for rune in runes:
            pattern_length = len(rune)

            # search in both direction
            for direction in [rune, rune[::-1]]:
                start = 0
                while True:
                    index = "".join(extended_column).find(direction, start)
                    if (
                        index == -1 or index >= rows
                    ):  # only count matches in the actual row
                        break

                    # add indices for the match
                    for i in range(index, index + pattern_length):
                        covered_indices.add(((i % rows), c))  # use modulo for wrapping

                    start = index + 1

    return covered_indices


def count_unique_symbols(runes, inscriptions):
    # horizontal search
    horizontal_indices = search_horizontal(runes, inscriptions)
    # print(horizontal_indices)

    # vertical search
    vertical_indices = search_vertical(runes, inscriptions)
    # print(vertical_indices)

    all_indices = horizontal_indices.union(vertical_indices)
    # print(all_indices)
    return len(all_indices)


def get_column(inscriptions, col_index):
    word = []
    for row in inscriptions:
        word.append(row[col_index])
    print("".join(word))
    return word


with open("everybody_codes_e2024_q02_p3.txt") as f:
    first_line = f.readline()
    runes = first_line[6:].strip().split(",")
    f.readline()
    inscriptions = [line.strip() for line in f.readlines()]

    print(runes)
    print(inscriptions)

    # Example input grid
    # inscriptions = ["HELWORLT", "ENIGWDXL", "TRODEOAL"]

    # Example runes
    # runes = ["THE", "OWE", "MES", "ROD", "RODEO"]

    print(count_unique_symbols(runes, inscriptions))

# f = open("everybody_codes_e2024_q2_p1.txt")


# first_line = f.readline()
# first_line = first_line[6:]
# runes = first_line.strip().split(",")

# f.close()


# Below code is helped with ChatGPT Tutoring:
def count_runes(runes, inscriptions):
    total_symbols = 0  # initialize total count

    for line in inscriptions:
        covered_indices = set()  # track indices of unique symbols covered

        for rune in runes:
            # check both the rune and it's revers
            for pattern in [rune, rune[::-1]]:
                start = 0  # start searching from the beginning of the line

                while True:
                    # find the next occurence of the pattern
                    index = line.find(pattern, start)
                    if index == -1:
                        break  # stop in no more matches are bfound

                    # Add the indices of the matched runic word to the set
                    for i in range(index, index + len(rune)):
                        covered_indices.add(i)

                    # move start index forward to prevent overlapping matches
                    start = index + 1  # move one character to check for overlaps

        # add the size of the covered indices to the toal count
        total_symbols += len(covered_indices)

    return total_symbols


with open("everybody_codes_e2024_q02_p2.txt") as f:
    first_line = f.readline()
    runes = first_line[6:].strip().split(",")

    inscriptions = [line.strip() for line in f.readlines()]

    # print(runes)
    # print(inscriptions)
    print(count_runes(runes, inscriptions))

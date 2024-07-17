with open('output/input_stobal1.txt') as file:
    line = file.readline()

    count_letter_entries = {}
    for x in set(line):
        count_letter_entries[x] = line.count(x)

    count_letter_entries = sorted(count_letter_entries,
                                  key=lambda x: count_letter_entries[x],
                                  reverse=True)

    word = ''.join(count_letter_entries[:9])
    shift = int(count_letter_entries[9])
    print(''.join([chr(ord(x) - shift) for x in word]))

with open('output/input_stobal2.txt') as file:
    line = file.readline()

    count_letter_entries = {}
    for x in set(line):
        count_letter_entries[x] = line.count(x)

    letters = sorted(count_letter_entries,
                     key=lambda x: count_letter_entries[x],
                     reverse=True)
    letters = letters[:9]

    print(''.join(
        chr(ord(letter) - count_letter_entries[letter]) for letter in letters
    ))

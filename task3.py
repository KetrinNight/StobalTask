with open('output/input_stobal3.txt') as file:
    line = file.readline()

    # Считаем количество вхождений каждого символа
    count_letter_entries = {}
    for x in set(line):
        count_letter_entries[x] = line.count(x)

    # Самое частое вхождение + дешифровка
    max_letters_entry = max(count_letter_entries.values())
    original_line = ''.join(chr(ord(letter) - max_letters_entry) for letter in line)

    # Считаем количество вхождений каждой буквы в изначальную (дешифрованную) строчку
    count_letter_entries = {}
    for x in set(original_line):
        count_letter_entries[x] = original_line.count(x)

    # Алгоритм поиска заедающей кнопки
    for index in range(len(original_line) - 1):
        current_letter, next_letter = original_line[index], original_line[index + 1]

        if current_letter != next_letter and \
                count_letter_entries[current_letter] == count_letter_entries[next_letter] and \
                original_line.count(current_letter + next_letter) == count_letter_entries[current_letter]:
            print(current_letter, next_letter)
            break

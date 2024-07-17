import random


def shuffle_string(input_line: str) -> str:
    shuffled_string = [x for x in input_line]
    random.shuffle(shuffled_string)
    return ''.join(shuffled_string)


# region Генератор для первого задания

answer = "выпускной"
shift = 9

shifted_string = ''.join(chr(ord(x) + shift) for x in answer)

result_string = shifted_string + str(shift)
result_string_in_ascii = [ord(x) for x in result_string]

result = ""
for index, repeat in enumerate([101, 99, 93, 88, 87, 82, 60, 58, 54, 50]):
    result += result_string[index] * repeat

for x in range(33, 126 + 1):
    if x in result_string_in_ascii:
        continue

    result += chr(x) * random.randint(1, 45)

with open("input_stobal1.txt", 'w') as file:
    file.write(shuffle_string(result))

# endregion

# region Генератор для второго задания

answer = "выпускной"
result_string_in_ascii = [ord(x) for x in answer]
result = ""

for index, repeat in enumerate([101, 99, 93, 88, 87, 82, 60, 58, 54]):
    input_letter = answer[index]
    encoded_letter = chr(ord(answer[index]) + repeat)
    result += chr(ord(answer[index]) + repeat) * repeat

for x in range(33, 126 + 1):
    if x in result_string_in_ascii:
        continue

    result += chr(x) * random.randint(1, 53)


with open("input_stobal2.txt", 'w') as file:
    file.write(shuffle_string(result))

# endregion

# region Генератор для третьего задания

plain_text = ""

unique_symbol = "F"
for index in range(33, 125 + 1):
    if ord(unique_symbol) == index:
        continue

    plain_text += chr(index) * random.randint(200, 300)

plain_text = shuffle_string(plain_text)
plain_text = plain_text.replace("@", "@" + unique_symbol)

count_letter_entries = {}
for x in set(plain_text):
    count_letter_entries[x] = plain_text.count(x)

with open('input_stobal3.txt', 'w') as file:
    file.write(''.join(chr(ord(x) + max(count_letter_entries.values())) for x in plain_text))

# endregion
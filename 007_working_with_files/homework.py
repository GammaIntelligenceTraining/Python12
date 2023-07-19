with open('text_files/trimushketera.txt', 'r', encoding='UTF8') as file:
    file_text = file.read()

    file_text = file_text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '')\
        .replace('"', '').replace('(', '').replace(')', '').replace('*', '')
    words = file_text.split()
    unique = list(set(words))
    unique.sort()

with open('text_files/trimushketera_result.txt', 'w', encoding='UTF8') as file:
    file.write(f'There are {len(words)} words.')
    file.write(f'\nThere are {len(unique)} unique words.')
    for word in unique:
        file.write('\n' + word)
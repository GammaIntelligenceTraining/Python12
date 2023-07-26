import re

# pattern1 = re.compile(r'#[a-fA-F0-9]{6}\b')
# sample1 = '#6655ff, #000000, #hmelee, #00998844, 23#323232'

# pattern2 = re.compile(r'(\d+)[^+]')
# sample2 = '“2*9-6*5” или (3+5)-9*4) 132231+'

# pattern3 = re.compile(r'\b([01][0-9]|2[0-3]):([0-5][0-9])\b')
# sample3 = 'Найти в тексте 123:123 время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время. [00:00 - 23:59]'

# with open('people.txt', 'r', encoding='utf8') as file:
#     sample4 = file.read()
#
#
# name_pattern = re.compile(r'([A-Z][a-z-]+ [A-Za-z-]+)\n')
# address_pattern = re.compile(r'\d{3} [0-9A-Za-z\'-]+ St\., [A-Za-z\' -]+ [A-Z]{2} \d{5}')
#
# # matches = name_pattern.finditer(sample4)
# matches = list(address_pattern.finditer(sample4))
# print(len(matches))
# # print(len(list(matches)))
# for match in matches:
#     print(match)


# pattern5 = re.compile(r'[^A-Za-z0-9]')
# sample5 = 'ASdasdasd913123 12'
#
# matches = pattern5.findall(sample5)
# if matches:
#     print('There are forbidden letters!')
# else:
#     print('There is no forbidden letters!')


pattern6 = re.compile(r'[1-8][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')
sample6 = '38803160272 99102021234 36713038965'
matches = pattern6.finditer(sample6)

for match in matches:
    print(match)

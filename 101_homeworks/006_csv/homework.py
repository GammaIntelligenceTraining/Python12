import csv


# with open('2019.csv', 'r', encoding='utf8') as file:
#     data = list(csv.reader(file))
#     data.sort(key=lambda x: x[7], reverse=True)
#
#     print(data)
# with open('2019.csv', 'r', encoding='utf8') as file:
#     data = csv.DictReader(file)
#
#     alysis_data = []
#     for line in data:
#         alysis_data.append([line['Generosity'], line['Country or region']])
#
#     alysis_data.sort(reverse=True)
#     result = []
#     for row in alysis_data:
#         if len(result) > 9:
#             break
#         result.append(row)
#
#     for line in result:
#         print(line[1], line[0])
# with open('2019.csv') as file:
#     data = csv.reader(file)
#     next(data)
#     data = list(data)
#
#     analysis_data = []
#     for row in data:
#         analysis_data.append([row[7], row[1]])
#
#     analysis_data.sort(reverse=True)
#     result = []
#     for row in analysis_data:
#         if len(result) > 9:
#             break
#         result.append(row)
#
#     for row in result:
#         print(row[1], row[0])


# x = [1, 2, 3, 4, 5, 6]
#
# y = map(, x)
# for line in y:
#     print(line)

a = lambda: print('Hello world!')
a()
import csv

# with open('csv_files/test.csv', 'r', encoding='UTF8') as file:
#     csv_reader = csv.reader(file)
#     headers = next(csv_reader)
#     csv_reader = list(csv_reader)
#
#
#     for line in csv_reader:
#         print('Name: ' + line[0])
#         print('DOB: ' + line[1])
#         print('Town: ' + line[2])
#
#     print(csv_reader)
# # normal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # normal_iterator = iter(normal)

# with open('csv_files/test.csv', 'r', encoding='UTF8') as file:
#     csv_reader = csv.reader(file)
#
#     with open('csv_files/test_copy.csv', 'w', encoding='UTF8') as wfile:
#         csv_writer = csv.writer(wfile, lineterminator='\n', delimiter='.', quotechar='*', quoting=csv.QUOTE_ALL)
#
#         # data = [['Name', 'Surname'], ['Jack', 'Smith'], ['Mary', 'Gold']]
#         for line in csv_reader:
#             csv_writer.writerow(line)


# with open('csv_files/test_copy.csv', 'r', encoding='UTF8') as test:
#     data = csv.reader(test, delimiter='*')
#
#     for line in data:
#         print(line)


with open('csv_files/test.csv', 'r', encoding='UTF8') as file:
    csv_data = csv.DictReader(file)

    with open('csv_files/test_copy.csv', 'w', encoding='UTF8') as wfile:
        fieldnames = ['Name', 'Date of birth', 'Town']

        csv_writer = csv.DictWriter(wfile, fieldnames=fieldnames, lineterminator='\n')

        csv_writer.writeheader()
        for line in csv_data:
            csv_writer.writerow(line)
# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

# with open('text_files/python.jpg', 'rb') as file:
#     data = file.read(10000)
#
#     with open('sample.jpg', 'wb') as wfile:
#
#
#         wfile.write(data)

with open('sample_text.txt', 'r') as file:
    file_data = file.read(100)
    print(file_data)
    file.seek(0)
    file_data = file.read(100)
    print(file_data)
    # file_content = file.read()
    # print(file_content)
    # print(type(file_content))
    # file_content2 = file.read()
    # print(file_content2)

    # file_content = file.readlines()
    # print(file_content)
    # print(len(file_content))

    # file_content = file.readline()
    # while len(file_content) > 0:
    #     print(file_content.upper())
    #     file_content = file.readline()

    # file.write('Hello!')
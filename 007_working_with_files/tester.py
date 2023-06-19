a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


ni = 0
for i in range(len(a)):
    while True:
        if i == ni:
            break
        else:
            ni += 1
            continue
    ni = 0

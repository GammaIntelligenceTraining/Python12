# idcode = '38803160272'
# try:
#     int(idcode)
# except ValueError:
#     print('Code is not numeric!')
# except:
#     print('NOK')
# else:
#     print(idcode)
# finally:
#     print('Good bye!')


while True:
    a = input('Enter side a: ')
    b = input('Enter side b: ')
    try:
        a = float(a)
        b = float(b)
    except:
        print('Need to enter numbers')
    else:
        print(a * b)
        break
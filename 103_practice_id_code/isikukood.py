# for x in range(10):
#     if x == 5:
#         continue
#     elif x == 7:
#         break
#     print(x)
#
# print('Good Bye')

while True:
    idcode = input('Please enter ID or type "exit": ')

    if idcode.lower() == 'exit':
        print('Good bye!')
        quit()
    else:
        if len(idcode) != 11:
            if len(idcode) > 11:
                print('Code is too long')
            else:
                print('Code is too short')
            continue
        else:
            while True:
                user_menu = input('Please select:\n'
                                  '1.Gender\n'
                                  '2.Date of birth\n'
                                  '3.Region\n'
                                  '4.Validate\n'
                                  '5.Change ID\n'
                                  '0.Exit\n'
                                  '--> ')
                if user_menu == '1':
                    if int(idcode[0]) % 2 == 0:
                        print('You are female')
                    else:
                        print('You are male')
                elif user_menu == '2':
                    if idcode[0] == '1' or idcode[0] == '2':
                        bcent = '18'
                    elif idcode[0] == '3' or idcode[0] == '4':
                        bcent = '19'
                    elif idcode[0] == '5' or idcode[0] == '6':
                        bcent = '20'
                    elif idcode[0] == '7' or idcode[0] == '8':
                        bcent = '21'
                    else:
                        bcent = None

                    if bcent is None:
                        print(f'{idcode[5:7]}.{idcode[3:5]}.{idcode[1:3]}')
                    else:
                        print(f'{idcode[5:7]}.{idcode[3:5]}.{bcent}{idcode[1:3]}')

                elif user_menu == '3':
                    if int(idcode[7:10]) in range(1, 11):
                        print('Kuressaare haigla')
                    elif int(idcode[7:10]) in range(11, 20):
                        print('Tartu Ülikooli Naistekliinik')
                    elif int(idcode[7:10]) in range(21, 151):
                        print('Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
                elif user_menu == '4':
                    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                    # 38803160272

                elif user_menu == '5':
                    break
                elif user_menu == '0':
                    print('Good bye')
                    quit()
                else:
                    print('Choice is out of range!')
                    continue
print('Good bye!')
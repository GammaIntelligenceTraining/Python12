# a = 500.0
# b = 200
# print(a + 100 + a)
#
# print(a - b + 100)
#
# print((b - 200) * a)
#
# print(a / b)
# print(a // b)
#
# print(5 % 2)
#
#
# print((25 * 5) ** 2)
#
# a = 100
# a = a + 200
# print(a)
#
# print('123' * 10)
#
# print(10 / False)


# int_var = 123
# float_var = 123.123
# str_var = '1234.213'
# bool_var = True
# name = ''

# print(bool(None))
#
# name = None

# print('Hello' + ' ' + str(123) + str(True) + str(None))
# print(float(str_var) ** 2)
#
# user_age = input('Please enter your age: ')
# my_age = 58
# print(type(user_age))
# print(my_age - int(user_age))


# print(str_var, type(str_var))
# str_var = int(float(str_var))
# print(str_var, type(str_var))

# print(int_var, type(int_var))
# int_var = float(int_var)
# print(int_var, type(int_var))

# print(float_var, type(float_var))
# float_var = int(float_var)
# print(float_var, type(float_var))

side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))

half_perimeter = (side_a + side_b + side_c) / 2
print(half_perimeter)
area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5
print(area)
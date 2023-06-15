# def say_hello():
#     print('Hello world!')

# say_hello()

# def squares(number):
#     print(number ** 2)
#
#
# squares(5)
# squares(25)
# squares(125)
#
# def sqrt(number):
#     print(number ** 0.5)
#
# sqrt(144)
# letter = 100
# sqrt(letter)
#
#
#
# def square_area(a, b):
#     return a * b
#
# print(square_area(10, 20) + square_area(30, 15))
#
# def say_hi():
#     return 'Hi world!'
#
# print(say_hi())

# print('Hello', 'world', 'planet', 'people', sep='-', end='*')
# print('Hello world!')

# def print_hello_message(name, age, occupation):
#     print(f'Hi {name}!. You are {age} years old. You work as {occupation}.')
#
# people = [
#     ('Jack', 20, 'Programmer'),
#     ('Mary', 18, 'Designer'),
#     ('Sarah', 30, 'Manager'),
#     ('Bob', 35, 'Plumber')
# ]
#
# for name, age, occupation in people:
#     print_hello_message(name, age, occupation)


# def double(num):
#     return num * 2
#
#
# def triple(num):
#     return num * 3
#
#
# def odd_or_even(start, stop):
#     result = []
#     for num in range(start, stop):
#         if num % 2 == 0:
#             result.append(double(num))
#         else:
#             result.append(triple(num))
#     return result
#
# x = odd_or_even(10, 100)
# print(x)



# def sample():
#     global a, c
#     a = 50
#     b = 100
#     c += 100
#     print(a, b, c)
#
#
# a = 5
# b = 10
# c = 15
#
# sample()
# print(a, b, c)

# def many_params(b, a=1, c=0, *args, **kwargs):
#     print(b, a, c)
#     for arg in args:
#         print(arg ** 2)
#     print(kwargs)
#
# # many_params(c=30, a=10, b=20)
# many_params(10, 20, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, one=1, two=2)

# import my_functions
#
# print(my_functions.triple(10))
# print(my_functions.double(20))

# import my_functions as mf
#
# print(mf.double(10))

from my_functions import double

print(double(100))
string_sample1 = 'Hello world world'
string_sample2 = 'first leTter is loWercase. new-sentnce'
string_sample3 = '*   **extra symbols   '
german_sample = 'der fluß'

# 'world'
#  01234
#  -5-4-3-2-1

# [START:END:STEP]
# print(string_sample1[::-1])
# print(string_sample1[-5:])
# print('world'[5])

# print(len('world'))
# print('World' in string_sample1)

# print(string_sample1.upper())
# print(string_sample1)
# string_sample1 = string_sample1.upper()
# print(string_sample1)

# print(german_sample.lower())
# print(german_sample.casefold())

# print(string_sample2.capitalize())
# print(string_sample2.title())

# print(string_sample3.strip('*'))
# print(string_sample1.replace('world ', '', 1).replace(' ', '*'))

# a, b, c = '123, 456, 789'.split(', ')
# print(a, b, c)

# print(string_sample1.count('world', 7))
# print(string_sample1.find('world', 7))


a = 'th\\sa\tdfsd\nat\'s'
print(a)
print(len(a))

salary = 1000
text = '{name:}s salary is {sal:.2f}'

print(text.format(name='Jack', sal=salary))

name = 'john'
print(f'{name.title()}s salary is {salary + 200:.2f}.')

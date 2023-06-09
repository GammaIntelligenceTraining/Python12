# x = 5
#
# student = {'name': 'Jack', 'age': 18, 'courses': ['Math', 'Art', 'English'],
#            1: 'int_key', 0.2: 'float_key', x: 'variable', 'var_key': x, True: 'HELLO',
#            'one': 1, 'two': 1, 'three': 1}  # Dictionary (dict)

# print(type(student))
# print(bool(student))

# print(student)
# student['name'] = 'Bob'
# student['phone'] = '555-555-5555'
# print(student.get('address', []))
# print(student)
# if student:
#     print(student)


# sample = [['Jack', 'Smith', 18], ['Mary', 'Gold', 21], ['Simon', 'Green', 30]]
# people = []
# for person in sample:
#     some_dict = {}
#     some_dict['name'] = person[0]
#     some_dict['surname'] = person[1]
#     some_dict['age'] = person[2]
#     people.append(some_dict)

# print(people)

sample2 = {'name': 'Jack', 'surname': 'Smith'}
#
# sample2.update({'name': 'Michael', 'age': 26, 'test': {'one': 1, 'two': 2}})
# print(sample2['test']['one'])
# print(len(sample2))
#
# del sample2['name']
#
# print(sample2)
# x = sample2.pop('surname')
# print(sample2)
# print(x)

for x in sample2.values():
    print(x)

print(sample2.keys())
print(sample2.values())
print(sample2.items())

for key, value in sample2.items():
    print(key, value)
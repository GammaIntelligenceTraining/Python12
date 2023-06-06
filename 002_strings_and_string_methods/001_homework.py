# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
hero_string = example_string1[0:2] + example_string1[-2:]
print(hero_string)


# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip('*'))
print(example_string3.replace('*', ''))


# Write a code to return "Hello my name is Jack"
example_string4 = "hello my naMe is jack"
print(example_string4.capitalize().replace('jack', 'Jack'))


# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"

var1 = var1.capitalize()
var2 = var2.capitalize()
var3 = var3.lower()

print(f'{var2}, {var3} {var1}')

print(f'{var2.capitalize()}, {var3.lower()} {var1.capitalize()}')



# Write a code to return byte_string text value
# 'utf-8' 'utf-16'
byte_string = b"\316\273"
print(byte_string.decode('utf8'))




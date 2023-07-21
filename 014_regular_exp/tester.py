import re

# Sample string
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
example*com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
900-555-123
1231-123-123123123
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
абвг

wall mall hall ball tall
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk.co
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
pattern = re.compile(r'(http://|https://)?(www\.)?([\w-]+)([.\w]+)')

matches = pattern.findall(urls)

for match in matches:
    print(match)

pattern = re.compile(r'abc')

matches = pattern.search(text_to_search)
print(matches)
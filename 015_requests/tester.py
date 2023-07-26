import requests

# https://xkcd.com/353/
# 200 - success
# 300 - redirect
# 400 - client error
# 500 - server error
# https://jsonplaceholder.typicode.com/posts
# r = requests.get('https://xkcd.com/353/', timeout=3)

# r = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=3)

r = requests.get('https://imgs.xkcd.com/comics/python.png', timeout=3)
with open('python_comic.png', 'wb') as file:
    file.write(r.content)
# print(r.text)
# print(r.content)

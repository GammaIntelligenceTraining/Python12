import hashlib

password = 'hello'

print(hashlib.md5(password.encode()).hexdigest())
# 5d41402abc4b2a76b9719d911017c592

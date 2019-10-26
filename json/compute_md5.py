import hashlib

hash = hashlib.md5()
hash.update(b'123')
print(hash.hexdigest())
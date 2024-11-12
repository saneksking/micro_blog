import hashlib


class HashMaster:
    @classmethod
    def get_hash(cls, text):
        sha = hashlib.sha256(text.encode('utf-8'))
        new_hash = sha.hexdigest()
        return new_hash

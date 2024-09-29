import hashlib

def crack_hash(hash_type, hash_value, wordlist):
    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            if hash_type == 'md5':
                hashed_word = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == 'sha1':
                hashed_word = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == 'sha256':
                hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == hash_value:
                return word
    return None

# Example usage
md5_hash = "56901cf4584b7841ec3cdbe1dba23caa47a79eb1"
sha256_hash = "bcfee25a8baf6808fce5ff4e63cf21c8d114853ca7eacdcc3c210d73c58dab66"
wordlist = "wordlist.txt"

print("MD5 Hash cracked:", crack_hash('md5', md5_hash, wordlist))
print("SHA256 Hash cracked:", crack_hash('sha256', sha256_hash, wordlist))

def hash(word):
    hash = 0
    for character in word:
        hash = (hash + ord(character)) * 17 % 256
    return hash

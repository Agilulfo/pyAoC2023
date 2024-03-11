from advent.utils import input_path

def main():
    with open(input_path(__file__)) as input:
        instructions = input.readline()[:-1].split(",")

    hashes = [hash(instruction) for instruction in instructions]
    print(f"hash sum is: {sum(hashes)}")

def hash(word):
    hash = 0
    for character in word:
        hash = (hash + ord(character)) * 17 % 256
    return hash

#Read key file from text file
def read_key():
    with open('key.txt', 'r') as f:
        key = f.read()
    return key
#Read cipher file from text file
def read_cipher():
    with open('Cipher.txt', 'r') as f:
        cipher = f.read()
    return cipher
#Read input file from text file
def read_input():
    with open('input.txt', 'r') as f:
        input = f.read()
    return input

if __name__ == '__main__':
    read_key()
    read_cipher()
    read_input()

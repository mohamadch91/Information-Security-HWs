#Read key file from text file
def read_key():
    """Read key file from text file
    Returns:
        string: key to be used for encryption/decryption
    """
    with open('key.txt', 'r') as f:
        key = f.read()
    return key
#Read cipher file from text file
def read_cipher():
    """Read cipher file from text file
    Returns:
        string: cipher text to be decrypted
    """
    with open('Cipher.txt', 'r') as f:
        cipher = f.read()
    return cipher
#Read input file from text file
def read_input():
    """Read input file from text file

    Returns:
        string: input text to be encrypted
    """
    with open('input.txt', 'r') as f:
        input = f.read()
    return input

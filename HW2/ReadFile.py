#Read key file from text file
def read_key() -> str:
    """Read key file from text file
    Returns:
        string: key to be used for encryption/decryption
    """
    try:
        with open('key.txt', 'r') as f:
            key :str = f.read()
            if(key == ''):
                print("Key file is empty")
                exit()
            return key

    except FileNotFoundError:
        print("Key file not found")
        exit()
#Read cipher file from text file
def read_cipher() -> str:
    """Read cipher file from text file
    Returns:
        string: cipher text to be decrypted
    """
    try:
        with open('Cipher.txt', 'r') as f:
            cipher: str = f.read()
            if(cipher == ''):
                print("Cipher file is empty")
                exit()
        return cipher
        
    except FileNotFoundError:
        print("Cipher file not found")
        exit()
#Read input file from text file
def read_input() -> str:
    """Read input file from text file

    Returns:
        string: input text to be encrypted
    """
    try: 
        with open('input.txt', 'r') as f:
            input :str = f.read()
            if(input == ''):
                print("Input file is empty")
                exit()
        return input
    except FileNotFoundError:
        print("Input file not found")
        exit()
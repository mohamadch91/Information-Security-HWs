#Read key file from text file
class bcolors:
    FAIL = '\033[91m'
    HEADER = '\033[95m'

    ENDC = '\033[0m'

def styled_print(color: str,text: str) -> None:
    print(bcolors.HEADER+"================================="+bcolors.ENDC)

    print(bcolors.HEADER+"AES-CTR Encryption and Decryption"+bcolors.ENDC)
    print(bcolors.HEADER+"================================="+bcolors.ENDC)
    print()
    print(color+"================================="+bcolors.ENDC)
    print(color+text+bcolors.ENDC)
    print(color+"================================="+bcolors.ENDC)  


def read_key() -> str:
    """Read key file from text file
    Returns:
        string: key to be used for encryption/decryption
    """
    try:
        with open('key.txt', 'r') as f:
            key :str = f.read()
            if(key == ''):
                styled_print(bcolors.FAIL,"Key file is empty")
                exit()
            return key

    except FileNotFoundError:
        styled_print(bcolors.FAIL,"Key file not found")
        exit()
#Read cipher file from text file
def read_cipher() -> str:
    """Read cipher file from text file
    Returns:
        string: cipher text to be decrypted
    """
    try:
        with open('EncryptedCipher.txt', 'rb') as f:
            cipher: str = f.read()
            if(cipher == ''):
                styled_print(bcolors.FAIL,"cipher file is empty")
                exit()
        return cipher
        
    except FileNotFoundError:
        styled_print(bcolors.FAIL,"Cipher file not found")
        exit()
#Read input file from text file
def read_input() -> str:
    """Read input file from text file

    Returns:
        string: input text to be encrypted
    """
    try: 
        with open('plain_input.txt', 'r') as f:
            input :str = f.read()
            if(input == ''):
                styled_print(bcolors.FAIL,"Input file is empty")
                exit()
        return input
    except FileNotFoundError:
        styled_print(bcolors.FAIL,"Input file not found")
        exit()

#Write encrypted to text file
def write_encrypted(encrypted: bytes) -> bool:
    """Write encrypted to text file

    Args:
        encrypted (bytes): encrypted text
    """
    try:
        with open('EncryptedCipher.txt', 'wb') as f:
            f.write(encrypted)
        
        return True
    except:
        return False

#Write decrypted to text file
def write_decrypted(decrypted: bytes) -> None:
    """Write decrypted to text file

    Args:
        decrypted (bytes): decrypted text
    """
    try:
        with open('DecryptedInput.txt', 'wb') as f:
            f.write(decrypted)
        return True
    except:
        return False

def write_key(key: bytes) -> None:
    """Write key to text file

    Args:
        key (bytes): key to be written to text file
    """
    try:
        with open('SHA256key.txt', 'wb') as f:
            f.write(key)
        return True
    except :
        
        return False

def write_init_vector(init_vector: int) -> None:
    """Write initial vector to text file

    Args:
        init_vector (int): initial vector to be written to text file
    """
    try:
        with open('init_vector.txt', 'w') as f:
            f.write(str(init_vector))
        return True
    except:
        return False
def read_init_vector() -> str:
    """Read initial vector from text file

    Returns:
        string: initial vector to be used for decryption
    """
    try:
        with open('init_vector.txt', 'r') as f:
            init_vector: str = f.read()
            if(init_vector == ''):
                styled_print(bcolors.FAIL,"init_vector file is empty")
                exit()
        return int(init_vector)
    except FileNotFoundError:
        styled_print(bcolors.FAIL,"init_vector file not found")
        exit()
def read_256_key() -> bytes:
    """Read 256 bit key from text file

    Returns:
        string: 256 bit key to be used for decryption
    """
    try:
        with open('SHA256key.txt', 'rb') as f:
            key: str = f.read()
            if(key == ''):
                styled_print(bcolors.FAIL,"key file is empty")
                exit()
        return key
    except FileNotFoundError:
        styled_print(bcolors.FAIL,"key file not found")
        exit()

def copy_256_key() -> None:
    """Copy 256 bit key to key.txt
    """
    try:
        with open('SHA256key.txt', 'rb') as f:
            key: str = f.read()
            if(key == ''):
                styled_print(bcolors.FAIL,"key file is empty")
                exit()
        with open('SHA256key_copy.txt', 'wb') as f:
            f.write(key)
    except FileNotFoundError:
        styled_print(bcolors.FAIL,"key file not found")
        exit()
def copy_init_vector() -> None:
    """Copy initial vector to init_vector.txt
    """
    try:
        with open('init_vector.txt', 'r') as f:
            init_vector: str = f.read()
            if(init_vector == ''):
                styled_print(bcolors.FAIL,"init_vector file is empty")
                exit()
        with open('init_vector_copy.txt', 'w') as f:
            f.write(init_vector)
    except FileNotFoundError:
        styled_print(bcolors.FAIL,"init_vector file not found")
        exit()
from typing import List
from dataclasses import dataclass,field
from os import urandom
from handleFile import *
import pbkdf2
import binascii
import secrets
import pyaes
@dataclass
class AES_CTR:
    """AES_CTR class for encrypting and decrypting files using AES in counter mode
    Attributes:
        key: key for AES encryption
        init_vector: initial vector for AES encryption
    """
    key: str = read_key()
    initial_vector :  list = field(default_factory=list) 
    def create_salt(self) -> bytes:
        """Create a random salt for the key
        Returns:
            random salt
        """
        return urandom(16)

    def convert_key_256 (self ) -> None:
        """Convert the key to 256 bits
        """
        salt : bytes = self.create_salt()
        self.key = pbkdf2.PBKDF2(self.key, salt).read(32)
    def show_key_hex(self) -> None:
        """Show the key in hex
        """
        print(f'Algorithm key is : {binascii.hexlify(self.key)}')
    def set_key(self, key: str) -> None:
        """Set the key for AES encryption
        Args:
            key (str): key for AES encryption
        """
        self.key = key
    def write_key(self) -> None:
        """Write key to text file
        """
        if(write_key(self.key)):
            print("Key written to file")
        else:
            print("Error writing key to file")
    def create_init_vector(self) -> None:
        """Create a random initial vector for AES encryption
        """
        self.initial_vector = secrets.randbits(256)
    def write_init_vector(self) -> None:
        """Write initial vector to text file
        """
        if(write_init_vector(self.initial_vector)):
            print("Initial vector written to file")
        else:
            print("Error writing initial vector to file")
    def set_init_vector(self, init_vector: str) -> None:
        """Set the initial vector for AES encryption
        Args:
            init_vector (str): initial vector for AES encryption
        """
        self.initial_vector = init_vector
    def read_256_key(self) -> None:
        """Read key from text file
        """
        self.key = read_256_key()
    def read_init_vector(self) -> None:
        """Read initial vector from text file
        """
        self.initial_vector = read_init_vector()
    def encrypt_initalize(self) -> None:
        """Initialize the encryption
        """
        self.convert_key_256()
        self.show_key_hex()
        self.write_key()
        self.create_init_vector()
        self.write_init_vector()
    def decrypt_initalize(self) -> None:
        """Initialize the decryption
        """
        self.read_256_key()
        self.show_key_hex()
        self.read_init_vector()

class Encrypt(AES_CTR):
    """Encrypt class for encrypt
    Attributes:
        key: key for AES encryption
        init_vector: initial vector for AES encryption
        plaintext: plaintext for AES encryption
        aes: pyaes object for AES encryption
    """
    def __init__(self) -> None:
        """Initialize Encrypt class
        """
        super().__init__()
        super().encrypt_initalize()
        self.aes :object = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.initial_vector))
        self.plaintext : str = read_input()
    def encrypt(self) -> str:
        """Encrypt the plaintext
        Returns:
            encrypted string
        """
        return self.aes.encrypt(self.plaintext)
    def write_cipher(self, cipher: bytes) -> None:
        """Write cipher to text file
        Args:
            cipher (bytes): encrypted string
        """
        if(write_encrypted(cipher)):
            print("Cipher written to file")
        else:
            print("Error writing cipher to file")
    def show_cipher_hex(self, cipher: bytes) -> None:
        """Show the cipher in hex
        Args:
            cipher (bytes): encrypted string
        """
        print(f'Encrypted cipher is : {binascii.hexlify(cipher)}')
    def encrypt_file(self) -> None:
        """Encrypt the file
        """
        cipher = self.encrypt()
        self.show_cipher_hex(cipher)
        self.write_cipher(cipher)
    
class Decrypt(AES_CTR):
    """Decrypt class for decrypt
    Attributes:
        key: key for AES decryption
        init_vector: initial vector for AES decryption
        ciphertext: ciphertext for AES decryption
        aes: pyaes object for AES decryption
    """
    def __init__(self) -> None:
        """Initialize Decrypt class
        """
        super().__init__()
        super().decrypt_initalize()
        self.aes : object = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.initial_vector))
        self.ciphertext : str = read_cipher()
    def decrypt(self) -> str:
        """Decrypt the ciphertext
        Returns:
            decrypted string
        """
        return self.aes.decrypt(self.ciphertext)
    def write_decrypted(self, decrypted: str) -> None:
        """Write decrypted to text file
        Args:
            decrypted (str): decrypted string
        """
        if(write_decrypted(decrypted)):
            print("Decrypted written to file")
        else:
            print("Error writing decrypted to file")
    def show_decrypted_hex(self, decrypted: str) -> None:
        """Show the decrypted in hex
        Args:
            decrypted (str): decrypted string
        """
        print(f'Decrypted cipher is : {binascii.hexlify(decrypted)}')
    def decrypt_file(self) -> None:
        """Decrypt the file
        """
        decrypted = self.decrypt()
        self.show_decrypted_hex(decrypted)
        self.write_decrypted(decrypted)
    
def get_inputs() -> list:
    print("1. Encrypt : ")
    print("2. Decrypt : ")
    print("3. Exit : ")
    inputs = input("Enter your choice : ")
    return inputs

def handle_inputs(inputs: list) -> None:
    if(inputs == "1"):
        print("Are you sure you want to encrypt the file after encrypt keys are resseted? (y/n)")
        choice = input("Enter your choice : ")
        if(choice == "y"):
            print('Do you want to copy the key and initial vector to new file? (y/n)')
            new_choice = input("Enter your choice : ")
            if(new_choice == "y"):
                copy_256_key()
                copy_init_vector()
            encrypt = Encrypt()
            encrypt.encrypt_file()
        else:
            print("Exiting")
            exit()
        
    elif(inputs == "2"):
        decrypt = Decrypt()
        decrypt.decrypt_file()
    elif(inputs == "3"):
        exit()
    else:
        print("Invalid choice")
    
def main() -> None:
    while(True):
        inputs = get_inputs()
        handle_inputs(inputs)

if __name__ == "__main__":
    main()


    

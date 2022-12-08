from typing import List
from dataclasses import dataclass,field
from os import urandom
from handleFile import *
import pbkdf2
import binascii
import secrets
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

if __name__ == "__main__":
    aes = AES_CTR()
    aes.convert_key_256()
    aes.show_key_hex()
    aes.write_key()
    aes.create_init_vector()
    aes.write_init_vector()


    

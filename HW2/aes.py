from typing import List
from dataclasses import dataclass,field
from os import urandom
from handleFile import *
import pbkdf2
import binascii
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
        return urandom(8)

    def convert_key_256 (self ) -> None:
        """Convert the key to 256 bits
        """
        salt : bytes = self.create_salt()
        self.key = pbkdf2.PBKDF2(self.key, salt).read(32)
    def show_key_hex(self) -> None:
        """Show the key in hex
        """
        print(f'Algorithm key is : {binascii.hexlify(self.key)}')


if __name__ == "__main__":
    aes = AES_CTR()
    aes.convert_key_256()
    aes.show_key_hex()


    

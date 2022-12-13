# AUT information security course HomeWorke 2

## Description

This project is a simple python CLI tool to ping encrypt and decrypt messages.

Use AES-CTR to encrypt and decrypt messages.

## Requirements

- Python 3.6 or higher
- pip3
- pyaes
- secrets
- binascii
- pbkdf2
## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 eas.py
```

## Code

[Code](./eas.py)

### Encrypt

read the message from the [plain text](./plain_input.txt) file and encrypt it and write the result to the [cipher text](./EncryptedCiphertxt) file.
write the key and the nonce to the [key](./key.txt) file.
<br/>

also write SHA-256 key to the [key](./SHA256key.txt)
and initialize vector to the [init](./init_vector.txt) file. 

### Decrypt

read cipher text from the [cipher text](./EncryptedCiphertxt) file and decrypt it and write the result to the [plain text](./DecryptedInput.txt) file.

read the key and the nonce from the [key](./SHA256key.txt) file.


## Report

[Report](./Report_9831125_MohamadChoupan.pdf)
# Python AES En(de)cryption
Python Aes Encryption tool. When called script will ask for password and keyphrase to encrypt and later decrypt the file provided. Tested and works with .txt, multiple image and video formats. In theory it should support any file format.
Generating 32 byte key from password provided. Using key stretching PBKDF2 alghorithm to prevent attacker from using pre-computed lookup tables for the key, forcing him to brute force attack. Using at least 100,000 iterations since its suggested for sha256 as of 2013.
This is just a side project for fun, no guarantees on will it behave properly so please use with caution on your files.

### Usage
```python
python encrypt.py <filename_to_encrypt>
python decrypt.py <filename_to_decrypt>
```

### Python version
Python 2.x. Python 3.x version perhaps coming later.

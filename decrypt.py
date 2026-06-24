from cryptography.fernet import Fernet
import os

'''
Key Management
'''
with open("decrypt.key", "rb") as key:
    sec_key = key.read()

'''
File Management
'''
files = []
for file in os.listdir():
    if file == "encrypt.py" or file.startswith('.') or file == "decrypt.key" or file.endswith('.md') or file == "LICENSE":
        continue
    if os.path.isfile(file):
        files.append(file)

'''
File Decryption
'''
for file in files:
    with open(file, "rb") as target_file:
        contents = target_file.read()
    decrypt_contents = Fernet(sec_key).decrypt(contents)
    with open(file, "wb") as target_file:
        target_file.write(decrypt_contents)

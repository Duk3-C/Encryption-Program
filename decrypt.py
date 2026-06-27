from cryptography.fernet import Fernet
import os

'''
Key Management
'''
with open("decrypt.key", "rb") as key:
    sec_key = key.read()

'''
File listing
'''
files = []
for file in os.listdir():
    if file == "encrypt.py" or file.startswith('.') or file == "decrypt.py" or file.endswith('.key') or file == "LICENSE" or file == "README.md" or file == "decrypt.py":
        continue
    files.append(file)

for file in files:
    with open(file, "rb") as target_file:
        contents = target_file.read()
    decrypt_contents = Fernet(sec_key).decrypt(contents)
    with open(file, "wb") as target_file:
        target_file.write(decrypt_contents)

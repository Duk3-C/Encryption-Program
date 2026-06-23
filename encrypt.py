from cryptography.fernet import Fernet
import os

'''
Key Management
'''
def create_key():
    Key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(Key)

def load_key():
    return open("key.key", "rb").read()

'''
File listing
'''
files = []
for file in os.listdir():
    if file == "encrypt.py" or file.startswith('.'):
        continue
    files.append(file)

# print(files)



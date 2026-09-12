## Minimal and functional python encryption tool
---

I made use of the *cryptography* library in python and added basic functionalities (encrypting the
files and generating a key for decryption). 

This project is merely a simple tool for learning purposes. So if you want to change and tweak
around some things, you're more than welcome to do so. 

I got the idea from a website I visited -- source is listed below:
    - https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

Build Process:
```bash
docker build -t encryption-program .

# Run with:
docker run -it encryption-program
```

Using docker you can test the program in a controlled environment.

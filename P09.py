from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_aes(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext.decode()

if __name__ == "__main__":
    key = get_random_bytes(16)  # AES-128 key
    plaintext = "Hello, AES!"

    encrypted = encrypt_aes(key, plaintext)
    decrypted = decrypt_aes(key, encrypted)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
//the pycrythe pycryptodome library installed (pip install pycryptodome). This code generates a random 128-bit AES key, encrypts the plaintext using AES in CBC mode, and then decrypts it back to the original plaintext. The pad and unpad functions are used to ensure that the plaintext is padded to the appropriate length.ptodome library installed (the pycryptodome library installed (pip install pycryptodome). This code generates a random 128-bit AES key, encrypts the plaintext using AES in CBC mode, and then decrypts it back to the original plaintext. The pad and unpad functions are used to ensure that the plaintext is 
padded to the appropriate length.pip install pycryptodome). This code generates a random 128-bit AES key, encrypts the plaintext using AES in CBC mode, and then decrypts it back to the original plaintext. The pad and unpad functions are used to ensure that the plaintext is padded to the appropriate length.//
-----------output-------------------------
Plaintext: Hello, AES!
Encrypted: b'\x93m\x89\xa9\x84\xe4\xcdY\xb1\xd4m4\xbb\x14\xfc\xdd\x1aI\x1a\xc9\xfd\x1eG\xbb&\xaf\x9a\x0b'
Decrypted: Hello, AES!

import random

# Function to calculate the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the modular inverse
def mod_inverse(e, phi):
    d = 0
    x1, x2, x3 = 0, 1, phi
    y1, y2, y3 = 1, 0, e
    while y3 != 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if x2 < 0:
        x2 += phi
    return x2

# Function to generate RSA keys
def generate_keys():
    # Choose two large prime numbers
    p = 61  # You can change these to larger prime numbers
    q = 53  # You can change these to larger prime numbers
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e (1 < e < phi) that is relatively prime to phi
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calculate the private key d
    d = mod_inverse(e, phi)

    # Public key (e, n) and private key (d, n)
    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext

# Function to decrypt a message
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr((char ** d) % n) for char in ciphertext])
    return plaintext

# Generate keys
public_key, private_key = generate_keys()
print("Public key:", public_key)
print("Private key:", private_key)

# Encrypt a message
message = "Hello, RSA!"
print("Original message:", message)
encrypted_message = encrypt(public_key, message)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)
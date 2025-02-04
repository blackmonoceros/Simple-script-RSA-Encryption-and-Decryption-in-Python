# Simple-script-RSA-Encryption-and-Decryption-in-Python
Python script that demonstrates how to implement RSA encryption and decryption. This script generates public and private keys, encrypts a message using the public key, and decrypts it using the private key.


### Detailed Explanation of the RSA Encryption Script in Python

The RSA encryption script provided earlier is a basic implementation of the RSA algorithm in Python. Below, I will explain each part of the script in detail, including its purpose and how it works.

---

#### **1. What is RSA?**
RSA (Rivest-Shamir-Adleman) is a widely used public-key cryptographic algorithm. It is based on the mathematical difficulty of factoring large composite numbers into their prime factors. RSA is used for secure data transmission and involves:
- **Public Key**: Used for encryption.
- **Private Key**: Used for decryption.

---

#### **2. Key Components of the Script**

##### **a. Generating Keys**
The function `generate_keys()` is responsible for creating the public and private keys. Here's how it works:

```python
def generate_keys():
    p = 61  # Prime number
    q = 53  # Prime number
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))
```

- **Steps**:
  1. Two prime numbers `p` and `q` are chosen. These are the foundation of RSA's security.
  2. `n` is calculated as `p * q`. This value is part of both the public and private keys.
  3. Euler's totient function `phi` is calculated as `(p - 1) * (q - 1)`.
  4. A random number `e` is chosen such that `1 < e < phi` and `gcd(e, phi) = 1`. This ensures that `e` is coprime with `phi`.
  5. The private key `d` is calculated as the modular inverse of `e` modulo `phi`.

- **Output**: The function returns:
  - Public key: `(e, n)` (used for encryption).
  - Private key: `(d, n)` (used for decryption).

---

##### **b. Encryption**
The function `encrypt(public_key, plaintext)` encrypts a plaintext message using the public key.

```python
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext
```

- **Steps**:
  1. Each character in the plaintext is converted to its ASCII value using `ord(char)`.
  2. The ASCII value is raised to the power of `e` (from the public key) and reduced modulo `n`.
  3. The resulting list of numbers represents the ciphertext.

- **Example**:
  - Plaintext: `"Hello"`
  - Encrypted: `[72^e % n, 101^e % n, ...]`

---

##### **c. Decryption**
The function `decrypt(private_key, ciphertext)` decrypts a ciphertext message using the private key.

```python
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr((char ** d) % n) for char in ciphertext])
    return plaintext
```

- **Steps**:
  1. Each number in the ciphertext is raised to the power of `d` (from the private key) and reduced modulo `n`.
  2. The resulting numbers are converted back to characters using `chr()`.
  3. The characters are joined to form the plaintext.

- **Example**:
  - Ciphertext: `[encrypted numbers]`
  - Decrypted: `"Hello"`

---

#### **3. Supporting Functions**

##### **a. Greatest Common Divisor (GCD)**
The function `gcd(a, b)` calculates the greatest common divisor of two numbers `a` and `b`. This is used to ensure that `e` is coprime with `phi`.

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

---

##### **b. Modular Inverse**
The function `mod_inverse(e, phi)` calculates the modular inverse of `e` modulo `phi`. This is used to compute the private key `d`.

```python
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
```

- **Purpose**: Finds `d` such that `(e * d) % phi = 1`. This is critical for decryption.

---

#### **4. Example Execution**

```python
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
```

- **Output**:
  - Public key: `(e, n)`
  - Private key: `(d, n)`
  - Encrypted message: A list of numbers representing the ciphertext.
  - Decrypted message: The original plaintext.

---

#### **5. Notes**
- **Security**: In real-world applications, much larger prime numbers are used to ensure security. Small primes like `61` and `53` are used here for simplicity.
- **Padding**: Practical RSA implementations use padding schemes (e.g., OAEP) to prevent certain attacks.
- **Performance**: RSA is computationally expensive, so it is often used to encrypt small pieces of data (e.g., symmetric keys) rather than large messages.


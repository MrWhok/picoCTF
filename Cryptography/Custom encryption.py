def encrypt(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = 89
    b = 27
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    # print("semi_cipher in encrypt:",semi_cipher)
    cipher = mini_encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')
    return cipher


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

def mini_encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher

################################

def decrypt(cipher, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = 89
    b = 27
    # print(f"a = {a}")
    # print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    # print(shared_key)
    semi_cipher=mini_decrypt(cipher, shared_key)
    # print("semi cipher in decrypt:",semi_cipher)
    plain_text = dynamic_xor_decrypt(semi_cipher, text_key)
    return plain_text


def mini_decrypt(ciphertext, key): #it is for getting semi_cipher
    semi_cipher =""
    for i in range(len(ciphertext)):
        temp=key*311
        semi_cipher+=chr(int((ciphertext[i]/temp)))
    return semi_cipher


def dynamic_xor_decrypt(ciphertext, text_key):
    plaintext = ""
    key_length = len(text_key)
    for i, char in enumerate(ciphertext):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += encrypted_char
    return plaintext

################################

def generator(g, x, p):
    return pow(g, x) % p

def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


# plaintext ="hello"
key="trudeau"
# ciphertext=encrypt(plaintext,key)
ciphertext=[33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]

# print(ciphertext)
plaintext=decrypt(ciphertext,key)
print(plaintext[::-1])

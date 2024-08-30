import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
print("ALPHABET:",ALPHABET)

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        print("binary:",binary)
        enc += ALPHABET[int(binary[:4], 2)]
        print("first enc:",enc)
        enc += ALPHABET[int(binary[4:], 2)]
        print("second enc:",enc)
    return enc

def binary_to_string(bits):
    return ''.join([chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)])

def b16_decode(cipher):
    dec = ""
    for i in range(0,len(cipher),2):
        temp=""
        binary="{0:04b}".format(ALPHABET.index(cipher[i]))
        temp+=binary
        binary="{0:04b}".format(ALPHABET.index(cipher[i+1]))
        temp+=binary
        dec+=binary_to_string(temp)
    return dec

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

flag = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
# key = ALPHABET

for key in ALPHABET:
    # print("key:", key)
    dec = ""
    for i, c in enumerate(flag):
        dec += shift(c, key[i % len(key)])
    # print("key:",key,dec)
    print(b16_decode(dec))
    # print("key:",key,b16_decode(dec))
    # print(enc)
    
    
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

# b16 = b16_encode(flag)
# print("b16: ",b16)
# enc = ""
# for i, c in enumerate(b16):
# 	enc += shift(c, key[i % len(key)])
# print(enc)

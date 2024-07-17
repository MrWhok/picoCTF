def decrypt(cipher):
    plaintext=""
    for i in range(1,len(cipher)+1):
        if i%3==0:
            plaintext=plaintext[:i-3]+cipher[i-1]+plaintext[i-3:]
        else:
            plaintext+=cipher[i-1]
    return plaintext

cipher="heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"
print(decrypt(cipher)) 

def decrypt(cipher,key):
    plaintext=""
    j=0
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            if j==5: j=0
            shift = ord(key[j].lower()) - ord('a')
            if cipher[i].islower():
                plaintext += chr((ord(cipher[i]) - shift - ord('a')) % 26 + ord('a'))
            elif cipher[i].isupper():
                plaintext += chr((ord(cipher[i]) - shift - ord('A')) % 26 + ord('A'))
            j+=1
        else:
            plaintext += cipher[i]
    return plaintext

key="CYLAB"
cipher="rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"
print(decrypt(cipher,key)) 

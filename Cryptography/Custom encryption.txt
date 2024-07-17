#Custom Encryption
1. Shared-key was generated if key == b_key
2. Semi-chiper was generated from dynamic_xor_encrypt function between plain-text and text-key("trudeau")
3. Cipher was generated from ecnrypt function between semi-cipher and shared-key

So, if we want to get the plain-text, we can reverse the steps from Custom Encryption

#Custom Decryption
1. We can get shared key that it used in Custom Encryption because we know the value of a and b
2. We already have cipher and shared key, so we can use the encrypt function that it used before to get semi-cipher. But we must change "cipher.append(((ord(char) * key*311)))" to        "semi_cipher+=chr(int((ciphertext[i]/temp)))"
3. Finally we can get plain-text with "dynamic_xor_encrypt" function that it used before. We use it and do xor between plain-text and text-key



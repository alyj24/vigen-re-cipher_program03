print("Problem 03 ~ Assignment 2".center(42, "="))

# pseudocode
# message: THISISTHELASTTASKHOORDAY 19 7 8 18 8 18 19 7 4 11 0 18 10 7 14 14 17 3 0 24 
# key: KNIGHTS                      10 13 8 6 7 19 18
# add: 29 20 16 24 15 37 37 7 4 11 0 18 19 19 0 18 10 7 14 14 17 3 0 24
# mod: 3 20 16 24 15 11 11 7 4 11 0 18 19 19 0 18 10 7 14 14 17 3 0 24 
# ciphertext: D U Q Y P L L H E L A S T T A S K H O O R D A Y
# define functions
def _pad_key(plaintext, key):
    padded_key = ""
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
        i += 1                      
    else:
            padded_key += ""
    return padded_key      
  
def _encrypt_decrypt_char(plaintext_char, key_char, mode= 'encrypt'):
    if plaintext_char.isalpha():
         first_alphabet_letter = 'a'
    if plaintext_char.isupper():
         first_alphabet_letter = 'A'

    old_char_position = ord(plaintext_char) - ord(first_alphabet_letter) 
    key_char_position = ord(key_char.lower()) - ord('a')  

    if mode == 'encrypt':
       new_char_position = (old_char_position + key_char_position) % 26
    else:  
       new_char_position = (old_char_position - key_char_position + 26) % 26
    return chr(new_char_position + ord(first_alphabet_letter))

def encrypt(plaintext, key):
    ciphertext = ""
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode= 'decrypt')
    return plaintext      
# ask the user for an input and save its input

plaintext_input_str = input("\033[93mGreat Day! Please enter in all uppercase letters with no spaces your input message: ")
key_input_str = input("\033[92mOne last thing, Please enter in all uppercase letters with no spaces your input key: ")

# recognize the input by the user
ciphertext = encrypt(plaintext_input_str, key_input_str)
decrypted_plaintext = decrypt(ciphertext, key_input_str)
# print the output
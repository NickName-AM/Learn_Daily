# Caesar Cipher.

letters_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_small = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
symbols = "!@\\#$%^&{}\"*()[]:;|-_=+`~'<>,./? "
LETTERS = (letters_cap + letters_small + nums + symbols)
REVERSED_LETTERS = LETTERS[::-1]

def encrypt(phrase, key):
    cipher = ''
    for letter in phrase:
        cipher += LETTERS[(LETTERS.index(letter) + key) % len(LETTERS)]
    return cipher

def decrypt(cipher, key):
    decipher = ''
    for letter in cipher:
        decipher += REVERSED_LETTERS[(REVERSED_LETTERS.index(letter) + key) % len(REVERSED_LETTERS)]
    return decipher
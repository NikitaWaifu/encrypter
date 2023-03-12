import random
import string
import numpy as np
while True:
    seed = random.randint(100, 999)
    r_seed = sum(int(digit) for digit in str(seed))
    chars = " " + string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits
    chars = list(chars)
    key = np.roll(chars, r_seed)

    print("Encrypter")
    print("[1] Encrypt")
    print("[2] Decrypt")
    x = input('Select option: ')

    try:
        x = int(x)
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        continue

    if x == 1:
        message = input('Enter your message: ')
        encrypted = ""
        for letter in message:
            index = chars.index(letter)
            encrypted += key[index]
        print()
        print(f'original message: {message}')
        print(f'encrypted message: [{encrypted}]')
        print(f'seed: {seed}')
        print()

    elif x == 2:
        decrypt_seed = input('Enter proper seed: ')
        try:
            decrypt_seed = int(decrypt_seed)
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue
        e_seed = -sum(int(digit) for digit in str(decrypt_seed))
        dkey = np.roll(chars, e_seed)
        message = input('Enter encrypted message: ')
        decrypted = ""
        for letter in message:
            index = chars.index(letter)
            decrypted += dkey[index]
        print(f'Decrypted message: {decrypted}')
        print()
    else:
        continue

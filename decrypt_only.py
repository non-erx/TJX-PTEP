#----------------------[DECRYPTION START]--------------------------
# Decryption keys for different methods
SHIFT_KEY = 5  # Shift value for custom digit shift
MOD_KEY = 7    # Modulus key for modular transformation
SCRAMBLE_ORDER = [2, 4, 1, 3, 0, 5, 7, 6, 9, 8, 11, 10, 13, 12]  # Scramble digit positions

# Custom Digit-wise Shifting (like Caesar Cipher for digits)
def custom_shift_decrypt(encrypted_number, key):
    decrypted = ''.join(str((int(digit) - key) % 10) for digit in encrypted_number)
    return decrypted
# Modular Transformation for digit scrambling
def modular_transform_decrypt(encrypted_number, key):
    decrypted = ''.join(str((int(digit) * pow(key, -1, 10)) % 10) for digit in encrypted_number)
    return decrypted
# Digit Scrambling based on a fixed pattern
def scramble_decrypt(encrypted_number, order):
    decrypted = [''] * len(encrypted_number)
    for i, pos in enumerate(order):
        decrypted[pos] = encrypted_number[i]
    return ''.join(decrypted)
# Decryption function to reverse the multi-layer encryption
def multi_decrypt(encrypted_number):
    # Reverse Scramble
    decrypted_number = scramble_decrypt(encrypted_number, SCRAMBLE_ORDER)
    # Reverse Modular Transformation
    decrypted_number = modular_transform_decrypt(decrypted_number, MOD_KEY)
    # Reverse Custom Shift
    decrypted_number = custom_shift_decrypt(decrypted_number, SHIFT_KEY)
    return decrypted_number
#----------------------[DECRYPTION END]--------------------------

def decrypt_number(encrypted_number):
    print(f"Encrypted number: {encrypted_number}\n")
    decrypted_number = multi_decrypt(encrypted_number)
    print(f"\nEncrypted Number: {encrypted_number}")
    print(f"Decrypted Number: {decrypted_number}")
encrypted_number = input("Please enter the 14-digit encrypted number: ")
decrypt_number(encrypted_number)

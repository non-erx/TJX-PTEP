#----------------------[ENCRYPTION START]--------------------------
# Encryption keys for different methods
SHIFT_KEY = 5  # Shift value for custom digit shift
MOD_KEY = 7    # Modulus key for modular transformation
SCRAMBLE_ORDER = [2, 4, 1, 3, 0, 5, 7, 6, 9, 8, 11, 10, 13, 12]  # Scramble digit positions

# Custom Digit-wise Shifting (like Caesar Cipher for digits)
def custom_shift_encrypt(number, key):
    encrypted = ''.join(str((int(digit) + key) % 10) for digit in number)
    return encrypted
def custom_shift_decrypt(encrypted_number, key):
    decrypted = ''.join(str((int(digit) - key) % 10) for digit in encrypted_number)
    return decrypted
# Modular Transformation for digit scrambling
def modular_transform_encrypt(number, key):
    encrypted = ''.join(str((int(digit) * key) % 10) for digit in number)
    return encrypted
def modular_transform_decrypt(encrypted_number, key):
    decrypted = ''.join(str((int(digit) * pow(key, -1, 10)) % 10) for digit in encrypted_number)
    return decrypted
# Digit Scrambling based on a fixed pattern
def scramble_encrypt(number, order):
    encrypted = ''.join(number[i] for i in order)
    return encrypted
def scramble_decrypt(encrypted_number, order):
    decrypted = [''] * len(encrypted_number)
    for i, pos in enumerate(order):
        decrypted[pos] = encrypted_number[i]
    return ''.join(decrypted)
# Main function to apply encryption with different methods
def multi_encrypt(number):
    # Apply Custom Shift
    encrypted_number = custom_shift_encrypt(number, SHIFT_KEY)
    # Apply Modular Transformation
    encrypted_number = modular_transform_encrypt(encrypted_number, MOD_KEY)
    # Apply Scramble (Rearrange digits according to the order)
    encrypted_number = scramble_encrypt(encrypted_number, SCRAMBLE_ORDER)
    return encrypted_number
# Decryption function to reverse the multi-layer encryption
def multi_decrypt(encrypted_number):
    # Reverse Scramble
    decrypted_number = scramble_decrypt(encrypted_number, SCRAMBLE_ORDER)
    # Reverse Modular Transformation
    decrypted_number = modular_transform_decrypt(decrypted_number, MOD_KEY)
    # Reverse Custom Shift
    decrypted_number = custom_shift_decrypt(decrypted_number, SHIFT_KEY)
    return decrypted_number
#----------------------[ENCRYPTION END]--------------------------   

def encrypt_and_decrypt(number):
    print(f"Original number: {number}\n")
    encrypted_number = multi_encrypt(number)
    decrypted_number = multi_decrypt(encrypted_number)
    print(f"\nOriginal Number: {number}")
    print(f"Encrypted Number: {encrypted_number}")
    print(f"Decrypted Number: {decrypted_number}")
    if decrypted_number == number:
        print("\nDecryption successful! The decrypted number matches the original.")
    else:
        print("\nDecryption failed! The decrypted number does not match the original.")
def get_user_input():
    while True:
        input_number = input("Please enter a 14-digit number: ")
        if len(input_number) == 14 and input_number.isdigit():
            return input_number
        else:
            print("Invalid input. Make sure it's exactly 14 digits.")
input_number = get_user_input()
encrypt_and_decrypt(input_number)

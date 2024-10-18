# Encryption keys for different methods
SHIFT_KEY = 5  # Shift value for custom digit shift
MOD_KEY = 7    # Modulus key for modular transformation
SCRAMBLE_ORDER = [2, 4, 1, 3, 0, 5, 7, 6, 9, 8, 11, 10, 13, 12]  # Scramble digit positions

# Custom Digit-wise Shifting (like Caesar Cipher for digits)
def custom_shift_encrypt(number, key):
    print("Custom Shift Encryption (Shift by {}):".format(key))
    encrypted = ''.join(str((int(digit) + key) % 10) for digit in number)
    print(f"  {number} -> {encrypted}")
    return encrypted
def custom_shift_decrypt(encrypted_number, key):
    print("Custom Shift Decryption (Shift by {}):".format(key))
    decrypted = ''.join(str((int(digit) - key) % 10) for digit in encrypted_number)
    print(f"  {encrypted_number} -> {decrypted}")
    return decrypted
# Modular Transformation for digit scrambling
def modular_transform_encrypt(number, key):
    print("Modular Transformation Encryption (Using Key {}):".format(key))
    encrypted = ''.join(str((int(digit) * key) % 10) for digit in number)
    print(f"  {number} -> {encrypted}")
    return encrypted
def modular_transform_decrypt(encrypted_number, key):
    print("Modular Transformation Decryption (Using Key {}):".format(key))
    decrypted = ''.join(str((int(digit) * pow(key, -1, 10)) % 10) for digit in encrypted_number)
    print(f"  {encrypted_number} -> {decrypted}")
    return decrypted
# Digit Scrambling based on a fixed pattern
def scramble_encrypt(number, order):
    print("Digit Scrambling Encryption (Using Order {}):".format(order))
    encrypted = ''.join(number[i] for i in order)
    print(f"  {number} -> {encrypted}")
    return encrypted
def scramble_decrypt(encrypted_number, order):
    print("Digit Scrambling Decryption (Using Order {}):".format(order))
    decrypted = [''] * len(encrypted_number)
    for i, pos in enumerate(order):
        decrypted[pos] = encrypted_number[i]
    decrypted_str = ''.join(decrypted)
    print(f"  {encrypted_number} -> {decrypted_str}")
    return decrypted_str

# Encryption with different methods
def multi_encrypt(number):
    print("\n--- Encrypting ---\n")
    # Apply Custom Shift
    encrypted_number = custom_shift_encrypt(number, SHIFT_KEY)
    # Apply Modular Transformation
    encrypted_number = modular_transform_encrypt(encrypted_number, MOD_KEY)
    # Apply Scramble (Rearrange digits according to the order)
    encrypted_number = scramble_encrypt(encrypted_number, SCRAMBLE_ORDER)
    print("\nFinal Encrypted Number:", encrypted_number)
    return encrypted_number
# Decryption function to reverse the multi-layer encryption
def multi_decrypt(encrypted_number):
    print("\n--- Decrypting ---\n")
    # Reverse Scramble
    decrypted_number = scramble_decrypt(encrypted_number, SCRAMBLE_ORDER)
    # Reverse Modular Transformation
    decrypted_number = modular_transform_decrypt(decrypted_number, MOD_KEY)
    # Reverse Custom Shift
    decrypted_number = custom_shift_decrypt(decrypted_number, SHIFT_KEY)
    print("\nFinal Decrypted Number:", decrypted_number)
    return decrypted_number
# Function to handle encryption and decryption of the input number
def encrypt_and_decrypt(number):
    print(f"Original number: {number}\n")
    # Encrypt using multiple different encryption methods
    encrypted_number = multi_encrypt(number)
    # Decrypt using the reverse steps of encryption
    decrypted_number = multi_decrypt(encrypted_number)
    # Display results
    print(f"\nOriginal Number: {number}")
    print(f"Encrypted Number: {encrypted_number}")
    print(f"Decrypted Number: {decrypted_number}")
    # Check if the decrypted number matches the original
    if decrypted_number == number:
        print("\nDecryption successful! The decrypted number matches the original.")
    else:
        print("\nDecryption failed! The decrypted number does not match the original.")
# Ask for the 14-digit input number from the user
def get_user_input():
    while True:
        input_number = input("Please enter a 14-digit number: ")
        if len(input_number) == 14 and input_number.isdigit():
            return input_number
        else:
            print("Invalid input. Make sure it's exactly 14 digits.")
input_number = get_user_input()
encrypt_and_decrypt(input_number)

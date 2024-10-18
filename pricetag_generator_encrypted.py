import random
from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter

# Encryption keys for different methods
SHIFT_KEY = 5  # Shift value for custom digit shift
MOD_KEY = 7    # Modulus key for modular transformation
SCRAMBLE_ORDER = [2, 4, 1, 3, 0, 5, 7, 6, 9, 8, 11, 10, 13, 12]  # Scramble digit positions

# Custom Digit-wise Shifting (like Caesar Cipher for digits)
def custom_shift_encrypt(number, key):
    encrypted = ''.join(str((int(digit) + key) % 10) for digit in number)
    return encrypted
# Modular Transformation for digit scrambling
def modular_transform_encrypt(number, key):
    encrypted = ''.join(str((int(digit) * key) % 10) for digit in number)
    return encrypted
# Digit Scrambling based on a fixed pattern
def scramble_encrypt(number, order):
    encrypted = ''.join(number[i] for i in order)
    return encrypted
# Encryption method for a number
def multi_encrypt(number):
    encrypted_number = custom_shift_encrypt(number, SHIFT_KEY)
    encrypted_number = modular_transform_encrypt(encrypted_number, MOD_KEY)
    encrypted_number = scramble_encrypt(encrypted_number, SCRAMBLE_ORDER)
    return encrypted_number
# Price Ticket Generation
def generate_ticket(department, style, type_code, category, month=None, comparable=None, price=None):
    department_str = f"{int(department):02}" 
    style_str = f"{int(style):06}"
    category_str = f"{int(category):04}" 
    comparable_str = f"${float(comparable):.2f}" if comparable else None
    price_str = f"${float(price):.2f}" if price else None
    price_as_int = int(float(price) * 100) if price else 0
    barcode_number = f"{department_str}{style_str}{price_as_int:06}"
    encrypted_barcode_number = multi_encrypt(barcode_number)
    template = Image.open('pricetag.png')
    draw = ImageDraw.Draw(template)
    # Fonts
    dept_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    style_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    type_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    cat_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    month_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    price_font = ImageFont.truetype("fonts/pertibd.ttf", 48)
    price_value_font = ImageFont.truetype("fonts/avramsans.ttf", 58)
    # Place text
    if month:
        draw.text((431, 329), month, font=month_font, fill=(0, 0, 0))
    if comparable_str:
        draw.text((270, 520), comparable_str, font=price_font, fill=(0, 0, 0))
    if price_str:
        draw.text((213, 589), price_str, font=price_value_font, fill=(0, 0, 0))
    barcode_image = generate_barcode(encrypted_barcode_number)
    barcode_position = (89, 680)
    template.paste(barcode_image, barcode_position)
    template.show()
    template.save(f"price_ticket_{encrypted_barcode_number}.png")
    print(f"Ticket generated: price_ticket_{encrypted_barcode_number}.png")
# Generate the barcode
def generate_barcode(barcode_number):
    barcode_obj = barcode.get_barcode_class('code128')(barcode_number, writer=ImageWriter())
    barcode_image = barcode_obj.render(writer_options={'write_text': False})
    barcode_image = barcode_image.convert("L")
    threshold = 128
    bw_barcode = barcode_image.point(lambda p: 0 if p > threshold else 128)
    new_width = int(bw_barcode.width * 1.3)
    new_height = int(bw_barcode.height / 2)
    resized_barcode = bw_barcode.resize((new_width, new_height), Image.NEAREST)
    return resized_barcode
# Generate random input
def generate_random_input():
    department = random.randint(2, 99)
    style = random.randint(100000, 999999)
    type_code = random.choice([random.randint(1, 9), random.randint(1, 9)])
    category = random.randint(1000, 9999)
    month = random.choice([None, random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']) + str(random.randint(1000, 9999))])
    comparable = round(random.uniform(10.00, 100.00), 2)
    price = round(random.uniform(10.00, 100.00), 2)
    return department, style, type_code, category, month, comparable, price
# Manually input all fields
def get_manual_input():
    department = input("Enter department (02-99): ")
    style = input("Enter style (6 digits): ")
    type_code = input("Enter type code (2 or 4 digits): ")
    category = input("Enter category (4 digits): ")
    month = input("Enter month (optional, e.g., A2023): ")
    comparable = input("Enter comparable price (e.g., 16.99): ")
    price = input("Enter price (e.g., 19.99): ")
    return department, style, type_code, category, month, comparable, price
def main():
    choice = input("Generate ticket with (1) Manual input or (2) Random input? Enter 1 or 2: ")
    if choice == '1':
        department, style, type_code, category, month, comparable, price = get_manual_input()
    elif choice == '2':
        department, style, type_code, category, month, comparable, price = generate_random_input()
        print("Randomly generated values:")
        print(f"Department: {department}, Style: {style}, Type Code: {type_code}, Category: {category}, Month: {month}, Comparable: {comparable}, Price: {price}")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return
    generate_ticket(department, style, type_code, category, month, comparable, price)
if __name__ == "__main__":
    main()

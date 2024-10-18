import random
from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter

#---------------------[ENCRYPTION START]------------------------
# Encryption keys for different methods
SHIFT_KEY = 5
MOD_KEY = 7
SCRAMBLE_ORDER = [2, 4, 1, 3, 0, 5, 7, 6, 9, 8, 11, 10, 13, 12]

# Custom Digit-wise Shifting
def custom_shift_encrypt(number, key):
    return ''.join(str((int(digit) + key) % 10) for digit in number)
# Modular Transformation
def modular_transform_encrypt(number, key):
    return ''.join(str((int(digit) * key) % 10) for digit in number)
# Digit Scrambling
def scramble_encrypt(number, order):
    return ''.join(number[i] for i in order)
# Combined Encryption
def multi_encrypt(number):
    encrypted = custom_shift_encrypt(number, SHIFT_KEY)
    encrypted = modular_transform_encrypt(encrypted, MOD_KEY)
    encrypted = scramble_encrypt(encrypted, SCRAMBLE_ORDER)
    return encrypted
#----------------------[ENCRYPTION END]--------------------------

def generate_ticket(department, style, type_code, category, month=None, comparable=None, price=None):
    department_str = f"{int(department):02}"
    style_str = f"{int(style):06}"
    category_str = f"{int(category):04}"
    comparable_str = f"${float(comparable):.2f}" if comparable else None
    price_str = f"${float(price):.2f}" if price else None
    price_as_int = round(float(price) * 100)  # Correct rounding
    barcode_number = f"{department_str}{style_str}{price_as_int:06}"
    encrypted_barcode_number = multi_encrypt(barcode_number)
    print(f"Barcode number (original): {barcode_number}")
    print(f"Encrypted barcode number: {encrypted_barcode_number}")
    template = Image.open('pricetag.png')
    draw = ImageDraw.Draw(template)
    # Fonts (ensure paths are correct)
    dept_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    style_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    type_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    cat_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    month_font = ImageFont.truetype("fonts/garamond.ttf", 36)
    price_font = ImageFont.truetype("fonts/pertibd.ttf", 48)
    price_value_font = ImageFont.truetype("fonts/avramsans.ttf", 58)
    # Place text
    draw.text((106, 163), department_str, font=dept_font, fill=(0, 0, 0))
    draw.text((262, 163), style_str, font=style_font, fill=(0, 0, 0))
    draw.text((478, 163), str(type_code), font=type_font, fill=(0, 0, 0))
    draw.text((84, 250), category_str, font=cat_font, fill=(0, 0, 0))
    if month:
        draw.text((431, 329), month, font=month_font, fill=(0, 0, 0))
    if comparable:
        draw.text((270, 520), f"${comparable:.2f}", font=price_font, fill=(0, 0, 0))
    if price:
        draw.text((213, 589), f"${price:.2f}", font=price_value_font, fill=(0, 0, 0))
    barcode_image = generate_barcode(encrypted_barcode_number)
    template.paste(barcode_image, (89, 680))
    template.show()
    template.save(f"price_ticket_{encrypted_barcode_number}.png")
def generate_barcode(barcode_number):
    barcode_obj = barcode.get_barcode_class('code128')(barcode_number, writer=ImageWriter())
    barcode_image = barcode_obj.render(writer_options={'write_text': False})
    barcode_image = barcode_image.convert("L")
    bw_barcode = barcode_image.point(lambda p: 0 if p > 128 else 128)
    resized_barcode = bw_barcode.resize((int(bw_barcode.width * 1.3), int(bw_barcode.height / 2)), Image.NEAREST)
    return resized_barcode
def generate_random_input():
    department = random.randint(2, 99)
    style = random.randint(100000, 999999)
    type_code = random.choice([random.randint(1, 9), random.randint(1, 9)])
    category = random.randint(1000, 9999)
    month = random.choice([None, random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']) + str(random.randint(1000, 9999))])
    comparable = round(random.uniform(10.00, 100.00), 2)
    price = round(random.uniform(10.00, 100.00), 2)
    return department, style, type_code, category, month, comparable, price
def get_manual_input():
    department = input("Enter department (02-99): ")
    style = input("Enter style (6 digits): ")
    type_code = input("Enter type code (2 or 4 digits): ")
    category = input("Enter category (4 digits): ")
    month = input("Enter month (optional, e.g., A2023): ")
    comparable = float(input("Enter comparable price (e.g., 16.99): "))
    price = float(input("Enter price (e.g., 19.99): "))
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

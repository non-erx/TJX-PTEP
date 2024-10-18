# TJX - PTEP (Price Ticket Encryption Project)

## Overview
The TJX - Price Ticket Encryption Project serves as an example of how to enhance the security of price tickets within retail environments, specifically addressing the issue of counterfeit price tickets. This project implements a robust encryption method for barcodes to demonstrate how unauthorized creation of price tickets with incorrect pricing can be prevented, thereby protecting both customers and the company.

## Features
- **Barcode Encryption and Decryption:** A comprehensive script that allows for both encryption and decryption of barcode data.
- **Price Ticket Generators:**
  - **Regular Price Ticket Generator:** Generates standard price tickets.
  - **Encrypted Price Ticket Generator:** Produces price tickets with encrypted barcodes to ensure authenticity.

## Methodology
The project utilizes a multi-layer encryption technique consisting of:
1. **Custom Shift Encryption:** Shifts each digit of the barcode by a specified number of positions (5 in this case).
2. **Modular Transformation Encryption:** Adds a fixed value (7) to each digit and applies a modulo operation to maintain digit integrity.
3. **Digit Scrambling Encryption:** Reorders the digits based on a predetermined sequence to add complexity.

And they all retain the size of the original barcode (14 numbers).
## Purpose
This project is designed to illustrate potential solutions for a critical yet under-recognized issue in the retail industry. It aims to provide a foundation for companies like TJX to stay ahead of potential risks related to pricing discrepancies and fraud.

## Legal and Ethical Usage
**IMPORTANT:** This project is intended for educational and illustrative purposes only. Unauthorized use of these scripts for fraudulent activities, including the creation of counterfeit price tickets, is illegal and unethical. Users are encouraged to apply the knowledge gained from this project responsibly and to seek permission before implementing similar solutions in any commercial environment.

## Installation and Usage
To run the scripts, clone the repository and ensure you have Python installed on your system.

```
git clone https://github.com/non-erx/TJX-PTEP.git
pip install -r requirements.txt
python encrypt_and_decrypt.py (for testing encryption and decryption in one script with a detailed description of actions)
python encrypt.py (for encryption testing)
python decrypt.py (for decryption testing)
pricetag_generator_encrypted.py (to generate a picture (.png) of an encrypted price ticket)
pricetag_generator_unencrypted.py (to generate a picture (.png) of an unencrypted price ticket)
```

## Example of Use and Explanation

To create this project, I began by researching the structure of a typical price ticket. For reference, I used an image sourced from **[this Reddit thread](https://www.reddit.com/media?url=https://preview.redd.it/3fb7z5dg0la31.jpg?width=1080&crop=smart&auto=webp&s=4b2edc922c81150eececa1445b33c4ec472986c5)**:

![Data](https://github.com/user-attachments/assets/33fd46f3-01b0-44fc-bd6d-f4d2d1aa04a0)

Following this, I designed my own ticket template. To identify the fonts used in the original image, I utilized **[Font Squirrel's Matcherator](https://www.fontsquirrel.com/matcherator)**. Using this template, I developed a price ticket generator:

![Unencrypted Ticket](https://github.com/user-attachments/assets/be6fa03d-a9d8-4b4d-8d96-09ace02065ac)


In the final step, I implemented a script featuring three encryption methods to securely protect the information encoded in the barcode. Additionally, I created a decryption function to verify the integrity of the data. This led to the development of my own price ticket generator with an encrypted barcode:

![Encrypted Ticket](https://github.com/user-attachments/assets/09151314-d8f5-4fed-a620-a88c79351118)

## Acknowledgments

I would like to express my heartfelt gratitude to TJX Companies and my coworkers for the opportunity to work here. This job has been instrumental in supporting my living expenses and helping me build a future in Canada. I truly appreciate being part of such a wonderful team during these challenging times, and I am eager to continue serving our customers and motivating those around me.

## License
This project is licensed under the MIT License.


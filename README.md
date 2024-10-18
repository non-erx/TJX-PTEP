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

## License
This project is licensed under the MIT License.


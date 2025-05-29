# Credit Card Validator (Luhn Algorithm)

This is a simple Python script that validates credit card numbers using the **Luhn algorithm**.

## What It Does

The script checks whether a given credit card number is valid based on the checksum method used by major card issuers (Visa, MasterCard, etc.).

## How It Works

1. Removes spaces and dashes from the input.
2. Reverses the card number.
3. Doubles every second digit and subtracts 9 if the result is greater than 9.
4. Adds all digits together.
5. If the total is divisible by 10, the card is considered valid.

## Example

```python
card_number = '4111-1111-4555-1118'

## Output
```

Valid

```

## File Structure

credit_card_validator.py  # Main script
README.md          # Project overview

How to Run
Make sure you have Python installed.

Clone this repository:

## bash

git clone https://github.com/<your-username>/credit-card-validator.git
cd credit-card-validator

## Run the script:

python card_validator.py

## Author

Abhishek Anand

# Secure Password Generator 🔐

This is a Python script that generates a secure, random password based on customizable constraints. It uses the `secrets` module for cryptographically strong random values and checks that all character requirements are met.

## Features

- ✅ Generate strong passwords with:
  - Digits
  - Uppercase letters
  - Lowercase letters
  - Special characters
- ✅ Fully customizable length and character type requirements
- ✅ Uses secure random generation (`secrets.choice`)
- ✅ Validates the presence of required character types using regular expressions

## Requirements

- Python 3.6+

No external libraries are required — only Python's standard library (`string`, `secrets`, `re`).

## Usage

### Default Usage

```python
new_password = generate_password()
print('Generated password:', new_password)
With Custom Constraints
python
Copy
Edit
new_password = generate_password(
    length=12,
    nums=2,
    special_chars=2,
    uppercase=1,
    lowercase=1
)
print('Generated password:', new_password)
Function Parameters
Parameter	Type	Description	Default
length	int	Total length of the password	16
nums	int	Minimum number of digits	1
special_chars	int	Minimum number of special characters	1
uppercase	int	Minimum number of uppercase letters	1
lowercase	int	Minimum number of lowercase letters	1

Example Output

Generated password: A1@xj#LP9zq3b&um

License
This project is open-source and free to use under the MIT License.

Author
Abhishek Anand
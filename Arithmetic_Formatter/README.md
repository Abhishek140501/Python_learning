# Arithmetic Arranger

A Python function that takes a list of arithmetic problems and returns them arranged vertically in a neatly formatted string, just like in primary school math.

## Features

- Accepts addition and subtraction problems.
- Properly formatted vertical alignment.
- Includes error handling for:
  - Too many problems (max 5).
  - Unsupported operators (only `+` or `-` allowed).
  - Non-digit characters in operands.
  - Operands longer than 4 digits.
- Optional display of results.

## Example

### Input:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
With answers:


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)

Output:


   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
Usage

Import or copy the function into your Python script and call it with a list of problems. Set show_answers=True if you want to display the results.

Function Signature

def arithmetic_arranger(problems, show_answers=False):

Error Messages

Error: Too many problems.

Error: Operator must be '+' or '-'.

Error: Numbers must only contain digits.

Error: Numbers cannot be more than four digits.

Author:
Abhishek Anand
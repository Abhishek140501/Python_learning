# Convert to Snake Case

This Python script provides a utility function to convert a string written in PascalCase or camelCase to `snake_case`.

## Features

- Converts camelCase or PascalCase strings to snake_case.
- Automatically handles strings with mixed uppercase and lowercase letters.
- Removes any leading underscore from the result.

## Example

```python
>>> convert_to_snake_case('aLongAndComplexString')
'a_long_and_complex_string'


Usage

1. Run the script

bash

python script_name.py

Output:

a_long_and_complex_string


2. Use the function in your code

python

from script_name import convert_to_snake_case

snake = convert_to_snake_case("MyVariableName")
print(snake)  # Outputs: my_variable_name
Function Description
convert_to_snake_case(pascal_or_camel_cased_string)

Parameters:

pascal_or_camel_cased_string (str): A string in PascalCase or camelCase format.

Returns:

str: The converted string in snake_case format.

How It Works
Iterates through each character in the string.

If the character is uppercase, it is converted to lowercase and prepended with an underscore.

If it’s not uppercase, the character is left unchanged.

After processing, the list is joined into a string and any leading underscore is stripped.

License
This project is open source and available under the MIT License.

Author
Abhishek Anand
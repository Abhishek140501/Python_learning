def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []

    for i, char in enumerate(pascal_or_camel_cased_string):
        if char.isupper():
            if i != 0:
                snake_cased_char_list.append('_')
            snake_cased_char_list.append(char.lower())
        else:
            snake_cased_char_list.append(char)

    return ''.join(snake_cased_char_list)

def main():
    print(convert_to_snake_case('aLongAndComplexString'))  
    print(convert_to_snake_case('CamelCase'))              
    print(convert_to_snake_case('XMLParser'))              

main()

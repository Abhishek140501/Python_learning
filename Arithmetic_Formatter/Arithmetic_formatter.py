def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_lines = []
    second_lines = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must consist of two operands and one operator."

        first, operator, second = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2
        top = first.rjust(width)
        bottom = operator + second.rjust(width - 1)
        line = '-' * width

        first_lines.append(top)
        second_lines.append(bottom)
        dashes.append(line)

        if show_answers:
            if operator == '+':
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            results.append(result.rjust(width))

    arranged = '    '.join(first_lines) + '\n' + \
               '    '.join(second_lines) + '\n' + \
               '    '.join(dashes)

    if show_answers:
        arranged += '\n' + '    '.join(results)

    return arranged


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

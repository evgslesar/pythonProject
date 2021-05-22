# -*- coding: utf-8 -*-

# total = 0
# with open('calc.txt', 'r') as ff:
#     for line in ff:
#         print(f'Read line {line}')
#         operand_1, operation, operand_2, = line.split(' ')
#         operand_1 = int(operand_1)
#         operand_2 = int(operand_2)
#         if operation == '+':
#             value = operand_1 + operand_2
#         elif operation == '-':
#             value = operand_1 - operand_2
#         elif operation == '/':
#             value = operand_1 / operand_2
#         elif operation == '*':
#             value = operand_1 * operand_2
#         elif operation == '//':
#             value = operand_1 // operand_2
#         elif operation == '%':
#             value = operand_1 % operand_2
#         else:
#             print(f'Unknown operand {operation}')
#             continue
def calc(line):
    # print(f'Read line {line}', flush=True)
    operand_1, operation, operand_2, = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '*':
        value = operand_1 * operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        print(f'Unknown operand {operation}')
    return value

total = 0
with open('calc.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Not enough operands {exc} in line {line}')
            else:
                print(f'Cannot convert to integer {exc} in line {line}')

print(f'Total {total}')


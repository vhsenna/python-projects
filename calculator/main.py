from art import logo

print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

num1 = float(input('What is the first number? '))

for symbol in operations:
    print(symbol)

should_continue = True

while should_continue:
    operation_symbol = input('Pick an operation: ')
    num2 = float(input('What is the next number? '))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {answer:.2f}')

    op = input(f'Type Y to continue calculating with {answer}, type N to start a new calculation or E to exit: ').lower()
    if op == 'y':
        num1 = answer
        print('')
    elif op == 'e':
        should_continue = False
        print('\nGoodbye!')
    elif op == 'n':
        num1 = float(input('\nWhat is the first number? '))
    else:
        print('Invalid option.')

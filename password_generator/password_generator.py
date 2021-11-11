import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

nr_letters= int(input('How many letters would you like in your password? '))
nr_numbers = int(input('How many numbers would you like? '))
nr_symbols = int(input('How many symbols would you like? '))

letter_password = random.sample(letters, nr_letters)
number_password = random.sample(numbers, nr_numbers)
symbol_password = random.sample(symbols, nr_symbols)

password = letter_password + number_password + symbol_password
random.shuffle(password)
print(f'\n{"".join(password)}')

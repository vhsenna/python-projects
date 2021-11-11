rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import randint

images = [rock, paper, scissors]
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

if user == 0 or user ==1 or user == 2:
    print(images[user])

    computer = randint(0, 2)
    print('\nComputer choose:')
    print(images[computer])
    print()

if user == 0:
    if computer == 0:
        print('It\'s a draw.')
    elif computer == 1:
        print('Computer wins.')
    else:
        print('User wins.')
elif user == 1:
    if computer == 0:
        print('User wins.')
    elif computer == 1:
        print('It\'s a draw.')
    else:
        print('Computer wins.')
elif user == 2:
    if computer == 0:
        print('Computer wins.')
    elif computer == 1:
        print('User wins.')
    else:
        print('It\'s a draw.')
else:
    print('It\'s not a valid number.')

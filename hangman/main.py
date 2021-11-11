import random
import os

from words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from art import logo
print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    clear = lambda: os.system('clear')
    clear()

    if guess in display:
        print(f'You\'ve already guessed {guess}.')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f'You guessed {guess} that\'s not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')
            print(f'The word is {chosen_word}.')

    # Join all the elements in the list and turn it into a string.
    print(f'{" ".join(display)}')

    # Check if user has got all letters.
    if '_' not in display:
        end_of_game = True
        print('You win.')

    from art import stages
    print(stages[lives])

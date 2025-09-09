# print("Welcome to Hangman!")
# print('''
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/  
      
# ''')

import random as rd

words = ['apple', 'bannana', 'orange']

comp_choice = rd.choice(words)

print(comp_choice)

comp_choice_len = len(comp_choice)

blanks = ""

for i in range(comp_choice_len):
    blanks += '_'

print(f'\nYou need to guess word whos length is {comp_choice_len}')

print(f"\n {blanks}\n")

option = 'Yes'

word_list = list(comp_choice)
blanks_list = list(blanks)

while True:
    guess_word = input("\nPlease Guess a character from word: ")
    if guess_word in comp_choice:
        blanks += guess_word
        print(f"You have guesls correct word {blanks}")
    else:
        print("You have guessed wrong word")
        option = input("Do you want to continue playing?(Y or N)")
        if option == 'N':
            break






import random as rd
from guess_number_logo import logo
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")

computer_guess = rd.randint(1,100)
# print(computer_guess)

def number_guess_game(attempts):
    while attempts > 0:

        print(f"You have {attempts} remaining to guess the number.")

        player_guess =int(input("Make a guess: "))

        if (player_guess < computer_guess) and (player_guess <=100):
            print("Too Low.\nGuess Again.")
            attempts = attempts - 1
        elif player_guess > computer_guess and (player_guess <=100):
            print("Too High.\nGuess Again.")
            attempts = attempts - 1
        elif player_guess > 100:
            print("The number is out of range of the game!")
            attempts = attempts - 1
        else:
            return f"You got it! The answer was {player_guess}" 
        
    if attempts == 0:
        return f"You are out of chances. You lose. The number was {computer_guess}"
    
player_choice = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

if player_choice == 'easy':
    num_attempts = 10
    print(number_guess_game(num_attempts))
elif player_choice == 'hard':
    num_attempts = 5
    print(number_guess_game(num_attempts))
else:
    print("Wrong input")
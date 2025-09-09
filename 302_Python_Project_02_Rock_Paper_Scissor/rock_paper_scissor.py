print("Welcome to Rock, paper, scissor game!")

print("\nRock ---> 0\nPaper ---> 1 \nScissor ---> 2\n\nGame Rules: \n*Rock beats Scissor\n*Scissor beats Paper\n*Paper beats Rock")

import random as rd

comp_choice = rd.randint(0,2)

user_choice = int(input("Please Enter Rock(0) or Paper(1) or scissor(2): "))

if comp_choice == 0:
    print('\nComputer Choose')
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    Rock
          ''')
elif comp_choice == 1:
    print('\nComputer choose Papper!')
    print('''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
      Paper
''')
else:
    print('\nComputer choose Scissor!')
    print('''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
      Scissor
''')

if user_choice == 0:
    print('You choose Rock!')
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    Rock
          ''')
elif user_choice == 1:
    print('You choose Papper!')
    print('''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
      Paper
''')
elif user_choice == 2:
    print('You choose Scissor!')
    print('''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
      Scissor
''')
else:
    print("You given wrong input! Bye Bye\n")
    exit()

if comp_choice == user_choice:
    print("Its a draw")
elif (comp_choice == 0 and user_choice == 2) or (comp_choice == 1 and user_choice == 0) or (comp_choice == 2 and user_choice == 1):
    print("Computer Win, You Lose!")
elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
    print("Computer Lose, You Win!")
else:
    print("Wrong Input!")
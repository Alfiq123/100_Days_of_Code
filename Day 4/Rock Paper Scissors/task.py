import random

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


# # My Options
# the_list = [rock, paper, scissors]
#
# player = int(input("Enter your chosen one: 0 for Rock, 1 for Paper, or 2 for Scissors "))
#
# computer = random.choice(the_list)
#
# if player >= 3 and player < 0:
#     print("Please Enter a Valid Number")
#
# # Rock vs Rock
# elif player == 0 and computer == rock:
#     print(rock)
#     print("COMPUTER CHOOSE")
#     print(rock)
#     print("DRAW")
# # Rock vs Paper
# elif player == 0 and computer == paper:
#     print(rock)
#     print("COMPUTER CHOOSE")
#     print(paper)
#     print("Computer - Paper Wins")
# # Rock vs Scissors
# elif player == 0 and computer == scissors:
#     print(rock)
#     print("COMPUTER CHOOSE")
#     print(scissors)
#     print("Player - Rock Wins")
#
# # Paper vs Paper
# elif player == 1 and computer == paper:
#     print(paper)
#     print("COMPUTER CHOOSE")
#     print(paper)
#     print("DRAW")
# # Paper vs Rock
# elif player == 1 and computer == rock:
#     print(paper)
#     print("COMPUTER CHOOSE")
#     print(rock)
#     print("Player - Paper Wins")
# # Paper vs Scissors
# elif player == 1 and computer == scissors:
#     print(paper)
#     print("COMPUTER CHOOSE")
#     print(scissors)
#     print("Computer - Scissor WIns")
#
# # Scissors vs Scissors
# elif player == 2 and computer == scissors:
#     print(scissors)
#     print("COMPUTER CHOOSE")
#     print(scissors)
#     print("DRAW")
# # Scissors vs Rock
# elif player == 2 and computer == rock:
#     print(scissors)
#     print("COMPUTER CHOOSE")
#     print(rock)
#     print("Computer - Rock WIns")
# # Scissors vs Paper
# elif player == 2 and computer == paper:
#     print(scissors)
#     print("COMPUTER CHOOSE")
#     print(paper)
#     print("Player - Scissor Wins")
# else:
#     print("NOTHING TO SHOW")



# Chat-GPT Fixes

# List containing moves
the_list = [rock, paper, scissors]

# Get player input
player = int(input("Enter your choice: 0 for Rock, 1 for Paper, or 2 for Scissors "))

# Validate input
if player < 0 or player > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
    # Computer's move
    computer = random.randint(0, 2)

    print(f"\nPlayer chose:\n{the_list[player]}")
    print(f"Computer chose:\n{the_list[computer]}")

    # Determine the result
    if player == computer:
        print("DRAW")
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("Player Wins!")
    else:
        print("Computer Wins!")



# Course Option
game_image = [rock, paper, scissors]

user_choice = int(input("Enter your chosen one: 0 for Rock, 1 for Paper, and 2 for Scissors "))
print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("COMPUTER CHOOSE")

# print(List[Index])
print(game_image[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You're enter a invalid number. YOU LOSE")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN!")
elif computer_choice == 0 and user_choice ==2:
    print("YOU LOSE!")
elif computer_choice > user_choice:
    print("YOU LOSE!")
elif user_choice > computer_choice:
    print("YOU WIN!")
elif user_choice == computer_choice:
    print("IT'S A DRAW")

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

#Write your code below this line 👇

player = input("Welcome to my game. What is your name?")
player_move = int(input(f"{player}, What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors. "))

try:
  opt = [rock, paper, scissors]
  computer_move = random.choice(opt)
  
  player_choice = opt[player_move]
  print(f"You chose: {player_choice}")  
  print(f"Computer chose: {computer_move}") 

  if player_move == 0:
    if computer_move == scissors:
      print(f"\n You win, Yaaay!!")
    elif computer_move == paper:
      print("\n Computer wins.")
 
  if player_move == 1:
    if computer_move == scissors:
      print("\n Computer wins.")
    elif computer_move == rock:
      print("\n You win, Yaaay!!") 
   
  if player_move == 2:
    if computer_move == rock:
      print("\n Computer wins.")
    elif computer_move == paper:
      print("\n You win, Yaaay!!") 
    
  if player_choice == computer_move:
    print("\n It's a tie. Go again!")
except IndexError:
  print("Invalid Choice")

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

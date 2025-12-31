import random 

print("Welcome to Rocky, Paper, Scissors Game!")
player_name = input("Enter your name.")
print(f"Hello {player_name}! Let's start the game.\n")

choices = ["rock","paper","scissors"]
score = 0

for i in range (3):
 player_choice = input("Choose rock, paper, scissors: ").lower()
 computer_choice = random.choice(choices)
 print(f"Computer choose: {computer_choice}")

 if player_choice == computer_choice:
  print("it's a tie!\n")
 elif (player_choice == "rock" and computer_choice == "scissors") or \
      (player_choice == "paper" and computer_choice == "rock") or \
      (player_choice == "scissors" and computer_choice == "paper"):
      print("You win this round!\n")
      score +=1
 else:
      print("You loose this round!\n")

print(f"Game Over! Your total score: {score}/3")
print("Thanks for playing! 🚀")
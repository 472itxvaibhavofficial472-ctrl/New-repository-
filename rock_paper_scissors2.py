import random

print("Welcome to Rock, Paper, Scissors Game!")
player_name = input("Enter your name: ")
print(f"Hello {player_name}! Let's start the game.\n")

while True:
    rounds = int(input("How many rounds do you want to play? "))
    score = 0

    for i in range(rounds):
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!\n")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!\n")
            score += 1
        else:
            print("You lose this round!\n")

    print(f"Game Over! Your total score: {score}/{rounds}")

    if score > rounds // 2:
        print("Congratulations! You won the game!")
    elif score == rounds // 2:
        print("It's a tie!")
    else:
        print("Computer won the game!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
import random

print("\033[1;33mWelcome to Rock, Paper, Scissors Game!\033[0m")
player_name = input("\033[0;37mEnter your name: \033[0m")
print(f"\033[0;37mHello {player_name}! Let's start the game.\033[0m\n")

while True:
    rounds = int(input("\033[1;33mHow many rounds do you want to play? \033[0m"))
    score = 0

    for i in range(rounds):
        player_choice = input("\033[0;37mChoose rock, paper, or scissors: \033[0m").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"\033[1;31mComputer chose: {computer_choice}\033[0m")

        if player_choice == computer_choice:
            print("\033[0;37mIt's a tie!\033[0m\n")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("\033[1;33mYou win this round!\033[0m\n")
            score += 1
        else:
            print("\033[1;31mYou lose this round!\033[0m\n")

    print(f"\033[0;37mGame Over! Your total score: {score}/{rounds}\033[0m")

    if score > rounds // 2:
        print("\033[1;33m🎉 Congratulations! You won the game!\033[0m")
    elif score == rounds // 2:
        print("\033[0;37m🤝 It's a tie!\033[0m")
    else:
        print("\033[1;31m😢 Computer won the game!\033[0m")

    play_again = input("\033[1;33mDo you want to play again? (yes/no): \033[0m").lower()
    if play_again != "yes":
        print("\033[0;37mThanks for playing! 🚀\033[0m")
        break
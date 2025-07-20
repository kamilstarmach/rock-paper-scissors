from random import randint

# Variables to keep track of the score
user_score = 0
computer_score = 0

# Game introduction
print("Welcome to Rock, Paper, Scissors!")
print("First to reach 5 points wins the game.")

# Main game loop
while user_score < 5 and computer_score < 5:
    # Show options
    print("\nChoose your move:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    # Get user's choice
    user_choice = int(input("Enter your number (1/2/3): "))

    # Get computer's random choice
    computer_choice = randint(1, 3)

    # Check if the input is valid
    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please try again.")
        continue

    # Print user's choice
    if user_choice == 1:
        print("You chose Rock.")
    elif user_choice == 2:
        print("You chose Paper.")
    else:
        print("You chose Scissors.")

    # Print computer's choice
    if computer_choice == 1:
        print("Computer chose Rock.")
    elif computer_choice == 2:
        print("Computer chose Paper.")
    else:
        print("Computer chose Scissors.")

    # Check who wins
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        user_score += 1
        print("You win this round!")
    else:
        computer_score += 1
        print("You lose this round.")

    # Show current score
    print(f"Score: You {user_score} - {computer_score} Computer")

# Game over message
print("\nGame over!")
if user_score == 5:
    print("🎉 Congratulations! You won the game!")
else:
    print("😞 The computer won. Better luck next time!")


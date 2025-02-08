import random

# Define the choices
CHOICES = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the result
def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")

# Main game function
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        print("Choose: rock, paper, or scissors")

        # User input
        user_choice = input("Your choice: ").lower()
        while user_choice not in CHOICES:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Your choice: ").lower()

        # Computer selection
        computer_choice = random.choice(CHOICES)

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        # Display result
        display_result(user_choice, computer_choice, result)
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    play_game()
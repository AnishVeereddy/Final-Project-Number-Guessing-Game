import random

def play_game():
    """
    Runs one round of the number guessing game.

    Asks the user to select a difficulty level,
    generates a random number in a range based on difficulty, and
    allows the user to guess until they either guess
    correctly or run out of attempts.
    """

    print("\nChoose difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    difficulty = input("Enter 1, 2, or 3: ")

    # Set difficulty settings
    if difficulty == "1":
        min_num, max_num = 1, 50
        max_tries = 10
    elif difficulty == "2":
        min_num, max_num = 1, 100
        max_tries = 7
    elif difficulty == "3":
        min_num, max_num = 1, 200
        max_tries = 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        min_num, max_num = 1, 100
        max_tries = 7

    # Generate random number
    secret_number = random.randint(min_num, max_num)
    tries_used = 0

    print(f"\nGuess a number between {min_num} and {max_num}")
    print(f"You have {max_tries} attempts.")

    # Game loop
    while tries_used < max_tries:
        user_guess = input("Enter your guess: ")

        # Validate input
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        user_guess = int(user_guess)
        tries_used += 1

        # Provide feedback
        if user_guess > secret_number:
            print("Too high!")
        elif user_guess < secret_number:
            print("Too low!")
        else:
            print("Congratulations! You guessed it!")
            print("Attempts used:", tries_used)
            return

        print("Attempts left:", max_tries - tries_used)

    # If user runs out of attempts
    print("Game over! The number was:", secret_number)


def main():
    """
    Controls the overall flow of the program.

    Repeatedly calls the game function and asks the user
    if they want to play again.
    """
    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    """
    Entry point of the program.

    Ensures that the main function runs only when this file
    is executed directly.
    """
    main()
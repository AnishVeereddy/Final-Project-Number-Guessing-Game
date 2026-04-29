import random

def play_game():
    print("\nChoose difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = input("Enter 1, 2, or 3: ")

    # Set difficulty
    if choice == "1":
        low, high = 1, 50
        max_attempts = 10
    elif choice == "2":
        low, high = 1, 100
        max_attempts = 7
    elif choice == "3":
        low, high = 1, 200
        max_attempts = 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        low, high = 1, 100
        max_attempts = 7

    number = random.randint(low, high)
    attempts = 0

    print(f"\nGuess a number between {low} and {high}")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ")

        # Validate input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Congratulations! You guessed it!")
            print("Attempts used:", attempts)
            return  # end game early if correct

        print("Attempts left:", max_attempts - attempts)

    # If user runs out of attempts
    print("Game over! The number was:", number)


# Main loop for replay
print("Welcome to the Number Guessing Game!")

while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
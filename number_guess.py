import random

def play_guessing_game():
    """
    A simple number guessing game.
    The computer picks a number between 1 and 100, and the user tries to guess it.
    """
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound) # Generate a random number
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print(f"I have picked a number between {lower_bound} and {upper_bound}.")

    while guess != secret_number: # Loop until the guess is correct
        try:
            # Get user input and convert it to an integer
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break # Exit the loop on correct guess

        except ValueError:
            # Handle cases where the user enters non-integer input
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    play_guessing_game()

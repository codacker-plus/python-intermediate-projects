import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    print("\nGuess the number between 1 and 100")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! The number was {number}. Attempts: {attempts}\n")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_game()

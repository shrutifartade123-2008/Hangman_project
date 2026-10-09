
import random

WORDS = {
    "Easy": ["apple", "tiger", "chair", "grape"],
    "Medium": ["python", "college", "student", "journey"],
    "Hard": ["developer", "algorithm", "programming", "technology"]
}

def play_game():
    print("\n" + "=" * 35)
    print("       WELCOME TO HANGMAN")
    print("=" * 35)

    print("\nChoose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    levels = {"1": "Easy", "2": "Medium", "3": "Hard"}
    choice = input("Enter choice (1-3): ").strip()

    if choice not in levels:
        print("Invalid choice! Starting Easy level.")
        choice = "1"

    level = levels[choice]
    secret_word = random.choice(WORDS[level])
    guessed = set()
    attempts = {"Easy": 8, "Medium": 6, "Hard": 5}[level]
    score = 0

    print(f"\nLevel: {level}")
    print(f"You have {attempts} attempts.")
    print("Guess one letter at a time!")

    while attempts > 0:
        display = " ".join(
            letter if letter in guessed else "_"
            for letter in secret_word
        )

        print("\nWord:", display)
        print("Attempts left:", attempts)
        print("Guessed letters:", " ".join(sorted(guessed)) or "None")
        print("Score:", score)

        if all(letter in guessed for letter in secret_word):
            score += attempts * 10 + len(secret_word) * 5
            print("\nCongratulations! You won!")
            print("Word:", secret_word)
            print("Final score:", score)
            break

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        if guess in guessed:
            print("You already guessed that letter!")
            continue

        guessed.add(guess)

        if guess in secret_word:
            print("Correct guess!")
            score += 10
        else:
            print("Wrong guess!")
            attempts -= 1
    else:
        print("\nGame Over!")
        print("The word was:", secret_word)
        print("Final score:", score)

while True:
    play_game()
    again = input("\nPlay again? (yes/no): ").strip().lower()

    if again not in ("yes", "y"):
        print("\nThanks for playing Hangman!")
        print("Keep learning and keep coding!")
        break

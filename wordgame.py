import random

def generate_word(length):
    # Import words from dictionary
    with open('words.txt') as f:
        words = [word.strip() for word in f.readlines() if len(word.strip()) == length]
    return random.choice(words)

def is_real_word(word):
    # Check if the word is in the list of valid English words
    with open('words.txt') as f:
        words = [w.strip() for w in f.readlines()]
    return word in words

def display_feedback(word, guess):
    # Generate feedback for the guessed word
    feedback = []

    # Track which letters have already been marked to avoid duplicates
    marked_letters = set()

    for i in range(len(word)):
        if guess[i] == word[i]:
            # Bold for correct letter in correct position
            feedback.append(f"\033[1m{guess[i]}\033[0m")
            marked_letters.add(guess[i])
        elif guess[i] in word and guess[i] not in marked_letters:
            # Italics for correct letter in wrong position
            feedback.append(f"\033[3m{guess[i]}\033[0m")
            marked_letters.add(guess[i])
        else:
            # Empty dash for incorrect letter
            feedback.append('_')

    return ' '.join(feedback)

def play_game():
    word_length = int(input("Enter the desired word length (4-7): "))
    if word_length < 4 or word_length > 7:
        print("Invalid word length. Exiting.")
        return

    word = generate_word(word_length)
    guesses_left = 6
    guessed_word = ['_'] * word_length

    print(f"Welcome to the Not-Quite-Wordle Game! Guess the {word_length}-letter word. You have 6 chances.")
    print(f"Bold indicates a correct letter in the correct position.")
    print(f"Italics indicates a correct letter in the wrong position.")
    print(f"All correct letters guessed appear in the following feedback.")

    while guesses_left > 0:
        print("\nGuesses left:", guesses_left)
        print("Current word:", ' '.join(guessed_word))

        guess = input("Enter your guess: ").upper()

        if len(guess) != word_length:
            print(f"Invalid guess! Please enter a {word_length}-letter word.")
            continue

        if not is_real_word(guess):
            print("Invalid guess! Not a valid English word.")
            continue

        if guess == word:
            print("Congratulations! You guessed the word correctly.")
            return

        guesses_left -= 1

        feedback = display_feedback(word, guess)
        print(f"Feedback: {feedback}")

    print("Game over! You ran out of guesses.")
    print("The word was:", word)

if __name__ == "__main__":
    play_game()

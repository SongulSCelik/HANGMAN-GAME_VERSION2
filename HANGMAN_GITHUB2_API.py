
'''
🎮 Hangman Game 🎮
This is a Python implementation of the classic Hangman game with API integration.

Features:
- Fetches a random word from an online API.
- Uses ASCII art to represent the hangman stages.
- Limits players to 6 incorrect guesses, as per traditional Hangman rules.
- Provides feedback on progress and reveals the word upon losing.
- Dynamic and user-friendly gameplay.

Objective:
Guess the word letter by letter within the allowed number of incorrect guesses. Good luck! 🍀
'''



import requests
import random

# ASCII art for Hangman stages
hangman_stages = [
    """
       +---+
           |
           |
           |
           |
           |
       =====
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
       =====
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
       =====
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
       =====
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
       =====
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
       =====
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
       =====
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
       =====
    """
]

def fetchWord():
    '''
    Fetch a random word from the API.
    '''
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1", timeout=5)
        response.raise_for_status()  # Raise exception for HTTP errors
        word = response.json()[0]  # Get the first word
        return word
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching word: {e}. Using a fallback word.")
        return random.choice(["fallback", "default", "backup"])  # Fallback words

def initializeGame():
    '''
    Initialize the game with a word fetched from the API.
    '''
    print("🎮 Welcome to API-powered Hangman!")
    print("Fetching a random word from the API...")
    
    secretWord = fetchWord()
    hiddenArray = list(secretWord)
    publicArray = ["_" for _ in hiddenArray]

    return secretWord, hiddenArray, publicArray

def displayProgress(publicArray):
    '''
    Display the current progress of the guessed word.
    '''
    print("📖 Current Progress: ", ' '.join(publicArray))

def updateHiddenWord(guess, hiddenArray, publicArray):
    '''
    Update the public display array with correctly guessed letters.
    '''
    for i in range(len(hiddenArray)):
        if hiddenArray[i].lower() == guess.lower():
            publicArray[i] = hiddenArray[i]

def checkWin(publicArray):
    '''
    Check if the player has successfully guessed the entire word.
    '''
    return "_" not in publicArray

def mainLoop():
    '''
    Main game loop to handle gameplay and scoring.
    '''
    while True:
        secretWord, hiddenArray, publicArray = initializeGame()

        incorrectGuesses = []
        maxIncorrectGuesses = 6

        while len(incorrectGuesses) < maxIncorrectGuesses:
            print(hangman_stages[len(incorrectGuesses)])  # Display the current hangman stage
            displayProgress(publicArray)
            guess = input("🔠 Enter your guess: ")

            if guess.lower() in [letter.lower() for letter in hiddenArray]:
                updateHiddenWord(guess, hiddenArray, publicArray)
                print("✅ Correct guess!")

                if checkWin(publicArray):
                    print(f"🎊 You win! The word was '{secretWord}'.")
                    break
            elif guess.lower() in incorrectGuesses:
                print("⚠️ You've already guessed that letter.")
            else:
                print("❌ Incorrect guess.")
                incorrectGuesses.append(guess.lower())

        if not checkWin(publicArray):
            print(hangman_stages[-1])  # Show the final stage if the game ends
            print(f"💀 Game over! The word was '{secretWord}'.")

        play_again = input("🔁 Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print("Goodbye! 👋")

# Run the game
if __name__ == "__main__":
    mainLoop()








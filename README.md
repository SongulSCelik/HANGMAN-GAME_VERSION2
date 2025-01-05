# HANGMAN-GAME_VERSION2

This version uses dynamic selection of words using an API.

# 🎮 Hangman Game

A Python implementation of the classic Hangman game, enhanced with dynamic word fetching from an online API and ASCII art visuals for the hangman stages. This project is fun, educational, and demonstrates Python programming concepts like loops, conditionals, and API integration.

---

## 📝 Features

- **Dynamic Word Selection:** Words are fetched from the [Random Word API](https://random-word-api.herokuapp.com/) for each round.
- **Traditional Hangman Rules:** Players have 6 chances to guess the word before the hangman is fully drawn.
- **ASCII Art Visuals:** Each incorrect guess updates the hangman drawing for an immersive experience.
- **Fallback Words:** If the API fails, the game uses a local list of words to ensure uninterrupted gameplay.
- **Interactive Gameplay:** Real-time feedback on progress, with clear prompts for guesses.

---

## 📚 How to Play

1. The program fetches a random word from the API.
2. You guess the word letter by letter.
3. Correct guesses reveal the letters in the word. Incorrect guesses add parts to the hangman.
4. You win if you guess the entire word before reaching 6 incorrect guesses.
5. The game ends with a "Game Over" if the hangman is fully drawn.

---

### 🎲 Example Gameplay
📖 Current Progress: _ _ _ _ 🔠 Enter your guess: a ✅ Correct guess! 📖 Current Progress: a _ _ a 🔠 Enter your guess: b ❌ Incorrect guess.

+---+ | | O | | | |


---

## 🛠️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SongulSCelik/HANGMAN-GAME_VERSION2.git
   cd HANGMAN-GAME_VERSION2
   
Ensure you have Python 3.7 or higher installed on your machine.
Install any dependencies (e.g., requests library):
      pip install requests

Run the program











# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using loops, conditionals, and string manipulation. By the end of this assignment, you will create a playable terminal game that tracks guesses and determines win or lose outcomes.

## 📝 Tasks

### 🛠️	Create the Core Hangman Game Loop

#### Description
Write the main game logic for Hangman. The program should choose a secret word, repeatedly prompt the player for guesses, and update the displayed progress after each guess.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of at least 5 words.
- Display the hidden word using underscores (for example: `_ _ _ _ _`).
- Ask the player to guess one letter per turn.
- Reveal correctly guessed letters in all matching positions.


### 🛠️	Handle Attempts and Game Results

#### Description
Add rules for incorrect guesses, ending conditions, and clear final messages. The game should stop when the player either guesses the full word or runs out of attempts.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining.
- Decrease remaining attempts only for incorrect new guesses.
- End the game with a win message when all letters are guessed.
- End the game with a lose message and reveal the secret word when attempts reach 0.

from random import choice
secret_words = ["test", "python"]

class HangmanGame():
    def __init__(self):
        self.secret_word = choice(secret_words)
        self.lifes = 6
        self.guessed_letters = []

    def checker(self, letter):
        if not letter in self.guessed_letters:
            if letter in self.secret_word:
                print(f"Yes letter {letter} is in the word")
                self.guessed_letters.append(letter)
            else:
                self.lifes -= 1
                print(f"No, the letter {letter} isn't there")
        else:
            print(f"You've tried the letter {letter}. The available words are {self.guessed_letters}")
    def display_status(self):
        display = ""
        for char in self.secret_word:
            if char in self.guessed_letters:
                display += char + " "
            else:
                display += "_ "
        return display.strip()
game = HangmanGame()

print("Welcome to the hangman game")

while game.lifes > 0:
    print(f"\Word: {game.display_status()}")
    print(f"\nRemaining lifes: {game.lifes}")

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please, enter one alphabetic letter")
        continue
    game.checker(guess)

    if all(lett in game.guessed_letters for lett in game.secret_word):
            print("Congratulations. You won the game")
            break
else:
    print("You lost, your lifes are over")
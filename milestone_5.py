import random
# List of words
word_list = ['Apple', 'Banana', 'Grape', 'Plum', 'Date']
# Randomly select a word
word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print (f"Good guess! {guess} is in the word")
        
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
    
    # Check the guess is valid
    def ask_for_input(self):

        while True:
            guess = input("Guess a letter: ")
            
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please enter a single character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if num_lives == 0:
            print("You have lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
                if not (game.num_letters == 0 and game.num_letters > 0) :
                    print(f"Congratulations! You have won the game! The word was {game.word}.")
                    break

play_game(word_list)


        



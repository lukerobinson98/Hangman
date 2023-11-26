import random
# List of words
word_list = ['Apple', 'Banana', 'Grape', 'Plum', 'Date']
# Randomly select a word
word = random.choice(word_list)
# Check whether the guess is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word.lower():
        print (f"Good guess! {guess} is in the word")
    else: 
        print(f"Sorry, {guess} is not in the word. Please try again!")
# Check the guess is valid
def ask_for_input():

    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            print("Valid guess:", guess)
            break
        else:
            print("Invalid letter. Please enter a single character")
    check_guess(guess)

ask_for_input()


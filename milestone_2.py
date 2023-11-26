import random
word_list = ['Apple', 'Banana', 'Grape', 'Plum', 'Date']
guess = input("Enter a letter:")
word = random.choice(word_list)
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print ("Oops! That is not a valid input.")
print("Random word:", word)
print("User's leter:", guess)

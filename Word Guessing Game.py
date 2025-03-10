from random import *

name=input("Enter your name: ") # user input for user's name
print("Good luck!",name) # wishes best of luck to user

words = ['rainbow', 'computer', 'science', 'programming',  # list of words
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=choice(words) # random word from the list of words

print("Guess the characters")
guesses=' '
turns=12 # initialize the no. of turns to be 12

while turns>0: # while loop to iterate until user wins or looses
    failed=0  # initialize no.of failed times to be 0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed+=1

    if failed==0: # if user wins in first try
        print("\n You won!")
        print("The correct word is:",word)
        break

    print()
    guess=input("Guess a character: ")
    guesses+=guess

    if guess not in word:
        turns-=1 # if incorrect guess, no.of turns decrement by 1 as penalty for incorrect guess
        print("Wrong guess")
        print("You have",turns,"turns remaining.") # inform the user about the number of turns remaining

    if turns==0: # if no turns left, user looses
        print("Game over. Better luck next time.")
        print("The word was",word)

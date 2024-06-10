import random

# define random function to take random word from the text file
def get_random_word_from_wordlist():
    wordlist = [] # initialize an empty list to store words
    with open("wordlist.txt", 'r') as file: # open the text file in read mode
        wordlist = file.read().split("\n") # Read the file and split by new lines to get the words
    word = random.choice(wordlist) # select a random word from the wordlist
    return word # returns the randomly selected word

# Define the function to get the initial hidden letters of the word
def get_some_letters(word):
    return '_' * len(word)   # returns the dashes with the same length of the  selected word

# This function is used to draw the hangman based on the remaining chances
def draw_hangman(chances):
    if chances == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif chances == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif chances == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|             ")
        print("|             ")
    elif chances == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|     /       ")
        print("|             ")
    elif chances == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\    ")
        print("|     / \\    ")
        print("|             ")

# defines a function to start the hangman game
def start_hangman_game():
    word = get_random_word_from_wordlist() # get random word from the wordlist
    temp = get_some_letters(word) # get the initial hidden letters of the word
    chances = 7 # set the number of chances as
    found = False # set found as false

    while True: # start the game loop
        if chances == 0: # check the player has lost all chances
            print(f"Sorry! You Lost!, the word was: {word}") # print the lost msg
            print("Better luck next time")
            break

        print("*** Guess the word ***")
        print(temp, end='') # print the current state of the hidden word
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: {chances}") 
        character = input("Enter the character you think the word may have: ") # get the player's guess 

        if len(character) != 1 or not character.isalpha(): # validating the input
            print("Please enter a single alphabet only")
            continue # Continue to the next iteration if input is invalid

        else:
            for num, char in enumerate(word): # Iterate through the word to check for matches
                if char == character:
                    temp = temp[:num] + char + temp[num+1:]  # Update the hidden word with the guessed letter
                    found = True # set the found flag true

        if found:  # check if the guessed letter was found in the word
            found = False # Reset the found flag for the next guess
        else:
            chances -= 1 # decrease the number of chances if the guessed letter was incorrect

        if '_' not in temp:  # Checks if the player has guessed all the letters 
            print(f"\nYou Won! The word was: {word}")
            print(f"You got it in {7 - chances} guesses")
            break
        else:
            draw_hangman(chances) # Draw the hangman for the current number of chances

        print()

print("**** Welcome to the Hangman Game ****")

while True: # start a new game if the player wants to play the game again
    choice = input("Do you wanna play hangman again? (yes/no): ")

    if 'yes' in choice.lower():
        start_hangman_game()
    elif 'no' in choice.lower():
        print('Exiting the game...')
        break
    else:
        print("Please enter a valid choice.")

    print("\n") # print a new line to enhance readability

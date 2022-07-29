# Prints the hangman display
def hangman(num, row1, row2, row3):
    separator = " "

    if num == 0:
        print('\n     +------------++-----------------------+')
        print('     |    |‾‾‾‾|  ||                       |')
        print('     |    O    |  ||   ', separator.join(row1), '   |')
        print('     |  / | \\  |  ||   ', separator.join(row2), '   |')
        print('     |   / \\   |  || ', separator.join(row3), ' |')
        print('     |       ==== ||                       |')
        print('     +------------++-----------------------+')
    elif num == 1:
        print('\n     +------------++-----------------------+')
        print('     |    |‾‾‾‾|  ||                       |')
        print('     |    O    |  ||   ', separator.join(row1), '   |')
        print('     |  / | \\  |  ||   ', separator.join(row2), '   |')
        print('     |   /     |  || ', separator.join(row3), ' |')
        print('     |       ==== ||                       |')
        print('     +------------++-----------------------+')
    elif num == 2:
        print('\n     +------------++-----------------------+')
        print('     |    |‾‾‾‾|  ||                       |')
        print('     |    O    |  ||   ', separator.join(row1), '   |')
        print('     |  / | \\  |  ||   ', separator.join(row2), '   |')
        print('     |         |  || ', separator.join(row3), ' |')
        print('     |       ==== ||                       |')
        print('     +------------++-----------------------+')
    elif num == 3:
        print('\n     +------------++-----------------------+')
        print('     |    |‾‾‾‾|  ||                       |')
        print('     |    O    |  ||   ', separator.join(row1), '   |')
        print('     |  / |    |  ||   ', separator.join(row2), '   |')
        print('     |         |  || ', separator.join(row3), ' |')
        print('     |       ==== ||                       |')
        print('     +------------++-----------------------+')
    elif num == 4:
        print('\n     +------------++-----------------------+')
        print('     |    |‾‾‾‾|  ||                       |')
        print('     |    O    |  ||   ', separator.join(row1), '   |')
        print('     |    |    |  ||   ', separator.join(row2), '   |')
        print('     |         |  || ', separator.join(row3), ' |')
        print('     |       ==== ||                       |')
        print('     +------------++-----------------------+')
    elif num == 5:
        print('\n     +------------++-----------------------+')
        print('     |    |‾‾‾‾|  ||                       |')
        print('     |    O    |  ||   ', separator.join(row1), '   |')
        print('     |         |  ||   ', separator.join(row2), '   |')
        print('     |         |  || ', separator.join(row3), ' |')
        print('     |       ==== ||                       |')
        print('     +------------++-----------------------+')
    else:
        print('\n     +------------++-----------------------+')
        print('     |    |‾‾‾‾|  ||                       |')
        print('     |         |  ||   ', separator.join(row1), '   |')
        print('     |         |  ||   ', separator.join(row2), '   |')
        print('     |         |  || ', separator.join(row3), ' |')
        print('     |       ==== ||                       |')
        print('     +------------++-----------------------+')

# Verify that the guess is or isn't a duplicate
def verifyGuess(guesses, letter):
    for i in range(26):
        if guesses[i] == letter:
            return True
    return False

# Verify that the input is a letter
def verifyLetter(letter):
    # Lowercase and uppercase letters to verify that the inputs are letters
    lowerAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upperAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Lowercase letter
    for i in lowerAlphabet:
        if i == letter:
            return True
    # Uppercase letter
    for i in upperAlphabet:
        if i == letter:
            return True
    return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------#

# Title of game
print('\n               THE HANGMAN GAME')

# The word or phrase that the player will guess
# Input should be only lowercase letters (can include space):
#secretPhrase = input(">>What is the secret phrase or word? Input should be only lowercase letters (can include space):")
secretPhrase = "A Series of Unfortunate Events"     #  NOTE: Can change the secret phrase to another phrase/word
actualSecretPhrase = secretPhrase
secretPhrase = secretPhrase.lower()     # Turn phrase into lowercase, to verify word/phrase

# The hint for the word or phrase
#hint = input(">>What is the hint for the word or phrase:\n")
hint = "Hint: Book title" + "\n"    # NOTE: Can change hint

size = 0
# Find the size of the word/phrase
for i in range(len(secretPhrase)):
    if verifyLetter(secretPhrase[i]) == True:
        size = size + 1

row1 = []
row2 = []
row3 = []
row1 = [0 for i in range(8)]
row2 = [0 for i in range(8)]
row3 = [0 for i in range(10)]

# Fill each row as "_ "
for i in range(8):
    row1[i] = "_"
    row2[i] = "_"
for i in range(10):
    row3[i] = "_"

# Total guesses, representation of each body part
totalGuesses = 6

# Keep track of each guess
guesses = []
guesses = [0 for i in range(26)]

# Initialize empty list for each letter
output = []
output = [0 for i in range(len(secretPhrase))]

# Add spaces or punctuation from word/phrase to output
# Or include lines for letters that the user will guess
lines = " "
for i in range(len(secretPhrase)):
    output[i] = " "
    if verifyLetter(secretPhrase[i]) == True:
        lines = lines + "‾ "
    else:
        lines = lines + "  "
        output[i] = secretPhrase[i]

# Print the hangman
hangman(totalGuesses, row1, row2, row3)

# Print the hint
print(hint)

# Print output
separator = " "
print("", separator.join(output)) 

# Print the lines, each for each letter
print(lines)

position = 0        #keep track of guessed positions
p1 = 0              #keep track of row1 positions
p2 = 0              #keep track of row2 positions
p3 = 0              #keep track of row3 positions
complete = False
while complete == False:
    correct = False
    # Ask the user for a letter guess
    letter = input('\n>> Guess a letter: ')
    # Verify that the input is a letter
    while True:
        if verifyLetter(letter) == True:
            break
        else:
            letter = input('>> Guess a letter (a-z), try again: ')
    print("")

    duplicate = False
    # Check if letter was guessed already
    while True:
        duplicate = verifyGuess(guesses, letter)
        if duplicate == True:
            letter = input('>> Letter was guessed already, try again: ')
            # Verify that the input is a letter
            while True:
                if verifyLetter(letter) == True:
                    break
                else:
                    letter = input('>> Guess a letter (a-z), try again: ')
        else:
            break
    
    duplicate = False
    # Add guessed letter to guessed list to prevent duplicates
    for i in range(26):
        if guesses[i] == letter:
            duplicate = True
    if duplicate == False:
        guesses.insert(position, letter)    
        position = position + 1 
        if p1 < 8:
            row1[p1] = letter.upper()       #add to row1
            p1 = p1 + 1
        elif p2 < 8:
            row2[p2] = letter.upper()       #add to row2
            p2 = p2 + 1
        else:
            row3[p3] = letter.upper()       #add to row3
            p3 = p3 + 1

    count = 0
    # Search for letter, if it found then add it to the output list
    for i in range(len(secretPhrase)):
        if secretPhrase[i] == letter:
            output[count] = actualSecretPhrase[i]       # Store the non-lowercase secret word/phrase
            correct = True
        count = count + 1

    # If incorrect guess, subtract 1 from total (6)
    if correct == False:
        totalGuesses = totalGuesses - 1

    print('+===============================================+')

    # Print the hangman
    hangman(totalGuesses, row1, row2, row3)

    # Print the hint
    print(hint)

    # Print the letter that was guessed
    print("", separator.join(output)) 

    # Print the lines, each for each letter
    print(lines)

    # Game ends
    if totalGuesses == 0:
        print('\n>> GAME OVER')
        break

    # Checks if the user guessed the entire phrase/word
    count = 0
    for i in range(len(output)):
        if verifyLetter(output[i]) == True:
            count = count + 1
    
    # Game ends, user won
    if count == size:
        complete = True
        print('\n>> YOU WON!')

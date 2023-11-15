import random
import sys


def main():
    # Get a random word.
    answer = getRandomWord()

    
    # Start by asking the user for their initial guess
    # Ask them to "Enter a 5 letter guess?"
    
    attempts = 0
    
    while attempts < 6:
        guess = input("Enter a 5 letter guess?")
        print()
        printGuessColors(guess,answer)
        attempts+=1   
        if guess == answer:
            print(f"You Won! That took {attempts} guess(es).")
            break     
    if guess != answer:
        print(f"You lost. The answer was {answer}.")
   

# A helper method that prints the guess with the
# correct colors to the console.
# Example usage:
# printGuessColors("broke", "broke") should print the five lines:
#
# b - Green
# r - Green
# o - Green
# k - Green
# e - Green
def printGuessColors(guess, answer):
    
    for index in range(5):
        print(letterColor(index,guess,answer))        
        
   


# A helper method that determines the color
# of the letter in the guess. This function
# should return "Green", "Red", or "Yellow"
def letterColor(index, guess, answer):
    
    if guess[index] == answer[index]:
        return f"{answer[index]} - Green"
    elif guess[index] not in answer[0:]:
        return f"{guess[index]} - Red"
    else: 
        return f"{guess[index]} - Yellow" 


   
# A method that gets a random word from a file.

def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)
main()
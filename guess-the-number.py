# The Goal: Similar to the first project, this project also uses the random module in Python.
# The program will first randomly generate a number unknown to the user. The user needs to
# guess what that number is. (In other words, the user needs to be able to input information.)
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong
# (e.g. The number is too high or too low). If the user guesses correctly, a positive indication
# should appear. You’ll need functions to check if the user input is an actual number, to
# see the difference between the inputted number and the randomly generated numbers, and to
# then compare the numbers.

import random

## intialize the number to guess
## to make it easier, the number will be between 1 and 50
random_num = random.randint(1, 50)

## function to check if the user input is an actual number
def isNum(userGuess):
   try:
       return int(userGuess)
   except ValueError:
       print("Please enter an integer between 1 and 50.")

## function to check the difference between guessed number and randomly generated number
def guessNum(userGuess, generatedNum):
   try:
       if((userGuess == generatedNum) and (1 <= userGuess and userGuess <= 50)):
           guessCorrect = True
           print("You guessed correctly! The random number was " + str(generatedNum) + " and you guessed " + str(userGuess))
       elif((userGuess > generatedNum) and (1 <= userGuess and userGuess <= 50)):
           guessCorrect = False
           print("Your guess was too high... Guess again!")
       elif((userGuess < generatedNum) and (1 <= userGuess and userGuess <= 50)):
           guessCorrect = False
           print("Your guess was too low... Guess again!")
       else:
           guessCorrect = False
           print("Your guess was not between 1 and 50. Guess again!")
   except ValueError:
       print("Error. Please try again")
  
   return guessCorrect

## primary function of the game

print("Welcome to the guessing game! To play, you need to guess a number between 1 and 50. /n If you guess too high or low, the game will let you know and guess again. When you guess the correct number the game is over!")

## intialize guess correct as false
guessCorrect = False

while(not guessCorrect):
   intGuess = isNum(input("Please guess a number between 1 and 50. You need to guess the correct number to win."))
   guessNum(intGuess, random_num)

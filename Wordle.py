'''
hello
birth
child
dress
earth
first
guide
happy
index
magic
'''
import random
from termcolor import colored
file = open("C:\\Users\itssm\python\Sayur\Home-work\Week-9\\FiveLetterWords.txt", "r")
attemptCount = 5           #attemptCount 5
userWordList = []      
programWordList = []
countingAttempt = 0

def isWordMatching(wordList):      #Invoking the function with params
    programWord = random.choice(wordList)      #word list contains 10 five letter word and getting the random word in that
    counting = 0
    for attemptIndex in range (0, attemptCount):
        print("\nAttempt", attemptIndex + 1)
        userInputWord = input("")                   #getting input from user
        userWordList = []
        programWordList = []                        #if the user entered word is more than or less than five the game stops
        if (len(userInputWord) != 5):
            print("You have to enter 5 letter word")
            break
        if(programWord.strip() != userInputWord.strip()):                  #if programs random word and user enter word is not equals
            for userWordChars in range (0, len(userInputWord)):          
                userWordList.append(userInputWord[userWordChars])          #appending the each char to userWordList
                programWordList.append(programWord[userWordChars])         #appending the each char to programWordList
            wordStatus(programWordList, userWordList)                      #sending the both list to wordStatus function
        else:
            wonTheGame(userInputWord)                                      #if programs random word and user enter word in correct it moves to wonTheGame function
            break
        counting += 1

        if counting == 5:
            print("\n"+(colored("you have lost the game", 'red')))
def wonTheGame (userInputWord):
    print (end=(colored(userInputWord, 'green')))                          #it print Congrats You Won the Game in green color
    print("\nCongrats You Won the Game")

def wordStatus(programWord, userInputWord):
    for userIndex in range (0, len(userInputWord)):                         #this loop is runs between 0 to length of user entered word
        if (programWord[userIndex] == userInputWord[userIndex]):            #if the program words char and user entered char is equal 
            print (end=(colored(userInputWord[userIndex], 'green')))        #the char is print in green color
        elif (userInputWord[userIndex] in programWord):                     #elfi program word contains the char 
            if(userInputWord.count(userInputWord[userIndex]) > programWord.count(userInputWord[userIndex])):  #and we counting the specific char length in each list
                print (end=(colored(userInputWord[userIndex], 'red')))          #if the userInputs counts is greater than program count it print the char in red color
            else:
                print (end=(colored(userInputWord[userIndex], 'yellow')))               # or less it print the char in yellow color
        else:                                                                  #if the user enterd words specific char is not in program word 
            print(end=(colored(userInputWord[userIndex], 'red')))               #it prints the char in red color

wordList = file.readlines()
isWordMatching(wordList)


'''
sample output:-
Attempt 1
index
index
Attempt 2
guide
guide
Attempt 3
birth
birth
Attempt 4
first
first
Congrats You Won the Game

----------------------------------


Attempt 1
a
You have to enter 5 letter word

-----------------------------------

Attempt 1
magic
magic
Attempt 2
first
first
Attempt 3
hello
hello
Congrats You Won the Game

------------------------------------

Attempt 1
ddjhx
ddjhx
Attempt 2
sdjse  
sdjse
Attempt 3
sdcgv
sdcgv
Attempt 4
etyyu
etyyu
Attempt 5
sdfdd
sdfdd
you have lost the game

'''



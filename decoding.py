'''
You have a message that you want to send to your friend. You don't want others to see the message. You code the message and send it.
The alg to code is - split each word in half and reverse it (eg cricket becomes ketccri), if the word ends with a vowel, split at the 
last letter and reverse (eg cinema becomes acinem), if the word has numbers, spell the number but add A as first and last letters
 (8 pm becomes AeightA pm ).
 Write an app that can code and decode the message.
'''


userWord = input("enter your word: ")
centerWord = None
vowelWords = ['a', 'e', 'i', 'o', 'u']
isVowel = 0
noVowel = 0
isNumbers = 0
finalWord = []
removeDupes = []
numbersDict = {
    "zero": {
        "number": '0',
        "numberInWord": "zero"
    },
    "one": {
        "number": '1',
        "numberInWord": "one"
    },
    "two": {
        "number": '2',
        "numberInWord": "two"
    },
    "three": {
        "number": '3',
        "numberInWord": "three"
    },
    "four": {
        "number": '4',
        "numberInWord": "four"
    },
    "five": {
        "number": '5',
        "numberInWord": "five"
    },
    "six": {
        "number": '6',
        "numberInWord": "six"
    },
    "seven": {
        "number": '7',
        "numberInWord": "seven"
    },
    "eight": {
        "number": '8',
        "numberInWord": "eight"
    },
    "nine": {
        "number": '9',
        "numberInWord": "nine"
    },
}


def isVowelAtLast():                             #isVowelAtLast function is checking is there is any vowel word present at last of the user input
    for vowel in range (len(vowelWords)):
        if userWord[len(userWord) - 1] == vowelWords[vowel]:   
            finalWord.append(vowelWords[vowel])   #first appending the vowel char
            for ind in range (len(userWord) - 1):
                finalWord.append(userWord[ind])    # and im appending the rest
    return finalWord
    

def HandleReversing():                             #HandleReversing function is call when the user input has no vowel char present at last and no number present in between
    for index in range (int(len(userWord)/2) + 1, len(userWord)):
        finalWord.append(userWord[index])           #here im appending the last to middle chars
    if len(userWord) %2 != 0:
        centerWord=int(len(userWord) / 2)
        finalWord.append(userWord[centerWord])       #here im appending the middle char
    else:
        centerWord=int(len(userWord) / 2)
        finalWord.append(userWord[centerWord])
    for index in range (0, int(len(userWord)/2)):
        finalWord.append(userWord[index])           #here im appending rest
    return finalWord


def numbersInUserword():                    #numbersInUserword is call when the user input has any numbers
    for index in range (len(userWord)):
        for key in numbersDict:
            if (userWord[index] == numbersDict[key]["number"]):     #here checking the entered num equals in numbersDict
                if userWord[0] != numbersDict[key]["number"]:
                    for ind in range (0, index):
                        finalWord.append(userWord[ind])          #appending the first half berfore the number
                    for ind in range (0, index):
                        if numbersDict[key]["number"] in userWord:
                            removeDupes.append('A' + numbersDict[key]["numberInWord"] + 'A')   #appending the number with A
                    finalWord.append(*set(removeDupes))
                    for ind in range (index + 1, len(userWord)):
                        finalWord.append(userWord[ind]) #appending the rest
                else:
                    for ind in range (0, index+1):
                        if numbersDict[key]["number"] in userWord:
                            finalWord.append('A' + numbersDict[key]["numberInWord"] + 'A')
                    for ind in range (index + 1, len(userWord)):
                        finalWord.append(userWord[ind])
    return finalWord                    


isDigit = userWord.isdigit()     #isdight says is number present
for checkingVowel in range (len(vowelWords)):
    if userWord[len(userWord) - 1] == vowelWords[checkingVowel]:   #checking number present
        isVowel += 1
    else:
        noVowel += 1
for ind in range (0, len(userWord)):
    if userWord[ind].isdigit():
        output = numbersInUserword()
        isVowel = -1
if isVowel == 1:
    output = isVowelAtLast()
elif isVowel == 0:
    output = HandleReversing()
    
    
print(*output)

'''
output:

input: cricket
output: k e t c c r i

input: cinema
otuput: a c i n e m

input: 8mk
output: AeightA m k  

input: room
output: m o r o
'''

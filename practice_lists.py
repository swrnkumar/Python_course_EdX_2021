import math
import string

#practice list operations

L = [2,76,98894]

print(L)

L.append(546)
print(L)

L1 = [4,5,8,98]
L2 = [45,6,9282]

L3 = L1 + L2
print(L3)

L1.extend(["a","b","hello world"])

print(L1)
L1.remove(5)
print(L1)
L1.pop()
print(L1)

s = "Hello"

Alpha = list(s)
print(Alpha)

L2.sort()
print(L2)

listA = [100,0,1,4,7]
listA.extend([4, 1, 6, 3, 4])

print(listA)

# examples to show lists are mutable

warm = ['red', 'yellow', 'orange']

hot = warm
hot.append('pink')

print(hot)
print(warm)


chill = ['blue', 'green', 'grey']

cool = ['blue', 'green', 'grey']

chill.append('brown')

print(chill)
print(cool)

ListA = ['a', 'e', 'i', 'o']
ListB = ListA[:]

ListA.append('u')

print(ListA)
print(ListB)

colour = ['black', 'red', 'grey', 'orange']

colour.sort()

print(colour)

newcolour = sorted(colour)
print(newcolour)

warmcolour = ['red', 'orange']
hotcolour = ['yellow']
brightcolour = [warm]

brightcolour.append(hotcolour)

print(warmcolour)
print(hotcolour) 
print(brightcolour)

hotcolour.append('magenta')

print(hotcolour)
print(brightcolour)

L1 = [1,2,3,4,5,6,7]
L2 = [3,4,7,9,10]

def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

remove_dups(L1,L2)

print(L1)
print(L2)

L3 = [5.67,6.8374,7.9877575,9.647,8.87]

def applytoEach(L, f):
    ''' applying to each element of the list, function '''
    for i in range(len(L)):
        L[i] = f(L[i])

applytoEach(L3, int)

print(L3)


# Fibonacci series

numofCalls = 0

def fib(n):
    ''' Fibonacci series, returns values'''
    global numofCalls
    numofCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


values_fibonacci = fib(15)

print(f"""The number of Fibonacci for 15 is {values_fibonacci}
and number of times function was called {numofCalls}""")


# # Part 1 of game hangman - function isWordGuessed

# def isWordGuessed(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: boolean, True if all the letters of secretWord are in lettersGuessed;
#     False otherwise
#     '''
#     for letter in secretWord:
#         if letter in lettersGuessed:
#             return True
#         else:
#             return False

# WordofChoice = input("Enter your secret word: ")

# GuessList = input("Enter list of letters guessed: ")

# GameResult = isWordGuessed(WordofChoice, GuessList)

# print(f"Game results {GameResult}")



# # Part 2 of game hangman - getGuessedWord

# def getGuessedWord(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the word the user is guessing
#     lettersGuessed: list, what letters have been guessed so far
#     returns: string, comprised of letters and underscores that represents
#       what letters in secretWord have been guessed so far.
#     '''
#     guessedString = ""
#     underscore = " _ "

#     for s in secretWord:
#         if s in lettersGuessed:
#             guessedString = guessedString + s
#         else:
#             guessedString = guessedString + underscore
#     return guessedString

# SWord = input("Enter your word: ")
# GList = input("Enter list of guessed letters: ")


# GResult = getGuessedWord(SWord, GList)

# print(f"The results of this game is {GResult}")


# Part 3 of game hangman - getAvailableLetters

print(string.ascii_lowercase)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    s = string.ascii_lowercase
    alphabetList = []
    notGuessed = ""

    for letters in s:
        alphabetList.append(letters)

    for letter in alphabetList:
        if letter in lettersGuessed:
            alphabetList.remove(letter)
    
    for l in alphabetList:
        notGuessed = notGuessed + l
    
    return notGuessed

letterList = input("Enter list of guessed letters: ")

Finalstr = getAvailableLetters(letterList)

print(f"Remaining available letters for guessing are: {Finalstr}")

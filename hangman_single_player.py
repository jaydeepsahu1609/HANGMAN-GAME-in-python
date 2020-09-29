#TRADITIONAL HANGMAN GAME single player
#DEVELOPED BY- JAYDEEP SAHU (jaydeepsahu1609)

import random
from string import digits, punctuation
from os import system

def intro():
    print("="*20, "HANGMAN GAME BY JAYDEEP SAHU", "="*20)
    choice = int(input("Do you want to see the rules? Press 1 else 0 : "))
    if(choice):
        rules()

def rules():
    print("""
        Rules:
            * Computer generates a random word,   and  Player has 
            to guess the word in minimum of 5 attempts. For ease, 
            category of the word is displayed as a hint.
            * For each  correct  guess  Player gets 10 
            points and with each wrong guess  Player
            loses 5 points and 1 life.
            * Player can only give  a single letter to 
            guess. A complete word is not allowed.
            * Numbers have not been included for guessing, so
            go only for letters.
            * Player can type 'exit'  anytime  to exit 
            the game.
            * If Player guesses the correct word with
            atleast  1  life  remaining,  he / she  is 
            declared as the winner of this game.

            Play the Game. Good Luck.

        """)


def take_word():
    '''
    returns a word randomly from word-list
    '''
	categories = {"sports":['cricket', 'tennis', 'football', 'carrom', 'boxing'], "countries":['india', 'srilanka', 'china', 'australia', 'brazil', 'nepal'], "continent":['asia', 'australia', 'europe', 'afrika', 'antartika'], "oceans":['pecific', 'arctic', 'indian', 'atlantic']}
	category = random.choice(list(categories.keys()))   #randomly selects a category
	print("Category : ", category)
	actualword = str(categories[category][int(random.randrange(len(categories[category])))])
    #selects a word randmly from that category and assigns it to 'actualword'
	actualword = list(actualword)
	word = ('_ '*len(actualword)).strip()
    #create a string of length equal to that of actualword but replaces each letter with a dash ('-')
	return actualword, word.split()

      
def guess(guessed_list):
    '''
    takes the guessed letter from user
    '''
    while(True):        #run till player either enters 'exit' or guesses the word correctly 
        guess = input("Guess a letter : ")
        if guess  in digits or guess in punctuation:
            print("Invalid input.")             #numbers not allowed for guessing
        else:
            exit == 'exit'              #what actually exit looks like
            guess = guess.lower()       
            if len(guess)>1 and guess!="exit" :         #only single letter needs to be entered
                print("Give a single letter.")
            elif guess == "exit":       #player enters exit before guessing the complete word
                print("You lost.")
                quit(0)
            else:           #correct input
                if guess in guessed_list:   
                    print("'{}' has already been guessed.".format(guess))
                else:
                    guessed_list.append(guess)      #append to the  list of guessed-letters if not guessed before
                    return guess            

def hangman(actualword, guessed, word):
    if guessed in actualword:
        count = actualword.count(guessed)   #finds the number of occurances of guessed letters in actualword
        if(count == 1):                     
            index = actualword.index(guessed)
            word[index] = guessed       #replaces '-' with the guessed letter
        elif(count>1):                  #guessed letter appers more than 1 time in actualword
            while(count!=0):
                index = 0
                for letter in actualword:
                    if letter == guessed:
                        word[index] = guessed      #replaces '-' for all occurances of the guessed letters
                        count -= 1
                    index += 1
    print(' '.join(word), end='\n')     #return the dashed word after joining them
    return word


def play():
    '''
    desides the flow of our game
    '''
    intro()     #roll the intro
    actualword, word = take_word()      #select a word randomly
    win = False         
    life = 5        #5 lives for player, increase from here if you want
    score = 0       #score is 0
    guessed_list = []           #no letter has been guessed initially
    while(life >0 ):            #repeat if player  has lives remaining or has not won yet
        print("\nLife : {}\tScore : {}".format(life, score), end="\n\n")    #our scoreboard :)
        guessed = guess(guessed_list)       #make a guess!!
        prev_word = word[:]         # initially looks like : ' - - - - -'    
        word = hangman(actualword, guessed, word[:])        #check if the guess is correct 
        if(word == prev_word):      #word is equal to previous word if no letter has been guessed correctly
            print("Guessed Wrong !! ")
            life -= 1       #lose a life
            score -= 5      #negative marking
        else:
            print("Well Guessed !! ")
            score += 10     #reward for guessing correct letter
        if word == actualword:          #guessed the word
            print("Guessed the word correctly. You Win.\nYour Score is :", score)
            break
        print('_'*35)           #separator line
    if(not life):           #0 life remaining :(
        print("No life. You lost. Better luck Next time.")
    choice = int(input("Do you want to play again? 1 for YES, 0 to quit : "))
    if(choice):
    	play()
    else:
    	quit(0)

play()        


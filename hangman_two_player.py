def intro():
    print("="*20, "HANGMAN GAME BY JAYDEEP SAHU", "="*20)
    choice = int(input("Do you want to see the rules? Press 1 else 0 : "))
    if(choice):
        rules()

def rules():
    print("""
        Rules:
            * Player-1 gives a word,   and  Player-2 has 
            to guess the word in minimum of 5 attempts.
            * For each  correct  guess  Player-2 gets 10 
            points and with each wrong guess  Player-2 
            loses 5 points and 1 life.
            * Player-2 can only give  a single letter to 
            guess. A complete word is not allowed.
            * Player-2 can type 'exit'  anytime  to exit 
            the game.
            * If Player-2  guesses the correct word with
            atleast  1  life  remaining,  he / she  is 
            declared as the winner of this game.

            Play the Game. Good Luck.

        """)


from string import digits, punctuation
from os import system
def take_word():
    while(True):
        actualword = input("enter the word : ")
        for char in actualword:
            if char in digits or char in punctuation:
                print("Numbers and special characters are not allowed.")
                break
            else:
                actualword = [char.lower() for char in actualword]
                word = ('_ '*len(actualword)).strip()
                system('cls')
                return actualword, word.split()
      
def guess(guessed_list):
    while(True):
        guess = input("Guess a letter : ")
        if guess  in digits or guess in punctuation:
            print("Invalid input.")
        else:
            exit == 'exit'
            guess = guess.lower()
            if len(guess)>1 and guess!="exit" :
                print("Give a single letter.")
            elif guess == "exit":
                print("You lost.")
                quit(0)
            else:
                if guess in guessed_list:
                    print("'{}' has already been guessed.".format(guess))
                else:
                    guessed_list.append(guess)
                    return guess

def hangman(actualword, guessed, word):
    if guessed in actualword:
        count = actualword.count(guessed)
        if(count == 1):
            index = actualword.index(guessed)
            word[index] = guessed
        elif(count>1):
            while(count!=0):
                index = 0
                for letter in actualword:
                    if letter == guessed:
                        word[index] = guessed
                        count -= 1
                    index += 1
    print(' '.join(word), end='\n')
    return word


from os import system
def play():
    intro()
    actualword, word = take_word()
    win = False
    life = 5
    score = 0
    guessed_list = []
    while(life >0 ):
        print("\nLife : {}\tScore : {}".format(life, score), end="\n\n")
        guessed = guess(guessed_list)
        prev_word = word[:]
        word = hangman(actualword, guessed, word[:])
        if(word == prev_word):
            print("Guessed Wrong !! ")
            life -= 1
            score -= 5
        else:
            print("Well Guessed !! ")
            score += 10
        if word == actualword:
            print("Guessed the word correctly. You Win.\nYour Score is :", score)
            break
        print('_'*35)
    if(not life):
        print("No life. You lost. Better luck Next time.")
        choice = int(input("Do you want to play again? 1 for YES, 2 to quit : "))
        if(choice):
            play()
        else:
            quit(0)
play()        



import random
numberToGuess = random.randrange(2,101)


def GiveMeARealName():

    print "Howdy, what's your name?"
    while True:
        name = str(raw_input ("(type in your name) "))
        if name.isalpha():
            print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
            return False
        else:
            print "This does not appear to be a name! Please try again using the alphabet."
                
        
GiveMeARealName()

def TimeToGuess(i, guess, num_of_guess):
    
    num_of_guess = 0
    while i < 101:
        guess = raw_input("Your guess? ")
        if not guess.isdigit():
            print "This is not a number! Please try a number between 1 and 100."
        else:
            guess = int(guess)
            GiveAHint(i, guess, num_of_guess)  
            
        num_of_guess = num_of_guess + 1

def GiveAHint(i, guess, num_of_guess):

    if guess > numberToGuess:
        print "Your guess is too high, try again."
    elif guess < numberToGuess:
        print "Your guess is too low, try again."
    else:
        print "Well done! You found my number in %s tries!" % num_of_guess
        i = 101



TimeToGuess(i, guess, num_of_guess)
    

    #if not guess.isdigit():
     #   print "I'm sorry, that is not a valid number. Please try again."
     #   guess = raw_input ("Your guess? ")
    #elif guess != range(2,101):
     #   "That number is outside of this program's range. Please choose a number between 1 and 100."



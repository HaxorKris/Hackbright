import random
numberToGuess = random.randrange(2,101)
j = 0
i = 0


print "Howdy, what's your name?"
while j < 6:
    name = str(raw_input ("(type in your name) "))
    if not name.isalpha():
        print "This does not appear to be a name! Please try again using the alphabet."
    else:
        print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
        j = 7 

num_of_guess = 0
while i < 101:
    guess = raw_input("Your guess? ")
    if not guess.isdigit():
        print "This is not a number! Please try a number between 1 and 100."
    else:
        guess = int(guess) 
            
    num_of_guess = num_of_guess + 1


    if guess > numberToGuess:
        print "Your guess is too high, try again."
    elif guess < numberToGuess:
        print "Your guess is too low, try again."
    else:
        print "Well done! You found my number in %s tries!" % num_of_guess
        i = 101


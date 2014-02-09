import random
numberToGuess = random.randrange(1,101)


print "Howdy, what's your name?"

# Get user's name
name = str(raw_input ("(type in your name) "))
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name

# Initialize guess counter
num_of_guess = 0

while num_of_guess > -1:
    # Prompt for guess
    guess = raw_input("Your guess? (1-100) ")
    # Increment our guess counter, regardless of validity of guess. 
    num_of_guess = num_of_guess + 1
    # Check for valid input.. 
    if not guess.isdigit():
        print "This is not a valid number! Please try a number between 1 and 100."
    else: 
        guess = int(guess)
        if guess > numberToGuess:
            print "Your guess is too high, try again."
        elif guess < numberToGuess:
            print "Your guess is too low, try again."
        elif guess < numberToGuess:
            print "Your guess is too low, try again."
        else:
            print "Well done! You found my number in %s tries!" % num_of_guess
            num_of_guess = -5

# while num_of_guess > -1:
    # Prompt for guess
#    guess = raw_input("Your guess? (1-100) ")
    # Increment our guess counter, regardless of validity of guess. 
#    num_of_guess = num_of_guess + 1
    # Check for valid input.. 
#    if not guess.isdigit():
#        print "This is not a number! Please try a number between 1 and 100."
#    else:
#        guess = int(guess) 
#        if guess > numberToGuess:
#            print "Your guess is too high, try again."
#        elif guess < numberToGuess:
#            print "Your guess is too low, try again."
#        else:
#            print "Well done! You found my number in %s tries!" % num_of_guess
#            num_of_guess = -5


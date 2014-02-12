#!/usr/bin/env python

import sys
import random



#------------------------------
# The story, so far..
#
# 1. read the file (done)
# 2. copy the file into a single string/variable )done)
# 3. close the file (done)
# 4. split the string into words (done)
# 5. identify the number of words in the new list (done)
# 6. crawl through the list and pair:
# word 1 + word 2
# if this doesn't exist as a tuple already, add it, with the third word as a value
# if this does exist as a tuple already, append the next word to the value list

#def make_chains(corpus):

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
markov chains."""
    dictionary = {}

    split_words = corpus.split()
    # print split_words
   
    for i in range(len(split_words)-2):
        if dictionary.get((split_words[i], split_words[i+1])):
            dictionary[(split_words[i], split_words[i+1])].append(split_words[i+2]) # append list with split_words[i+2]
        else:
            dictionary[(split_words[i], split_words[i+1])] = [split_words[i+2]]

    print dictionary
    return dictionary


# ---------- this is all intact from the sample
#
def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
based off an original text."""
    keylist = chains.keys()
    first_tuple = random.choice(keylist)
    # could try the below by accessing first_tuple[0] and first_tuple[1]

    word1, word2 = first_tuple   # might need parentheses
    
    print first_tuple[0]
    print first_tuple[1]

    print word1
    print word2

    # build the list: the first two items are the first tuple
    output_list = [word1, word2]
    print output_list

    for i in range(20):
        next_word = random.choice(chains[(word1, word2)])
        word1, word2 = word2, next_word

        print word1
        print word2
        print next_word

        output_list.append(next_word)

        print output_list

    output_string = " ".join(output_list)
    
    output_string[0] = output_string[0].lower()

    print output_string
    return output_string

# join outside of for loop

# return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    f = open('blender.txt', 'r')
      #read the file into another copy
    input_text = f.read()
      #close original file
    f.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()



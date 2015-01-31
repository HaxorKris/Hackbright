from sys import argv
script, filename = argv
source_file = open(filename, "r")

text = source_file.read() # gives a giant string

source_file.close()

lower_case = text.lower()
# "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{}|~"
words = lower_case.split()

dictionary = {}  # start an empty dictionary

for i in words:
    q = i.strip("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{}|~")
    if dictionary.get(q):
        dictionary[q] += 1
    else:
        dictionary[q] = 1


index_dictionary = {}

    
for word, frequency in dictionary.iteritems():
    # if the value of the pair from dictionary exists as a key in index_dictionary
    if index_dictionary.get(frequency):
        # append word to frequency
        index_dictionary[frequency].append(word) 
    else:  
        # add new frequency/word as a list
        index_dictionary[frequency] = [word]

for key in reversed(sorted(index_dictionary.keys())):
    print "%r: %r" % (key, sorted(index_dictionary[key]))
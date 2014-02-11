
twain = open("twain.txt")

text = twain.read() # gives a giant string

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

# for k, v in dictionary.iteritems():
#     print k, v 

#key = []

#for key in sorted(dictionary.iterkeys()):
#    print "%r: %r" % (key, dictionary[key])

index_dictionary = {}

#for key, value in dictionary.iteritems():
    #index_dictionary[value] = [key]
    
for word, frequency in dictionary.iteritems():

    #index_dictionary[value] = [key]
    # if the value of the pair from dictionary exists as a key in index_dictionary
    if index_dictionary.get(frequency):
        # append word to frequency
        index_dictionary[frequency].append(word) 
    else:  
        # add new frequency/word as a list
        index_dictionary[frequency] = [word]
#for k, v in index_dictionary.iteritems():
#     print k, v 

# sorted_dict = sorted(index_dictionary)  # creates a list of the frequencies, in order
# sorted_dict 
for key in sorted(index_dictionary.keys()):
    print "%r: %r" % (key, sorted(index_dictionary[key]))

#sorted_dict = sorted(index_dictionary)
#print sorted_dict

#sorted_key = key.sort()
#print sorted_key

#sorted_dict = sorted(dictionary, key=dictionary.get)

twain.close()
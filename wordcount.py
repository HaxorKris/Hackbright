
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

for key in sorted(dictionary.iterkeys()):
    print "%r: %r" % (key, dictionary[key])

index_dictionary = {}

for key, value in dictionary.iteritems():
    index_dictionary[value] = [key]
    
for key, value in index_dictionary.iteritems():
    print key, value

    #key.append(k)

#print key

#sorted_key = key.sort()
#print sorted_key

#sorted_dict = sorted(dictionary, key=dictionary.get)

twain.close()
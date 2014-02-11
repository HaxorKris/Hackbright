
twain = open("twain.txt")

text = twain.read() # gives a giant string

lower_case = text.lower()
#stripped_words = lower_case.strip(",")
# "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{}|~"
words = lower_case.split()

# words = split_words.lower()
# print words

dictionary = {}  # start an empty dictionary

for k in words:
    q = k.strip("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{}|~")
    if dictionary.get(q):
        dictionary[q] += 1
    else:
        dictionary[q] = 1
print dictionary
    


twain.close()
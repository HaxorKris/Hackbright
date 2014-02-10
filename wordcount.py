
twain = open("twain.txt")

text = twain.read() # gives a giant string
words = text.split()
#print words

dictionary = {}  # start an empty dictionary

for k in words:
    if dictionary.get(k):
        dictionary[k] += 1
    else:
        dictionary[k] = 1
print dictionary
    


twain.close()
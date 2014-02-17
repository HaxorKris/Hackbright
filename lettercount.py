f = open("twain.txt")
filecopy = f.read(1)
f.close()

file_lowercase = filecopy.lower()

for char in file_lowercase:
	if char == 'a':
		tally += 1
	print tally


# maintain a tally for every letter

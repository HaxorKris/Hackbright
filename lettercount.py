f = open("twain.txt")
filecopy = f.read()
f.close()

file_lowercase = filecopy.lower()

running_total = [0] * 26    # sets a list of 26 0's, covered in class

for char in file_lowercase:
	if char.isalpha():
#		if char == 'a':
#			running_total[0] += 1
#		elif char == 'b':
#			running_total[1] += 1

print running_total


# maintain a tally for every letter

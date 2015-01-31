f = open("twain.txt")
filecopy = f.read()
f.close()

file_lowercase = filecopy.lower()

running_total = [0] * 26    # sets a list of 26 0's, covered in class

for char in file_lowercase:
	if char.isalpha():
		running_total[ord(char)-97] += 1

for i in running_total:
	print i
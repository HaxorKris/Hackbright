calculation = ["temp"]

print " "
print "         Ex03 Calculator"
print " "
print "The following functions are supported:"
print "======================================"
print "     addition (+ num1 num2)"
print "     subtraction (- num1 num2)"
print "     multiplication (* num1 num2)"
print "     division (/ num1 num2)"
print "     square root (square num1)"
print "     cube root (cube num1)"
print "     exponent (pow num1 num2)"
print "     modulo (mod num1 num2)"
print "========= type 'q' to quit =========="
print "  "

while calculation[0] != "q":
	
	user_input = raw_input("Calculator > ")   # prompt the user 
	calculation = user_input.split(" ")   # split the single string into 3 elements
	
	print calculation[0]
	print calculation[1] # checkpoint charlie -- does my string split work?
	
	print "Calculating . . ."
	
	if calculation[0] == "+":
		print "You are adding"
	elif calculation[0] == "-":
		print "You are subtracting"
	elif calculation[0] == "*":
		print "You are multiplying"
	elif calculation[0] == "/":
		print "You are dividing"
	elif calculation[0] == "square":
		print "You are squaring"
	elif calculation[0] == "cube":
		print "You are cubing"
	elif calculation[0] == "pow":
		print "You are exponentiating"
	elif calculation[0] == "mod":
		print "You seek a remainder"
	else:
		print "This is not a valid option, please use the format: "
		print "         'type num1 num2' e.g. '+ 1 2'"


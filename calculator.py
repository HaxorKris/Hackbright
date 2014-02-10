# This program assumes the user will pass valid numbers to arithmetic.py

from arithmetic import *

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
	
	print "debug= " + calculation[0] # checkpoint charlie -- does my string split work?
#	print "debug= " + calculation[1] 
	
	print "Calculating . . ."
	
	if calculation[0] == "+":
		print add(calculation[1], calculation[2])
		print "debug= " + "You are adding"
	elif calculation[0] == "-":
		print subtract(calculation[1], calculation[2])
		"debug= " + "You are subtracting"
	elif calculation[0] == "*":
		print multiply(calculation[1], calculation[2])
		print "debug= " + "You are multiplying"
	elif calculation[0] == "/":
		print divide(calculation[1], calculation[2])
		print "debug= " + "You are dividing"
	elif calculation[0] == "square":
		print square(calculation[1])
		print "debug= " + "You are squaring"
	elif calculation[0] == "cube":
		print cube(calculation[1])
		print "debug= " + "You are cubing"
	elif calculation[0] == "pow":
		print power(calculation[1], calculation[2])
		print "debug= " + "You are exponentiating"
	elif calculation[0] == "mod":
		print mod(calculation[1], calculation[2])
		print "debug= " + "You seek a remainder"
	elif calculation[0] == "q":
		print "Thank you, goodbye!"
	else:
		print "This is not a valid option, please use the format: "
		print "         'type num1 num2' e.g. '+ 1 2'"


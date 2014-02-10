
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

user_input = raw_input("Calculator > ")   # prompt the user 
calculation = user_input.split(" ")   # split the single string into 3 elements
print calculation[0]
print calculation[1] # checkpoint charlie -- does my string split work?
print calculation[2]

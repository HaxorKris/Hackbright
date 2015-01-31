from sys import argv

#open the file
script, filename = argv
txt = open(filename)

#read the file
myfile = txt.read()
#print myfile

#close the file
txt.close()

#provide them with a menu of options
print "Welcome to the restaurant search"
print "You have 2 options:"
print "1. Get an alphabetical list of restaurants"
print "2. Get a list of restaurants by rating, in descending order"
print "(type 'q' to quit)"

d = {}
for line in sorted(myfile.split("\n")):
    #split the line by the colon
        split_value = line.split(":")
        x = type(split_value)
        print x
        #print split_value
        # for dictionary 'd' set d[0] to restaurant name, d[1] to rating
        for restaurant,rating in split_value:
            if d.get(rating):
                d[rating].append(restaurant)
            else:
                d[rating] = [restaurant]

        #d[split_value[1]] = split_value[0]
        #print d
        #print "Restaurant %r is rated at %d" % (split_value[0], int(split_value[1]))
#print d

#options:
while True:
    selection = raw_input(" Your selection:  ")
    #1)list of restuarants and ratings in alpha order
    if selection == '1':
        #split the file line by line
        #and sort it by alpha
        for line in sorted(myfile.split("\n")):
        #split the line by the colon
            split_value = line.split(":")
            print "Restaurant %r is rated at %d" % (split_value[0], int(split_value[1]))
    elif selection == '2':

    #2)list of restuarants by rating in descending order
        for restaurant in sorted(d.keys(),reverse=True):
            print "%r: %r" % (restaurant, d[restaurant])

    #3)TODO: search feature - have user put in restaurant name and
    # the program will print restuarant and rating to the user 
    #4) TODO: search feature - have user put in a rating and
    # the program will print all restuarants with that rating to the user 
    #5)option to quit program    
    elif selection == 'q':
        print "Thanks! Have a great day!"
        break
    else:
        print "I do not understand that option. Please type '1', '2' or 'q'"




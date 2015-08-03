#creates a list called 10 things and puts 1 long string in it
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#creates list 'stuff' and splits the above long string into individula
#string elements, separated by ''
stuff = ten_things.split(' ')
#creates a new list with some more string elements in it, called more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#this is a while loop, while the length of list stuff is not 10 it will
#create a new object, next_one. the loop goes through the list more stuff and
#pops off each element, temporarily storing each one as next_one (which can
#only have 1 thing at a time in it). then it prints the name of the thing
#currently stored in next_one, and appends it to the list stuff. then it prints
#a running count of the length of list stuff, until it reaches 10.
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

#just prints everything in 'stuff'
print "There we go: ", stuff

print "Let's do some things with stuff."

#second element
print stuff[1]
#last element
print stuff [-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

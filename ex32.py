#creates a list called the count which contains 5 elements
the_count = [1, 2, 3, 4, 5]
#create a list called fruits that contains 4 elements
fruits = ['apples', 'oranges', 'pears', 'apricots']
#creates a list called change that contains 6 elements, both string & numeric
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for_loop goes through a list
for number in the_count:
    print "This is cound %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
#notice also that i can stand in for each element in change - above, fruit and
#number were working the same way, they weren't defined. IMPORTANT that fruit,
#i, and number is a var that temporarily stores whatever element is going thru
#the loop. If you type print fruit at the end of this program, it will contain
#only the last element passed to it.
for i in change:
    print "I got %r" % i

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range (0, 6):
    print "Adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print "Element was: %d" % i

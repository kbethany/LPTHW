#create new function, cheese_and_crackers, which has two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#the function has four things inside it contains, 4 print statements
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
#prints the functino where 20 and 30 map to first and second variables
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
#gives amount of cheese and amount of crackers a permanent value - before
#their values were assigned at the end of the line
amount_of_cheese = 10
amount_of_crackers = 50
#fYI: This puts something new in the function! instead of cheese_count and
#boxes_of_crackers, it contains amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#now we are assigning new values to cheese and crackers, but these just work
#for this one command. the 10 and 50 are still there lurking.
print "We can even do math inside, too:"
cheese_and_crackers(10 + 20, 5 + 6)

#that's why when we call up this last command, it still thinks cheese is 10
#and crackers is 50, and therefore says we have 110 cheese and 1050 crackers.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

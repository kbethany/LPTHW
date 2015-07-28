#create new function, cheese_and_crackers, which has two variables
def pets(cat_count, dog_count):
#the function has four things inside it contains, 4 print statements
    print "You have %d cat!" % cat_count
    print "You have %d dog!" % dog_count
    print "Man, those are hungry pets!"
    print "Give them a boost!\n"

print "We can just give the function numbers directly:"
#prints the functino where 20 and 30 map to first and second variables
pets(1, 1)

print "OR, we can use variables from our script:"

amount_of_cat = 1
amount_of_dog = 5

pets(amount_of_cat, amount_of_dog)

print "We can even do math inside, too:"
pets(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
pets(amount_of_cat + 100, amount_of_dog + 1000)

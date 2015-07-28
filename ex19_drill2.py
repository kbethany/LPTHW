#create new function, cheese_and_crackers, which has two variables
# def pets(pet1, pet2):
#the function has four things inside it contains, 4 print statements
prompt = '> '

print "What is your first pet's name?"
pet1 = raw_input(prompt)
print "How many %rs do you have?" % pet1
pet1n = raw_input(prompt)

print "What is your second pet's name?"
pet2 = raw_input(prompt)
print "How many %rs do you have?" % pet2
pet2n = raw_input(prompt)

print "Alright, so you have %r %r and %r %r." % (pet1n, pet1, pet2n, pet2)

print "Man, those are hungry pets!"
print "Give them a boost!\n"

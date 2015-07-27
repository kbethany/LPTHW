# create var x that is a string, with a number, %d, that is set to 10
x = "There are %d types of people." % 10
#creates var binary set to string "binary"
binary = "binary"
#same
do_not = "don't"
#creates var y that is a string with 2 format characters that reference other already-made string vars, binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r is set to what x is
print "I said: %r" % x
# %s is set to what y is
print "I also said: '%s'." % y

#sets hilarious as equal to false
hilarious = False

#not sure what % r does here
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
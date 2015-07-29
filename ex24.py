print "Let's practice everything."
#escape sequences within strings so things will print normally
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#creates var poem which contains the following string. The triple double quotes
#print exactly as typed, with the exception of \n and \t which create a new
#line and a tab, respectively
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

#creates new var five which contains a simple math problem
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#defines new function, secret formuala that calls one argument, started
#started is not set to anything, but it CAN be set with something, as seen in
#exercise 21, with a & b. REMEMBER that this little block doesn't print or
#produce anything yet -- it just sets up the arguments of secret_formula. There
#is one argument, started, that contains all the below. BUT started can be
#replaced with something else. We see below started will be replaced with
#start point.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#IMPORTANT! See how now we're just using beans instead of jellybeans like it
#ain't a thing? That's allowed because we saw about that secret_formula is the
#function that holds 1 argument, which holds 3 things. Those things can change,
#and they do as we see below. And the argument can change too. The names are
#not that important and we can change them however we want.
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#We assigned value to beans, jars, and crates using the function, so it should
#go ahead and do the calculations in the function and print the results.
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#this is a kinda crazy thing, just writing over a variable and calling it by
#the same name!
start_point = start_point / 10

#recalculating using same function, with the newly-adjusted start_point. Numbers
#should be different.
print "We can also do it this way:"
print "We'd have %d beans, %d jars, and %d crates." % (secret_formula(start_point))

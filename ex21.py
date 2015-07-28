#this top part just creates and defines all of the functions
#nothing else exciting is happening here. the functions will be used for
#something below
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

#now we're using the functions we made above
print "Next up!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age, %d, Height, %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
answer = -4391
print "I think it's %d." % answer

#bkc - Just playing around with raw inputs
prompt = '> '
print "What is your age?"
age = float(raw_input(prompt))
print "So your age is %d." % age

print "What is your weight?"
weight = float(raw_input(prompt))
print "So your weight is %d." % weight

print "Your age plus your weight is %d!" % (age + weight)

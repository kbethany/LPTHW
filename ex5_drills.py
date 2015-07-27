name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
in_to_cm = 2.54
lbs_to_kilos = 0.453592
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "In centimeters, he is %d centimeters tall." % (height * in_to_cm)
print "He's %d pounds heavy." % weight
print "In kilos, he is %d kilograms." % (weight * lbs_to_kilos)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
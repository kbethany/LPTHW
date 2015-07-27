#sys is a package, argv says to import only the vars listed
#when you call up the program (ex15.py filename), where argv is any
#module i want retrieved from that package.
from sys import argv
#argv is the arguments vector which contains the arguments passed
#to the program.
script, filename = argv
#opens the filnemae listed above
txt = open(filename)
#prints the name of the file as defined above
print " Here's your file %r:" % filename
#prints everything inside the text file
print txt.read() #calls a function on txt named 'read'

print "Type the filename again:"
#prompts the user to input the filename again (see print command above)
#and sets what she enters to file_again
file_again = raw_input("> ")
#function that opens the text of file_again and sets the whole text
#as txt_again
txt_again = open(file_again)
#function that prints everything in txt_again without modification
print txt_again.read()

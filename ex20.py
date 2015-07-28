from sys import argv

script, input_file = argv

#creates a function called print_all, which contains f, which i now know is
#a variable name or can also be a file. the function's job is assigned on the
#next line, which is to read in f and print the contents of f.
def print_all(f):
    print f.read()

#creates another function: rewind(f), which contains f, and the job of this
#function is to seek the first byte in file f.
def rewind(f):
    f.seek(0)

#another function: print_a_line which contains line_count and f. weirdly,
#line_count is not really defined anywhere? and then readline is a module that
#i think lets python read what lines of a file.
#from LPTHW: Inside readline() is code that scans each byte of the file until
# it finds a \n character, then stops reading the file to return what it found
#so far. The file f is responsible for maintaining the current position in the
#file after each readline() call, so that it will keep reading each line.
def print_a_line(line_count, f):
    print line_count, f.readline()

#opens the input file and sets that file = to object current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

#print_all is a function we defined at the beginning. the file to print is the
#current file, input_file, which is actually test.txt (see line 3)
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#now we take the test.txt file and return to the 0th byte.
rewind(current_file)

print "Let's print three lines:"

#remember that in function print_a_line we have f.readline() which is what is
#reading all of these lines. See the note about readline on line 19. So all
#this does is set current line to 1, then runs the print a line function, which
#has 2 arguments, here, they are to print the current line and the current
#file - but don't totally understand why it stops after the end of the line.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

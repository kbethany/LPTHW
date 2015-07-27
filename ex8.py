#creates variable formatter and sets it to an as-of-yet-unnamed series of 4 strings
formatter = "%r %r %r %r"

#sets the 4 strings that formatter are made of as 1, 2, 3, 4, and prints the values
print formatter % (1, 2, 3, 4)

#sets the 4 strings that formatter are made of as one, two, three, four, and prints the values
print formatter % ("one", "two", "three", "four")

#same
print formatter % (True, False, False, True)

#sets the 4 strings that formatter are made of as itself, and because we use %r it will print it literally. I think if I used %string it would not. 
#note: wrong! if I use %s it just prints %s sixteen times.
print formatter % (formatter, formatter, formatter, formatter)

#notice how what is important is that there are four things
print formatter % (
	"I had this thing.",
	"that you could type up right.",
	"But it didn't sign.",
	"So I said goodnight."
)

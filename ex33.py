#sets i equal to 0
i = 0
#creates an empty list called numbers
numbers = []

#a loop that begins at 0 and goes while i is less than 6. it prints the number
#and appends them together, i think.
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

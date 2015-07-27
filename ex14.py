from sys import argv

script, user_name, inlove = argv #have to include my name when i call up this script

prompt = '> '

print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like %s, %s?" % (inlove, user_name)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking %s.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, inlove, lives, computer)

a = True and True
print "a = %s" % a
b = False and True
print "b = %s" % b
c = 1 == 1 and 2 == 1
print "c = %s" % c
d = "test" == "test"
print "d = %s" % d
e = 1 ==1 and 2 != 1
print "e = %s" % e
f = True and 1 == 1
print "f = %s" % f
g = False and 0 != 0
print "g = %s" % g
h = True or 1 == 1
print "h = %s" % h
i = "test" == "testing"
print "i = %s" % i
j = 1 != 0 and 2 == 1
print "j = %s" % j
k = "test" != "testing"
print "k = %s" % k
l = "test" == 1
print "l = %s" % l
m = not(True and False)
print "m = %s" % m
n = not(1 == 1 and 0 != 1)
print "n = %s" % n
o = not(10 == 1 or 1000 == 1000) # watch the OR
print "o = %s" % o
p = not(1 != 10 or 3 == 4)
print "p = %s" % p
q = not("testing" == "testing" and "Zed" == "Cool Guy")
print "q = %s" % q
r = 1 == 1 and (not ("testing" == 1 or 1 ==0))
print "r = %s" % r
s = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print "s = %s" % s
t = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
print "t = %s" % t

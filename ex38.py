ten = "a o c t l s"
print "a"
stuff = ten.split(' ')
mor = ["d", "n", "s", "f", "corn", "b", "g", "b"]
while len(stuff) != 10:
    nxt = mor.pop()
    print "a the chimpanzee: ", nxt
    stuff.append(nxt)
    print "There's %d items now" %len(stuff)
print "Bettr ", stuff
print "Let's a b up"
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

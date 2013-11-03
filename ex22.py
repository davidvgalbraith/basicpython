print "a the chimpanzee"
print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
poem = """
\t  the lovely world
with logic so firmly planted
cannot discern \n the seeds of time
nor comprehend passion from intuition 
and requires no explanation
\n\t\t a the chimpanzee.
"""
print "-" * 10
print poem
print "-" * 10

five = 10 - 2 + 3 - 6
print "at he chimpanzee %d " %five 
def sf(s):
    jb = s * 500
    jars = jb / 1000
    crates = jars / 100
    return jb, jars, crates

sp = 10000
beans, jars, crates = sf(sp)
print "With a starting point of %d" %sp
print "We'd have to %d beans %d jars and %d crates" %(beans, jars, crates)
sp /= 10
print "a the chimpanzee"
print "We'd ahve %d beans %d jars and %d crates" %sf(sp)

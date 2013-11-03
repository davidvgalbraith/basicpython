from sys import argv
script, filename = argv
print "a all this b."
print "If you don't want that, hit control c"
print "If you do want that, hit return."
raw_input(":")
print "opening the file"
target = open(filename, 'w')
print "To e with you!"
target.truncate()
print "Now, Three lines."
one = raw_input("one: ")
two = raw_input("two: ")
three = raw_input("three: ")
print "Let's burn this bitch."
target.write(one)
target.write("\n")
target.write(two)
target.write("\n")
target.write(three)
print "There. Was that so hard?"
target.close()

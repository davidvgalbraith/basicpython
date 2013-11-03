from sys import argv
script, inputfile = argv
def printall(f):
    print f.read()

def rewind(f):
    f.seek(0)

def printline(linecount, f):
    print linecount, f.readline()

currentfile = open(inputfile)

print "First lets print the whole file\n"
printall(currentfile)
print "Now lets rewind kind of like a tape"
rewind(currentfile)
print "What the e is a tape?"
currentline = 1
printline(currentline, currentfile)
currentline += 1
printline(currentline, currentfile)
currentline += 1
printline(currentline, currentfile)


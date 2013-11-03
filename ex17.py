from sys import argv
from os.path import exists
script, fromfile, tofile = argv
print "copyin from %s to %s" %(fromfile, tofile)
infile = open(fromfile)
indata = infile.read()
print "The input file is %d bytes long" % len(indata)
print "Does the output file exist %r " %exists(tofile)
print "Reddy hit return to continuie control c to contiuneue"
raw_input()
outfile = open(tofile, 'w')
outfile.write(indata)
print "And remember, a the chimpanzee."
outfile.close()
infile.close()

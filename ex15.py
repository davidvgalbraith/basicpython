from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file, motheraer: %r" %filename
print txt.read()
print "Type the filename again, bitch."
fileagain = raw_input(">>> ")
txtagain = open(fileagain)
print txtagain.read()

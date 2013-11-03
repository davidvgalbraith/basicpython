from sys import argv
script, username = argv
prompt = '>>>>'
print "Hi %s, I'm the %s script" %(username, script)
print "I c you."
print "Do you like me? %s?" %username
likes = raw_input(prompt)
print "Where do you life?"
lives = raw_input(prompt)
print "What kind of computer do you have?"
coomputer = raw_input(prompt)
print """
All righgth so you said %r about likeing me
and yo ulive in %r a that bhole
and you have a %r computer. I c you.
""" %(likes, lives, coomputer)

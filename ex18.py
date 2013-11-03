def printwo(*args):
    arg1, arg2 = args
    print "arg1 = %r, arg2 = %r" %(arg1, arg2)

def printwogain(arg1, arg2):
    print "arg1 = %r, arg2 = %r" %(arg1, arg2)
    
def printone(arg1):
    print "arg1: %r" %arg1
    
def printnone():
    print "a the chimpanzee."

printwo("a the", "chimpanzee")
printwogain("This b", "is bananas")
printone("CHYEAH")
printnone()

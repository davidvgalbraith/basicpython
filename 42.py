from sys import exit
from sys import randint

class Game(object):

    def __init__(self, start):
        self.quips = ["You died, you a the chimpanzee.", "Your mom would be proud if you a the chimpanzee", "Such a bannaa", "I have a small puppy who will kill ya"]
        self.start = start

    def play(self):
        nextroom = self.start
        while True:
            print "\n-----------------"
            room = getattr(self, nextroom)
            nextroom = room()
            
        
    def deth(self):
        print self.quips[randint(0, len(self.quips) - 1)]
        exit(1)

    def cc(self):
        print "a the chimpanzee!!!1"
        action = raw_input("? ")
        if action == "shoot":
            print "oopps"
            return 'death'
        elif action == 'ok':
            return 'lwa'
        else:
            print "a THE chimpanzee!!"
            return 'cc'
print "a THE chimpanzee!!!"

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing(self):
        for line in self.lyrics:
            print line

hb = Song(["Happy birthday to you", "You live in a shoe", "a the chimpanzee"])
bop = Song(["They rally around the family", "a the chimpanzee"])
hb.sing()
bop.sing()

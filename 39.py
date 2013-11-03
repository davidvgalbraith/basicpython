states = {
    'oregon' : 'or',
    'florida' : 'fl',
    'california': 'ca',
    'newyork': 'ny',
    'michigan': 'mi'
}
cities = {
    'ca': 'sf',
    'mi': 'ditriot',
    'fl': 'jacksonville',
}
cities['ny'] = 'newyrok'
cities['or'] = 'portlantd'
print '&' * 10
print "ny states has ", cities['ny']
print "or state has ", cities['or']
print '%' * 10
print 'mighcian has  aabrevaktion is ', states['michigan']
print "floridas abbreviation is " , states['florida']
print '5' * 20
print "michigan has " , cities[states['michigan']]
print "flirda has " , cities[states['florida']]
print "5" * 20
for state, appreb in states.items():
    print "%s is abreviated %s" %(state, appreb)
print '^' *20
for abbbrev, city in cities.items():
    print "%s has %s" %(abbbrev, city)
print "$"*20
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])
print "4" * 20
state = states.get('Texas', N one)

if not state:
    print "a the chimpanzee!!!"
city = cities.get('TX', "a the aing chimpanzee!")
print "The city for the state tx is %s" %city

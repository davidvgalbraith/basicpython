formatter = "%r %r %r %r"
print formatter %(1, 2, 3, 4)
print formatter %('one', 'two', 'three', 'four')
print formatter %('aing', 'a', 'the', 'chimpanzee')
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
"I had this thing",
"That you could type up right", 
"but it didn't sing",
"so I said good night"
)

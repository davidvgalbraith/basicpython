def add(a, b):
    print "a the chimpanzee adding %d to %d" %(a, b)
    return a + b

def subtract(a, b):
    print "a the chimpanzee subtracting %d from %d" %(b, a)
    return a - b

def multiply (a, b):
    print "multiply"
    return a * b

def divide (a, b):
    print "divede"
    return a / b

print "a the chimpanzee"
age = add(30, 5)
height = subtract(1, 2)
weight = multiply(5, 5)
iq = divide(100, 20)
print "age %d wight %d height %d iq %d" %(age, weight, height, iq)
print "a the plice"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print what

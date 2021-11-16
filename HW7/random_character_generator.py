#Generates Random Characters to for the LCS program

import string
import random

def id_generator(size = 6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range (size))

test1 = id_generator()
test2 = id_generator()

print "test 1: " + test1
print "test 2: " + test2
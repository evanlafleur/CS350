#Longest Common Subsequence

#  J F A Y P U
#J * . . . . .
#W . . . . . .
#G . . . . . .
#L . . . . . .
#Y . . . * . . 
#U . . . . . *
#LCS = 3

import time
import string
import random

#Brute Force Implementation
def bf_lcs(array1, array2, m, n):
    if(m == 0 or n == 0):
        return 0;
    elif(array1[m-1] == array2[n-1]):
        return 1 + bf_lcs(array1, array2, m-1, n-1);
    else:
        return max(bf_lcs(array1, array2, m, n-1), bf_lcs(array1, array2, m-1, n));

def dyn_lcs(array1, array2):
    m = len(array1)
    n = len(array2)

    #Stores the array so that we do not repeat the same algorith on the specific pattern
    #more than once

    #Using bottom up method to determine value
    #tmp_store contains the length of the following...
    # X[0 -> i-1] & Y[0 -> j-1]

    tmp_store = [[None] * (n+1) for i in xrange(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if (i == 0 or j == 0):
                tmp_store[i][j] = 0
            elif (array1[i-1] == array2[j-1]):
                tmp_store[i][j] = tmp_store[i-1][j-1]+1
            else:
                tmp_store[i][j] = max(tmp_store[i-1][j], tmp_store[i][j-1])
    return tmp_store[m][n]

        
def id_generator(size = 6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range (size))

def average(array):
    return (sum(array) / len(array))



print " --------- Base Tests: ----------"
X = "AGGTAB"
Y = "GXTXAYB"
bf_start = time.time()
bf_count = bf_lcs(X, Y, len(X), len(Y))
bf_end = time.time()
print "Test: ", bf_count, "| Time cost: ", bf_end-bf_start

dyn_start = time.time()
dyn_count = dyn_lcs(X, Y)
dyn_end = time.time()
print "Dyn Test: ", dyn_count, "| Time cost: ", dyn_end-dyn_start

test_cases = 5000
print "-------- Extensive Tests: -------"
print "Tests Run: ", test_cases
bf_results = []
dyn_results = []
for i in range(test_cases):
    stringA = id_generator()
    stringB = id_generator()

    bf_start = time.time()
    bf_test = bf_lcs(stringA, stringB, len(stringA), len(stringB))
    bf_end = time.time()
    bf_duration = bf_end - bf_start
    bf_results.append(bf_duration)

    dyn_start = time.time()
    dyn_test = dyn_lcs(stringA, stringB)
    dyn_end = time.time()
    dyn_duration = dyn_end - dyn_start
    dyn_results.append(dyn_duration)

print "Brute Force Average Time Cost: ", average(bf_results), " milliseconds"
print "Dynamic Average Time Cost: ", average(dyn_results), " milliseconds"





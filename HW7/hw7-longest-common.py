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
from random import randrange

#Brute Force Implementation
def bf_lcs(array1, array2, m, n):
    table = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Building the mtrix in bottom-up way
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif array1[i - 1] == array2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    index = table[m][n]

    lcs_array = [""] * (index + 1)
    lcs_array[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if array1[i - 1] == array2[j - 1]:
            lcs_array[index - 1] = array1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return (len(lcs_array) - 1)

def dyn_lcs(array1, array2):
    m = len(array1)
    n = len(array2)

    #Stores the array so that we do not repeat the same algorith on the specific pattern
    #more than once

    #Using bottom up method to determine value
    #tmp_store contains the length of the following...
    # X[0 -> i-1] & Y[0 -> j-1]

    tmp_store = [[None] * (n+1) for i in range(m+1)]

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



print(" --------- Base Tests: ----------")
X = input("Enter original String: ")
Y = input("Enter new String: ")
bf_start = time.time()
bf_count = bf_lcs(X, Y, len(X), len(Y))
bf_end = time.time()
print("Brute Force Test LCS Length: ", bf_count, "|\nTime cost: ",
      bf_end - bf_start)

dyn_start = time.time()
dyn_count = dyn_lcs(X, Y)
dyn_end = time.time()
print("Dyn Test: ", dyn_count, "| Time cost: ", dyn_end-dyn_start)

test_cases = 5000
print("-------- Extensive Tests: -------")
print("Tests Run: ", test_cases)
bf_results = []
dyn_results = []
for i in range(test_cases):
    size = randrange(2, 50)
    stringA = id_generator(size)
    size = randrange(1, len(stringA))
    stringB = id_generator(size)

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

print("Brute Force Average Time Cost:\n",
      average(bf_results),
      " milliseconds",
      sep="")
print("Dynamic Average Time Cost:\n",
      average(dyn_results),
      " milliseconds",
      sep="")
print("------------ Example: -----------")
print("String A: ", stringA, "\nLength: ", len(stringA), sep="")
print("String B:", stringB, "\nLength: ", len(stringB))
print("LCS Length:", dyn_test)
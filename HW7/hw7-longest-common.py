#Longest Common Subsequence

#  J F A Y P U
#J * . . . . .
#W . . . . . .
#G . . . . . .
#L . . . . . .
#Y . . . * . . 
#U . . . . . *
#LCS = 3

from datetime import datetime


#Brute Force Implementation
def bf_lcs(X, Y, m, n):
    if(m == 0 or n == 0):
        return 0;
    elif(X[m-1] == Y[n-1]):
        return 1 + bf_lcs(X, Y, m-1, n-1);
    else:
        return max(bf_lcs(X, Y, m, n-1), bf_lcs(X, Y, m-1, n));

def dyn_lcs(X, Y):
    m = len(X)
    n = len(Y)

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
            elif (X[i-1] == Y[j-1]):
                tmp_store[i][j] = tmp_store[i-1][j-1]+1
            else:
                tmp_store[i][j] = max(tmp_store[i-1][j], tmp_store[i][j-1])
    return tmp_store[m][n]

        


print " --------- Base Tests: ----------"
X = "AGGTAB"
Y = "GXTXAYB"
bf_start = datetime.now()
bf_count = bf_lcs(X, Y, len(X), len(Y))
bf_end = datetime.now()
print "Test: ", bf_count, "| Time cost: ", bf_end-bf_start

dyn_start = datetime.now()
dyn_count = dyn_lcs(X, Y)
dyn_end = datetime.now()
print "Dyn Test: ", dyn_count, "| Time cost: ", dyn_end-dyn_start
#rod cutting for homework 6
#Time complexity is around O(n^2)
import sys


#Rod-Cutting Algorith to determine max value/profit of a specifc cut size and price
def rod_algorithm(price, n):
    value = [0 for x in range(n+1)]
    value[0] = 0

    #Tabulates Data from the bottom up
    #Avoided recomputations of specific locations by using the temp array 'val[]'
    for i in range(1, n+1):
        max_val = -sys.maxsize
        for j in range(i):
            max_val = max(max_val, price[j] + value[i-j-1])
        value[i] = max_val
    return value[n]

#Collects input from the user for both the price and the size of rod cuts
def get_input():
    list = []
    n = int(input("How many prices are going to be tested: "))
    for i in range(0, n):
        element = int(input())
        list.append(element)
    rod_len = int(input("What is the rod length?"))
    return list, rod_len


#Runs program and implements the get input function to collect values from client 
a,b = get_input()
print("Max Val: "+ str(rod_algorithm(a,b)))

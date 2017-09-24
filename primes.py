#!/usr/bin/env python3

###
# Name: Evan A Walker, Kristaaaa, Ehsan
# Student ID: 01932978 , kristaIDHere, EhsanIDHere
# Email: walke208@mail.chapman.edu , kristaEmailHere , ehsanEmailHere
# Course: CS510 Fall 2017
# Assignment: Classwork 4
###


import sys


def eratosthenes(n):
    """
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        prime_list (list): a list of all prime numbers less than or equal to n
    """
    assert n>1                                       #asserting n be a positive integer
    prime_list = []
    for i in range(2,n+1):                             #fills prime_list with all integers  2 <= i <= n
        prime_list.append(i)
    multiple = 2                                     #set to 2 because if set to 1 it will remove all elements from the list
    while multiple <= n/multiple:
        count = 2                                    #set to 2 because if set to 1 it will remove the prime itself from the list
        while count <= n/multiple:
            if count*multiple in prime_list:         #checks if count*multiple is in list. needed because it could have already been removed
                prime_list.remove(count*multiple)    #removes count*multiple
            count = count + 1
        multiple = multiple + 1
    #print(prime_list)   for testing only
    return prime_list


def gen_eratosthenes():
    """
    Args:
        none
    Yields:
        n (int): where n is the next prime
    """
    n=3
    yield 2
    while True:
        count = 2               #set count to 2 because all numbers are divisible by 1, so it is not a case we need to check
        while count < n:
            if n%count == 0:    #i.e. if n is divisble by count, then n is not prime
                count = n       #ends this loop; if n is not prime, there is no reason to continur the loop
            count += 1
        if count == n:          #i.e. if count == n, then we know that the while loop was completely executed and n has no divisors except 1 and n
            yield n             #yield n since it went through the entire loop without finding divisors
        n += 1                  #increment n to see if n+1 is prime. will continue incrimenting until another prime is found and yields it

def genPrimes(n):
    """
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        prime_list (list): a list of all prime numbers less than or equal to n utilizing a generating fxn
    """
    assert n>1
    p = gen_eratosthenes()
    prime_list = []
    prime_list.append(next(p))
    while n > prime_list[len(prime_list)-1]:        #while input is less than the last term in the prime list
        prime_list.append(next(p))                  #adds next term from generator
    if n < prime_list[len(prime_list)-1]:          #deletes last term
        del prime_list[len(prime_list)-1]
    #print(prime_list)  for testing only
    return prime_list


if __name__ == "__main__":
    import sys
    eratosthenes(int(sys.argv[1]))
    #genPrimes(int(sys.argv[1]))
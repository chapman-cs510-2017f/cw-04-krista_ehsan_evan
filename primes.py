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
        prime_list (list): a list of all prime numbers strictly less than n
    """
    assert n>1
    prime_list = []
    for i in range(2,n):
        prime_list.append(i)
    multiple = 2
    while multiple <= n/multiple:
        count = 2
        while count <= n/multiple:
            if count*multiple in prime_list:
                prime_list.remove(count*multiple)
            count = count + 1
        multiple = multiple + 1
    #print(prime_list)
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
        count = 2
        while count < n:
            if n%count == 0:
                count = n
            count += 1
        if count == n:
            yield n
        n += 1

def genEratosthenes(n):
    """
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        prime_list (list): a list of all prime numbers strictly less than n utilizing a generating fxn
    """
    assert n>1
    p = gen_eratosthenes()
    prime_list = []
    prime_list.append(next(p))
    while n > prime_list[len(prime_list)-1]:        #while input is less than the last term in the prime list
        prime_list.append(next(p))                  #adds next term from generator
    if n <= prime_list[len(prime_list)-1]:          #deletes last term
        del prime_list[len(prime_list)-1]
    #print(prime_list)
    return prime_list

eratosthenes(20)
genEratosthenes(20)

if __name__ == "__main__":
    import sys
    eratosthenes(int(sys.argv[1]))

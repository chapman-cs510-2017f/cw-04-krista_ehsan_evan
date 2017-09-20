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
        prime_list (list): a list of all prime numbers less than n
    """
    assert n>1
    prime_list = []
    for i in range(n):
        prime_list.append(i)
    prime_list.remove(0)
    prime_list.remove(1)
    multiple = 2
    while multiple <= n/multiple:
        count = 2
        while count <= n/multiple:
            if count*multiple in my_list:
                prime_list.remove(count*multiple)
            count = count + 1
        multiple = multiple + 1
    #print(prime_list)
    return prime_list




eratosthenes(1)

#def gen_eratosthenes():







#if __name__ == "__main__":
#    import sys
#    eratosthenes(int(sys.argv[1]))


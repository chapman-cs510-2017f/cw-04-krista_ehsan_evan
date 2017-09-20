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
    assert n>1
    my_list = []
    for i in range(n):
        my_list.append(i)
    my_list.remove(0)
    my_list.remove(1)
    multiple = 2
    while multiple <= n/multiple:
        count = 2
        while count <= n/multiple:
            if count*multiple in my_list:
                my_list.remove(count*multiple)
            count = count + 1
        multiple = multiple + 1
    #print(my_list)
    return my_list




eratosthenes(120)

def gen_eratosthenes():







if __name__ == "__main__":
    import sys
    eratosthenes(int(sys.argv[1]))


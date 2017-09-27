#!/usr/bin/env python3
import primes
###
# Name: Evan A Walker, Kristaaaa, Ehsan
# Student ID: 01932978 , kristaIDHere, EhsanID: 2285887
# Email: walke208@mail.chapman.edu , kristaEmailHere , ehsanEmailHere
# Course: CS510 Fall 2017
# Assignment: Classwork 4
###


import sys

def test_primes():
    result = primes.eratosthenes(10)
    correct = [2,3,5,7]
    assert result == correct

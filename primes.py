#!/usr/bin/env python3
#.remove(n)
import sys


def eratosthenes(n):
    try:
        my_list = []
        for i in range(n):
            my_list.append(i)
        my_list.remove(0)
        my_list.remove(1)
        multiple = 2
        while multiple <= n:
            count = 2
            while count <= n/multiple:
                if count*multiple in my_list:
                    my_list.remove(count*multiple)
                count = count + 1
            multiple = multiple + 1
        print(my_list)
        return my_list
    except Exception as e:
        print(e)



eratosthenes(120)

#if __name__ == "__main__":
#        import sys
#        eratosthenes(int(sys.argv[1]))


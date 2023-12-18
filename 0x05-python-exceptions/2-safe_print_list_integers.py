#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    start = 0
    for index in range(x):
        try:
            if (isinstance(my_list[index], int)):
                print("{:d}".format(my_list[index]), end="")
            start += 1
        except (ValueError, TypeError):
            pass
    print()
    return start

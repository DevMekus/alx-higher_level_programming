#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dictry = dict(a_dictionary)
    for key, value in my_dictry.items():
        my_dictry[key] = value * 2
    return my_dictry

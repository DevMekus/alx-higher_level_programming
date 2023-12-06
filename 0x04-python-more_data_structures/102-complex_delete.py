i#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listkeys = list(a_dictionary.keys())

    for value_a in listkeys:
        if value == a_dictionary.get(value_a):
            del a_dictionary[value_a]

    return (a_dictionary)

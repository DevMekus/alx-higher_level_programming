#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmporary = my_dict.copy()
    for key, values in tmporary.items():
        if value == values:
            my_dict.pop(key)
    return my_dict

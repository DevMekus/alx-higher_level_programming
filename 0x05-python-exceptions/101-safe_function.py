#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        answer = fct(*args)
        return answer
    except Exception as errors:
        print("Exception: {}".format(errors), file=sys.stderr)
        return None

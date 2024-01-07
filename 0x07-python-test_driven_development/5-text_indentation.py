#!/usr/bin/python3

"""Text Indentation Function"""


def text_indentation(text):
    """After each '.', '?', and ':' Print text with two new lines.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    d = 0
    while d < len(text) and text[d] == ' ':
        d += 1

    while d < len(text):
        print(text[d], end="")
        if text[d] == "\n" or text[d] in ".?:":
            if text[d] in ".?:":
                print("\n")
            d += 1
            while d < len(text) and text[d] == ' ':
                d += 1
            continue
        d += 1
